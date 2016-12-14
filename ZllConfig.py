from DLTools.Permutator import *

#Previously in InputFiles.py
# Define the Input Files
InputFiles = ['Zll.h5']

# Select datasets (formerly TTrees in original ROOT file)
Samples = []
for InputData in InputFiles:
    InputData = os.getenv('SampleDir') + '/' + InputData
    Samples += [ [InputData, 'Zto2LOS'],
                 [InputData, 'Rndm2LOS'] ]
    pass

#Previously in InputVars.py
# Select Variables To use in training
Observables = {
    # group similar
    'Group': [
        ['LP_pT', 'LP_E',
         'LM_pT', 'LM_E'],
        ['LP_phi', 'LM_phi'],
        ['LP_eta', 'LM_eta'],
    ],
}

SelectedFields = [
    # all variables
    ['LP_pT', 'LP_eta', 'LP_phi', 'LP_E',
     'LM_pT', 'LM_eta', 'LM_phi', 'LM_E'],

    # known differences
    ['LP_phi', 'LM_phi'],    
]

Name = 'ZllModel'

Config = {'MaxEvents':    50000,
          'Epochs':       1000,
          'BatchSize':   2048*8,
          'LearningRate': 0.005,
          'Decay':           0.,
          'Momentum':        0.,
          'Nesterov':        0.,
          'WeightInitialization':"'normal'"}

Params = {'Width': [1585],
          'Depth': [1],
          'loss': ["'categorical_crossentropy'"]}

arrType = np.float32

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
