import random
import getopt
from DLTools.Permutator import *
import sys,argparse

#Previously in InputFiles.py
# Define the Input Files
InputFiles = ['mP1000_mC150_mX100.h5',
              'mP1000_mC400_mX100.h5',
              'mP1000_mC600_mX100.h5',
              'mP1000_mC900_mX100.h5',
              'mP1000_mC200_mX100.h5',
              'mP1000_mC500_mX100.h5',
              'mP1000_mC700_mX100.h5',
              'mP1000_mC950_mX100.h5',
              'mP1000_mC300_mX100.h5',
              'mP1000_mC550_mX100.h5',
              'mP1000_mC800_mX100.h5']

# Select datasets (formerly TTrees in original ROOT file)
Files = []
for InputData in InputFiles:
    InputData = '/scratch/data-backup/afarbin/crogan/h5/' + InputData
    #InputData = '/afs/cern.ch/work/a/afarbin/public/RestFrames-llbbMET/' + InputData
    Files += [ [InputData, 'AA_Gen'],
               [InputData, 'AB_Gen'],
               [InputData, 'BA_Gen'],
               [InputData, 'BB_Gen'] ]
    pass

Samples = []

for F in Files:
    if type(F) != str: Samples.append(F)
    else:
        name = F.split('.')[0].split('/')[-1]
        Samples.append ( [F,name+'_SRAll'] )
        pass
    pass

#Previously in InputVars.py
# Select Variables To use in training
FieldGroups = [    
    ['mP', 'mC', 'mX',
     'METx', 'METy',
     'L1_M', 'L1_pT', 'L1_phi', 'L1_eta',
     'L2_M', 'L2_pT', 'L2_phi', 'L2_eta',
     'B1_M', 'B1_pT', 'B1_phi', 'B1_eta',
     'B2_M', 'B2_pT', 'B2_phi', 'B2_eta',
     'MPP_AA', 'Eb_a_AA', 'Eb_b_AA', 'El_a_AA', 'El_b_AA',
     'MPP_AB', 'Eb_a_AB', 'Eb_b_AB', 'El_a_AB', 'El_b_AB',
     'MPP_BA', 'Eb_a_BA', 'Eb_b_BA', 'El_a_BA', 'El_b_BA',
     'MPP_BB', 'Eb_a_BB', 'Eb_b_BB', 'El_a_BB', 'El_b_BB',
     'cosPP_AA', 'cosPa_AA', 'cosPb_AA', 'cosCa_AA', 'cosCb_AA',
     'cosPP_AB', 'cosPa_AB', 'cosPb_AB', 'cosCa_AB', 'cosCb_AB',
     'cosPP_BA', 'cosPa_BA', 'cosPb_BA', 'cosCa_BA', 'cosCb_BA',
     'cosPP_BB', 'cosPa_BB', 'cosPb_BB', 'cosCa_BB', 'cosCb_BB',
     'dphi_PP_Pa_AA', 'dphi_PP_Pb_AA', 'dphi_Pa_Ca_AA', 'dphi_Pb_Cb_AA',
     'dphi_PP_Pa_AB', 'dphi_PP_Pb_AB', 'dphi_Pa_Ca_AB', 'dphi_Pb_Cb_AB',
     'dphi_PP_Pa_BA', 'dphi_PP_Pb_BA', 'dphi_Pa_Ca_BA', 'dphi_Pb_Cb_BA',
     'dphi_PP_Pa_BB', 'dphi_PP_Pb_BB', 'dphi_Pa_Ca_BB', 'dphi_Pb_Cb_BB']
]

