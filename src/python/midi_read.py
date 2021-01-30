#!BPY
# -*- coding: UTF-8 -*-
# Read MIDI File
#
# 2017.10.12 Natukikazemizo
#

import bpy
import os
import utils_log
import utils_io_csv
import pretty_midi
import math

# CONSTANT OF PARAMETERS
PIANO_ARMATURE_NAME = "Piano_Armature"
START_FRAME = 3000
FPS = 24
BONE_ON_Y = 0.009
DOWN_FRAME = 3
UP_FRAME = 2
VELOCITY_MAX = 127
INSTRUMENTS_CNT = 4

# BONE_NAME PER PITCH
BONE_PITCH_DIC={
    21:"A_T.000",
    22:"A#_T.000",
    23:"B_T.000",
    24:"C_T.001",
    25:"C#_T.001",
    26:"D_T.001",
    27:"D#_T.001",
    28:"E_T.001",
    29:"F_T.001",
    30:"F#_T.001",
    31:"G_T.001",
    32:"G#_T.001",
    33:"A_T.001",
    34:"A#_T.001",
    35:"B_T.001", 
    36:"C_T.002",
    37:"C#_T.002",
    38:"D_T.002",
    39:"D#_T.002",
    40:"E_T.002",
    41:"F_T.002",
    42:"F#_T.002",
    43:"G_T.002",
    44:"G#_T.002",
    45:"A_T.002",
    46:"A#_T.002",
    47:"B_T.002",
    48:"C_T.003",
    49:"C#_T.003",
    50:"D_T.003",
    51:"D#_T.003",
    52:"E_T.003",
    53:"F_T.003",
    54:"F#_T.003",
    55:"G_T.003",
    56:"G#_T.003",
    57:"A_T.003",
    58:"A#_T.003",
    59:"B_T.003",
    60:"C_T.004",
    61:"C#_T.004",
    62:"D_T.004",
    63:"D#_T.004",
    64:"E_T.004",
    65:"F_T.004",
    66:"F#_T.004",
    67:"G_T.004",
    68:"G#_T.004",
    69:"A_T.004",
    70:"A#_T.004",
    71:"B_T.004",
    72:"C_T.005",
    73:"C#_T.005",
    74:"D_T.005",
    75:"D#_T.005",
    76:"E_T.005",
    77:"F_T.005",
    78:"F#_T.005",
    79:"G_T.005",
    80:"G#_T.005",
    81:"A_T.005",
    82:"A#_T.005",
    83:"B_T.005",
    84:"C_T.006",
    85:"C#_T.006",
    86:"D_T.006",
    87:"D#_T.006",
    88:"E_T.006",
    89:"F_T.006",
    90:"F#_T.006",
    91:"G_T.006",
    92:"G#_T.006",
    93:"A_T.006",
    94:"A#_T.006",
    95:"B_T.006",
    96:"C_T.007",
    97:"C#_T.007",
    98:"D_T.007",
    99:"D#_T.007",
    100:"E_T.007",
    101:"F_T.007",
    102:"F#_T.007",
    103:"G_T.007",
    104:"G#_T.007",
    105:"A_T.007",
    106:"A#_T.007",
    107:"B_T.007",
    108:"C_T.008"  
  }

# init logger
global logger
logger = utils_log.Util_Log(os.path.basename(__file__))

logger.start()

midi_data = pretty_midi.PrettyMIDI(bpy.path.abspath("//") + "data/MIDI/yamato_piano_rendan.mid")

## GET 1ST TEMPO
#tempo = math.floor(midi_data.get_tempo_changes()[1][0])
## GET MUSICAL TIME
#numerator = midi_data.time_signature_changes[0].numerator
#denominator = midi_data.time_signature_changes[0].denominator

piano = bpy.data.objects[PIANO_ARMATURE_NAME]

for index in range(INSTRUMENTS_CNT):
    print(midi_data.instruments[index])
    for note in midi_data.instruments[index].notes:
        print(note)
        ctrl_bone = piano.pose.bones[BONE_PITCH_DIC[note.pitch]]
        
        note_pre_frame = START_FRAME + math.floor(145 * FPS / 120 * note.start)
        #note_start_frame = note_pre_frame + math.floor(DOWN_FRAME * note.velocity / VELOCITY_MAX)
        note_start_frame = note_pre_frame + 1
        #note_end_frame = START_FRAME + math.floor(145 * FPS / 120 * note.end) - UP_FRAME
        note_end_frame = START_FRAME + math.floor(145 * FPS / 120 * note.end) - 2
        
        note_up_frame = note_end_frame + 1
        
        # + UP_FRAME
        
        #if note_start_frame > note_end_frame:
        #    note_start_frame = note_up_frame - 2
        #    note_end_frame = note_up_frame - 1
        
        # INSERT KEY FRAMES
        ctrl_bone.location = 0, 0, 0
        ctrl_bone.keyframe_insert(data_path = "location", frame = note_pre_frame)
        ctrl_bone.location = 0, BONE_ON_Y, 0
        ctrl_bone.keyframe_insert(data_path = "location", frame = note_start_frame)
        ctrl_bone.location = 0, BONE_ON_Y, 0
        ctrl_bone.keyframe_insert(data_path = "location", frame = note_end_frame)
        ctrl_bone.location = 0, 0, 0
        ctrl_bone.keyframe_insert(data_path = "location", frame = note_up_frame)

logger.end()

