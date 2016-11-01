import random
import getopt
from DLTools.Permutator import *
import sys,argparse

#Previously in InputFiles.py
# Define the Input Files
InputFiles = ['Zll.h5']

# Select datasets (formerly TTrees in original ROOT file)
Files = []
for InputData in InputFiles:
    InputData = '/home/dbullock/samples' + InputData
    #InputData = '/afs/cern.ch/work/d/dbullock/public/samples/dnn-tutorial/' + InputData
    Files += [ [InputData, 'Zto2LOS'],
               [InputData, '2LOS'] ]
    pass

Samples = []

for F in Files: Samples.append(F)

#Previously in InputVars.py
# Select Variables To use in training
FieldGroups = [
    # energy scale
    ['LP_pT', 'LP_E',
     'LM_pT', 'LM_E']

    # transverse angle
    ['LP_phi', 'LM_phi'],

    # pseudorapidity
    ['LP_eta', 'LM_eta'],
]

SelectedFields = [
    ['LP_pT', 'LP_eta', 'LP_phi', 'LP_E',
     'LM_pT', 'LM_eta', 'LM_phi', 'LM_E']
]

Name = 'ZllModel'

Config = {'MaxEvents':    50000,
          'Epochs':       10000,
          'BatchSize':   2048*8,
          'LearningRate': 0.005,
          'Decay':           0.,
          'Momentum':        0.,
          'Nesterov':        0.,
          'WeightInitialization':"'normal'"}

Params = {'Width': [128],
          'Depth':   [2],
          'loss': ["'categorical_crossentropy'"]}

PS = Permutator (Params)
Combos = PS.Permutations ()

print 'HyperParameter Scan:', len(Combos), 'possible combinations.'

if 'HyperParamSet' in dir(): i = int(HyperParamSet)
else:
    # Set Seed based on time
    random.seed()
    i = int(round( len(Combos)*random.random() ))
    print 'Randomly picking HyperParameter Set'
    pass

if i < 0:
    print 'SetList:'
    for j in xrange(len(Combos)): print j, ':', Combos[j]
    quit()
    pass

print 'Picked combination:', i

for k in Combos[i]: Config[k] = Combos[i][k]

#for MetaData in Params:
#    val = str(Config[MetaData]).replace ('"','')
#    Name += '_' + val
#    pass

#print 'Model Filename:', Name