SelectedFields = [
    # all reconstruction
    ['mP', 'mC', 'mX',
     'METx', 'METy',
     'L1_M', 'L1_pT', 'L1_phi', 'L1_eta',
     'L2_M', 'L2_pT', 'L2_phi', 'L2_eta',
     'B1_M', 'B1_pT', 'B1_phi', 'B1_eta',
     'B2_M', 'B2_pT', 'B2_phi', 'B2_eta',
     'MPP_AA', 'Eb_a_AA', 'Eb_b_AA', 'El_a_AA', 'El_b_AA',
     'MPP_AB', 'Eb_a_AB', 'Eb_b_AB', 'El_a_AB', 'El_b_AB',
     'MPP_BA', 'Eb_a_BA', 'Eb_b_BA', 'El_a_BA', 'El_b_BA',
     'MPP_BB', 'Eb_a_BB', 'Eb_b_BB', 'El_a_BB', 'El_b_BB',
     'cosPP_AA', 'cosPa_AA', 'cosPb_AA', 'cosCa_AA', 'cosCb_AA',
     'cosPP_AB', 'cosPa_AB', 'cosPb_AB', 'cosCa_AB', 'cosCb_AB',
     'cosPP_BA', 'cosPa_BA', 'cosPb_BA', 'cosCa_BA', 'cosCb_BA',
     'cosPP_BB', 'cosPa_BB', 'cosPb_BB', 'cosCa_BB', 'cosCb_BB',
     'dphi_PP_Pa_AA', 'dphi_PP_Pb_AA', 'dphi_Pa_Ca_AA', 'dphi_Pb_Cb_AA',
     'dphi_PP_Pa_AB', 'dphi_PP_Pb_AB', 'dphi_Pa_Ca_AB', 'dphi_Pb_Cb_AB',
     'dphi_PP_Pa_BA', 'dphi_PP_Pb_BA', 'dphi_Pa_Ca_BA', 'dphi_Pb_Cb_BA',
     'dphi_PP_Pa_BB', 'dphi_PP_Pb_BB', 'dphi_Pa_Ca_BB', 'dphi_Pb_Cb_BB'],

    # detector reconstruction
    ['METx', 'METy',
     'L1_pT', 'L1_phi', 'L1_eta',
     'L2_pT', 'L2_phi', 'L2_eta',
     'B1_pT', 'B1_phi', 'B1_eta',
     'B2_pT', 'B2_phi', 'B2_eta'],

    # particle reconstruction
    ['METx', 'METy',
     'L1_M', 'L1_pT', 'L1_phi', 'L1_eta',
     'L2_M', 'L2_pT', 'L2_phi', 'L2_eta',
     'B1_M', 'B1_pT', 'B1_phi', 'B1_eta',
     'B2_M', 'B2_pT', 'B2_phi', 'B2_eta'],

    # physics reconstruction
    ['mP', 'mC', 'mX',
     'METx', 'METy',
     'L1_M', 'L1_pT', 'L1_phi', 'L1_eta',
     'L2_M', 'L2_pT', 'L2_phi', 'L2_eta',
     'B1_M', 'B1_pT', 'B1_phi', 'B1_eta',
     'B2_M', 'B2_pT', 'B2_phi', 'B2_eta'],

    # Recursive Jigsaw reconstruction
    ['MPP_AA', 'Eb_a_AA', 'Eb_b_AA', 'El_a_AA', 'El_b_AA',
     'MPP_AB', 'Eb_a_AB', 'Eb_b_AB', 'El_a_AB', 'El_b_AB',
     'MPP_BA', 'Eb_a_BA', 'Eb_b_BA', 'El_a_BA', 'El_b_BA',
     'MPP_BB', 'Eb_a_BB', 'Eb_b_BB', 'El_a_BB', 'El_b_BB',
     'cosPP_AA', 'cosPa_AA', 'cosPb_AA', 'cosCa_AA', 'cosCb_AA',
     'cosPP_AB', 'cosPa_AB', 'cosPb_AB', 'cosCa_AB', 'cosCb_AB',
     'cosPP_BA', 'cosPa_BA', 'cosPb_BA', 'cosCa_BA', 'cosCb_BA',
     'cosPP_BB', 'cosPa_BB', 'cosPb_BB', 'cosCa_BB', 'cosCb_BB',
     'dphi_PP_Pa_AA', 'dphi_PP_Pb_AA', 'dphi_Pa_Ca_AA', 'dphi_Pb_Cb_AA',
     'dphi_PP_Pa_AB', 'dphi_PP_Pb_AB', 'dphi_Pa_Ca_AB', 'dphi_Pb_Cb_AB',
     'dphi_PP_Pa_BA', 'dphi_PP_Pb_BA', 'dphi_Pa_Ca_BA', 'dphi_Pb_Cb_BA',
     'dphi_PP_Pa_BB', 'dphi_PP_Pb_BB', 'dphi_Pa_Ca_BB', 'dphi_Pb_Cb_BB'],
]

Name = 'TrainedModel'

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
