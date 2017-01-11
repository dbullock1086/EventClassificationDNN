import datetime
a = datetime.datetime.now()
print a.ctime()

import os

# Parse Arguments
execfile ('EventClassificationDNN/Arguments.py')

# Now load the Hyperparameters
import numpy as np
execfile (ConfigFile)

if 'Config' in dir():
    for a in Config:
        if a != 'arrType': exec (a + '=' + str(Config[a]))
        pass
    pass

# Load the Data
import h5py
from EventClassificationDNN.MultiClassTools import *

(Train_X, Train_Y), (Test_X, Test_Y), ClassIndex = LoadData (Samples, .1, MaxEvents=MaxEvents)
 
# Select Variables To use in training
# To get the field names, just look at Fields=Train_X.dtype.names

# Keep the original data before renomalizing... will use this in output
Train_X0 = Train_X.copy()
Test_X0 = Test_X.copy()

#### Trimming
print 'Trimming outliers from data ...'
num = Train_X.shape[0]
for obs in Observables:
    if not Observables[obs].has_key('trim'): continue
    print '   ', obs
    if Observables[obs]['trim'][0] < 0: lower = -np.inf
    else: lower = np.nanpercentile(Train_X[obs], Observables[obs]['trim'][0])
    if Observables[obs]['trim'][1] > 100: upper = np.inf
    else: upper = np.nanpercentile(Train_X[obs], Observables[obs]['trim'][1])
    for evt in xrange(num):
        val = Train_X[obs][evt]
        if np.isnan(val) or np.isinf(val) or np.isneginf(val):
            Train_X[obs][evt] = np.nan
            pass
        elif val > upper:
            Train_X[obs][evt] = np.nan
            pass
        elif val < lower:
            Train_X[obs][val] = np.nan
            pass
        pass
    pass
for evt in xrange(num):
    if any(np.isnan(Train_X[obs][evt]) for obs in Observables):
        for obs in Observables:
            Train_X[obs][evt] = np.nan
            pass
        pass
    pass

#### Shifting/Scaling normalization
print 'Normalizing', obs, '...'
for obs in Observables:
    print '   ', obs
    if Observables[obs].has_key('range'):
        minval = Observables[obs]['range'][0]
        maxval = Observables[obs]['range'][1]
        pass
    else:
        minval = np.min(Train_X[obs])
        maxval = np.max(Train_X[obs])
        pass
    yy = Train_X[obs]
    yy[:] = 1./(maxval-minval) * (yy-minval)
    yy1 = Test_X[obs]
    yy1[:] = 1./(maxval-minval) * (yy1-minval)
    # gaus
    #yy = Train_X[obs]
    #yy1 = Train_X[obs]
    #M = np.mean (Train_X0[obs])
    #V = np.var (Train_X0[obs])
    #yy[:] = (yy - M) / V + .5
    #yy1[:] = (yy1 - M) / V + .5
    pass
pass

#Train_X_N = Train_X

# Keep Only selected Variables
Train_X = Train_X[SelectedFields[VarSet]]
Test_X = Test_X[SelectedFields[VarSet]]

#Train_X_S = Train_X

# Now Lets Simplify the structure (Note this requires everything to be a float)
# If you get an error that the input size isn't right, try changing float below to float32 or float64
Train_X = Train_X.view(Config['arrType']).reshape(Train_X.shape + (-1,))
Test_X = Test_X.view(Config['arrType']).reshape(Test_X.shape + (-1,))

# Protect against divide by zero! 
Train_X = np.nan_to_num(Train_X)
Test_X = np.nan_to_num(Test_X)

# Get some Inof
N_Inputs = len(SelectedFields[VarSet])
N_Classes = np.shape(Train_Y)[1]
print 'N Inputs:', N_Inputs
print 'Width:', Width
print 'N Classes:', N_Classes

# Now Build the Model
from DLTools.ModelWrapper import *

# Build the Model
from EventClassificationDNN.Classification import FullyConnectedClassification

if LoadModel:
    print 'Loading Model From:', LoadModel
    if LoadModel[-1]=='/': LoadModel = LoadModel[:-1]
    Name = os.path.basename (LoadModel)
    MyModel = ModelWrapper (Name)
    MyModel.InDir = LoadModel
    MyModel.Load()
    pass
else:
    Name += '_%s' % VarSet
    print 'Model Filename:', Name
    MyModel = FullyConnectedClassification (Name, N_Inputs, Width, Depth, N_Classes, WeightInitialization)
    MyModel.Build ()
    pass

MyModel.MetaData['Config'] = Config

# Compile the Model
print 'Compiling the Model... this will take a while.'

optimizer = 'sgd'
MyModel.Compile (Loss=loss, Optimizer=optimizer)

model = MyModel.Model
# Print the summary
model.summary ()

if Train:
    print 'Training.'
    hist = MyModel.Train(Train_X, Train_Y, Epochs, BatchSize)
    score = model.evaluate(Test_X, Test_Y , batch_size=BatchSize)
    print 'Final Score:',score
    MyModel.MetaData['FinalScore'] = score
    pass

# Save 
MyModel.Save ()

# Analysis
from EventClassificationDNN.Analysis import MultiClassificationAnalysis
result = MultiClassificationAnalysis (MyModel, Test_X, Test_Y, BatchSize)

# Dump out the predictions added to the input
if WriteResults:
    print 'Writing Results.'
    from EventClassificationDNN.CSVWriter import *
    CSVWriter (MyModel.OutDir+'/Result.csv', Test_X0, Test_Y, result, Config['arrType'])
    pass

a = datetime.datetime.now()
print a.ctime()
