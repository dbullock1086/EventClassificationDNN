from DLTools.Permutator import *

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
Samples = []
for InputData in InputFiles:
    InputData = os.getenv('SampleDir') + '/' + InputData
    Sanples += [ [InputData, 'AA_Gen'],
                 [InputData, 'AB_Gen'],
                 [InputData, 'BA_Gen'],
                 [InputData, 'BB_Gen'] ]
    pass

#Previously in InputVars.py
# Select Variables To use in training

# used for scaling
Observables = [
    # energy scale
    'mP', 'mC', 'mX',
    'METx', 'METy',
    'L1_pT', 'L1_M',
    'L2_pT','L2_M',
    'B1_pT','B1_M',
    'B2_pT','B2_M',
    'MPP_AA', 'Eb_a_AA', 'Eb_b_AA', 'El_a_AA', 'El_b_AA',
    'MPP_BB', 'Eb_a_BB', 'Eb_b_BB', 'El_a_BB', 'El_b_BB',
    'MPP_AB', 'Eb_a_AB', 'Eb_b_AB', 'El_a_AB', 'El_b_AB',
    'MPP_BA', 'Eb_a_BA', 'Eb_b_BA', 'El_a_BA', 'El_b_BA',

    # pseudo rapidity
    'L1_eta', 'L2_eta',  'B1_eta','B2_eta',

    # azimutahl angle
    'L1_phi', 'L2_phi','B1_phi', 'B2_phi',

    # decay angles (by frame)
    'cosPP_AA', 'cosPP_AB', 'cosPP_BA', 'cosPP_BB',
    'cosPa_AA', 'cosPa_AB', 'cosPa_BA', 'cosPa_BB',
    'cosPb_AA', 'cosPb_AB', 'cosPb_BA', 'cosPb_BB',
    'cosCa_AA', 'cosCa_AB', 'cosCa_BA', 'cosCa_BB',
    'cosCb_AA', 'cosCb_AB', 'cosCb_BA', 'cosCb_BB',

    # separation angles (by frame)
    'dphi_PP_Pa_AA', 'dphi_PP_Pa_BB', 'dphi_PP_Pa_AB', 'dphi_PP_Pa_BA',
    'dphi_PP_Pb_AA', 'dphi_PP_Pb_BB', 'dphi_PP_Pb_AB', 'dphi_PP_Pb_BA',
    'dphi_Pa_Ca_AA', 'dphi_Pa_Ca_BB', 'dphi_Pa_Ca_AB', 'dphi_Pa_Ca_BA',
    'dphi_Pb_Cb_AA', 'dphi_Pb_Cb_BB', 'dphi_Pb_Cb_AB', 'dphi_Pb_Cb_BA',
]

SelectedFields = [
    # all observables
    ['mP', 'mC', 'mX',
     'METx', 'METy',
     'L1_pT', 'L1_eta', 'L1_phi', 'L1_M',
     'L2_pT', 'L2_eta', 'L2_phi', 'L2_M',
     'B1_pT', 'B1_eta', 'B1_phi', 'B1_M',
     'B2_pT', 'B2_eta', 'B2_phi', 'B2_M',
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
     'L1_pT', 'L1_eta', 'L1_phi', 'L1_M',
     'L2_pT', 'L2_eta', 'L2_phi', 'L2_M',
     'B1_pT', 'B1_eta', 'B1_phi', 'B1_M',
     'B2_pT', 'B2_eta', 'B2_phi', 'B2_M'],

    # physics reconstruction
    ['mP', 'mC', 'mX',
     'METx', 'METy',
     'L1_pT', 'L1_eta', 'L1_phi', 'L1_M',
     'L2_pT', 'L2_eta', 'L2_phi', 'L2_M',
     'B1_pT', 'B1_eta', 'B1_phi', 'B1_M',
     'B2_pT', 'B2_eta', 'B2_phi', 'B2_M'],

    # recursive jigsaw reconstruction
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

    # single topology reconstruction
    ['MPP_AA', 'Eb_a_AA', 'Eb_b_AA', 'El_a_AA', 'El_b_AA',
     'cosPP_AA', 'cosPa_AA', 'cosPb_AA', 'cosCa_AA', 'cosCb_AA',
     'dphi_PP_Pa_AA', 'dphi_PP_Pb_AA', 'dphi_Pa_Ca_AA', 'dphi_Pb_Cb_AA'],

    # adjusted recursive jigsaw reconstruction
    ['mP', 'mC', 'mX',
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
]

Name = 'SUSYModel'

Config = {'MaxEvents':    50000,
          'Epochs':       10000,
          'BatchSize':   2048*8,
          'LearningRate': 0.005,
          'Decay':           0.,
          'Momentum':        0.,
          'Nesterov':        0.,
          'arrType':      float,
          'WeightInitialization':"'normal'"}

Params = {'Width': [1024],
          'Depth': [2],
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
