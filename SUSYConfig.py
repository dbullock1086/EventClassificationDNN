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
    InputData = os.getenv('SampleDirSUSY') + '/' + InputData
    Samples += [ [InputData, 'AA_Gen'],
                 [InputData, 'AB_Gen'],
                 [InputData, 'BA_Gen'],
                 [InputData, 'BB_Gen'] ]
    pass

#Previously in InputVars.py
# Select Variables To use in training

# used for scaling
Observables = {
    'mP': {},
    'mC': {},
    'mX': {},
    'B1_pT': {'trim': [0, 99]},
    'B1_phi': {'range': [-np.pi, np.pi]},
    'B1_eta': {'range': [-2.5, 2.5]},
    'B1_M': {'trim': [0, 99]},
    'B2_pT': {'trim': [0, 99]},
    'B2_phi': {'range': [-np.pi, np.pi]},
    'B2_eta': {'range': [-2.5, 2.5]},
    'B2_M': {'trim': [0, 99]},
    'L1_pT': {'trim': [0, 99]},
    'L1_phi': {'range': [-np.pi, np.pi]},
    'L1_eta': {'range': [-2.5, 2.5]},
    'L1_M': {'trim': [0, 99]},
    'L2_pT': {'trim': [0, 99]},
    'L2_phi': {'range': [-np.pi, np.pi]},
    'L2_eta': {'range': [-2.5, 2.5]},
    'L2_M': {'trim': [0, 99]},
    'METx': {'trim': [0, 99]},
    'METy': {'trim': [0, 99]},
    'MPP_AA': {},
    'Eb_a_AA': {},
    'Eb_b_AA': {},
    'El_a_AA': {},
    'El_b_AA': {},
    'MPP_BB': {},
    'Eb_a_BB': {},
    'Eb_b_BB': {},
    'El_a_BB': {},
    'El_b_BB': {},
    'MPP_AB': {},
    'Eb_a_AB': {},
    'Eb_b_AB': {},
    'El_a_AB': {},
    'El_b_AB': {},
    'MPP_BA': {},
    'Eb_a_BA': {},
    'Eb_b_BA': {},
    'El_a_BA': {},
    'El_b_BA': {},
    'cosPP_AA': {'range': [0, 1]},
    'cosPP_AB': {'range': [0, 1]},
    'cosPP_BA': {'range': [0, 1]},
    'cosPP_BB': {'range': [0, 1]},
    'cosPa_AA': {'range': [0, 1]},
    'cosPa_AB': {'range': [0, 1]},
    'cosPa_BA': {'range': [0, 1]},
    'cosPa_BB': {'range': [0, 1]},
    'cosPb_AA': {'range': [0, 1]},
    'cosPb_AB': {'range': [0, 1]},
    'cosPb_BA': {'range': [0, 1]},
    'cosPb_BB': {'range': [0, 1]},
    'cosCa_AA': {'range': [0, 1]},
    'cosCa_AB': {'range': [0, 1]},
    'cosCa_BA': {'range': [0, 1]},
    'cosCa_BB': {'range': [0, 1]},
    'cosCb_AA': {'range': [0, 1]},
    'cosCb_AB': {'range': [0, 1]},
    'cosCb_BA': {'range': [0, 1]},
    'cosCb_BB': {'range': [0, 1]},
    'dphi_PP_Pa_AA': {'range': [0, np.pi]},
    'dphi_PP_Pa_BB': {'range': [0, np.pi]},
    'dphi_PP_Pa_AB': {'range': [0, np.pi]},
    'dphi_PP_Pa_BA': {'range': [0, np.pi]},
    'dphi_PP_Pb_AA': {'range': [0, np.pi]},
    'dphi_PP_Pb_BB': {'range': [0, np.pi]},
    'dphi_PP_Pb_AB': {'range': [0, np.pi]},
    'dphi_PP_Pb_BA': {'range': [0, np.pi]},
    'dphi_Pa_Ca_AA': {'range': [0, np.pi]},
    'dphi_Pa_Ca_BB': {'range': [0, np.pi]},
    'dphi_Pa_Ca_AB': {'range': [0, np.pi]},
    'dphi_Pa_Ca_BA': {'range': [0, np.pi]},
    'dphi_Pb_Cb_AA': {'range': [0, np.pi]},
    'dphi_Pb_Cb_BB': {'range': [0, np.pi]},
    'dphi_Pb_Cb_AB': {'range': [0, np.pi]},
    'dphi_Pb_Cb_BA': {'range': [0, np.pi]},
    }

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

Params = {'Width': [1585],
          'Depth': [1],
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
