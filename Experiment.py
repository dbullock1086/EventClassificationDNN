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
    for a in Config: exec (a + '=' + str(Config[a]))
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

#### Normalization
for scheme in Observables:
    if scheme == 'Group':
        for grp in Observables[scheme]:
            Mins = []
            Maxs = []
            for obs in grp:
                Mins.append ( np.min(Train_X0[obs]) )
                Maxs.append ( np.max(Train_X0[obs]) )
                pass
            minval = min(Mins)
            maxval = max(Maxs)
            for obs in grp:
                yy = Train_X[obs]
                yy[:] = 1./(maxval-minval) * (yy-minval)
                yy1 = Test_X[obs]
                yy1[:] = 1./(maxval-minval) * (yy1-minval)
                pass
            pass
        continue
    for obs in Observables[scheme]:
        print 'Normalizing', obs, 'to', scheme, '...'
        yy = Train_X[obs]
        yy1 = Train_X[obs]
        if scheme == 'Gaus': # Gaus variance set to [0,1]
            M = np.mean (Train_X0[obs])
            V = np.var (Train_X0[obs])
            yy[:] = (yy - M) / V + .5
            yy1[:] = (yy1 - M) / V + .5
            pass
        else:
            if scheme == 'Full':
                lower = 0
                upper = 10001
                pass
            elif scheme == 'LeftTrim':
                lower = 2500
                upper = 10001
                pass
            elif scheme == 'RightTrim':
                lower = 0
                upper = 7501
                pass
            elif scheme == 'IQR':
                lower = 2500
                upper = 7501
                pass
            nanpct = np.nanpercentile (Train_X0[obs], np.arange(lower,upper)/100.)
            for itrv in xrange(len(yy)):
                val = yy[itrv]
                if np.isnan(val) or np.isinf(val) or np.isneginf(val): continue
                for itrw in xrange(len(nanpct)):
                    weight = (lower+itrw)/10000.
                    if val >= weight:
                        # left-trimmed range shifted to [0, 1]
                        if scheme == 'LeftTrim': shift = 4. * (weight-.25) / 3.
                        # right-trimmed range shifted to [0, 1]
                        elif scheme == 'RightTrim': shift = 4. * weight / 3.
                        # IQR shifted to [0, 1]
                        elif scheme == 'IQR': shift = 2. * weight - .5
                        # full range shifted to [0,1]
                        else: shift = weight
                        yy[itrv] = shift
                        yy1[itrv] = shift
                        pass
                    break
                # default to NaN
                yy[itrv] = np.nan
                yy1[itrv] = np.nan
                pass
            pass
        pass
    pass

#Train_X_N = Train_X

# Keep Only selected Variables
Train_X = Train_X[SelectedFields[VarSet]]
Test_X = Test_X[SelectedFields[VarSet]]

#Train_X_S = Train_X

# Now Lets Simplify the structure (Note this requires everything to be a float)
# If you get an error that the input size isn't right, try changing float below to float32 or float64
Train_X = Train_X.view(arrType).reshape(Train_X.shape + (-1,))
Test_X = Test_X.view(arrType).reshape(Test_X.shape + (-1,))

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
    CSVWriter (MyModel.OutDir+'/Result.csv', Test_X0, Test_Y, result, arrType)
    pass

a = datetime.datetime.now()
print a.ctime()
