#keyMaps are dictionnary used to interprete midisignal
# there is one dictionary per instrument, with one dictionary per possible message type, with one dictionnary per key value

keyMapDic = {
    'layout':{
        'note':{
            'preset':{
                    'name' : 'A#2',
                    'start_signal': 'note_on',
                    'release_signal': 'note_on',
                    'treshold' : 5,
                    'retrigger' : 10,
                    'curve' :  'linear',#log2
 
                
            }
        },
        'control':{},
    },
    'DM10':{
        'note':{
            'preset':{
                    'start_signal': 'note_on',
                    'release_signal': None,
                    'treshold' : 5,
                    'retrigger' : 10,
                    'curve' :  'linear',#log2
 
                
            },
            46 : {
                'name': 'charleston'
            },
            38 : {
                'name' : 'snare'
            },
            40 : {
                'name' : 'snare_ring'
            },
            47 : {
                'name' : 'tom_1'
            },
            45 : {
                'name' : 'tom_2'
            },
            48 : {
                'name' : 'tom_2_ring'
            },
            63 : {
                'name' : 'tom_3'
            },
            64 : {
                'name' : 'tom_3_ring'
            },
            43 : {
                'name' : 'tom_4'
            },
            41 : {
                'name' : 'tom_4_ring'
            },
            
            36 : {
                'name' : 'kick'
            },
            49 : {
                'name' : 'cymbal_1'
            },
            34 : {
                'name' : 'cymbal_1_stop'
            },
            51 : {
                'name' : 'cymbal_2'
            },
            53 : {
                'name' : 'cymbal_2_bell'
            },
            26 : {
                'name' : 'cymbal_2_stop'
            },
            60 : {
                'name' : 'cymbal_2'
            },
        },
        'control':{},
    },
    'Keyboard':{
        'note':{
            'preset':{
                    'start_signal': 'note_on',
                    'release_signal': 'note_off',
                    'treshold' : 5,
                    'retrigger' : 10,
                    'curve' :  'linear',#log2
 
                
            },

            21: {'name': 'A0'},
            22: {'name': 'A#0'},
            23: {'name': 'B0'},
            24: {'name': 'C1'},
            25: {'name': 'C#1'},
            26: {'name': 'D1'},
            27: {'name': 'D#1'},
            28: {'name': 'E1'},
            29: {'name': 'F1'},
            30: {'name': 'F#1'},
            31: {'name': 'G1'},
            32: {'name': 'G#1'},
            33: {'name': 'A1'},
            34: {'name': 'A#1'},
            35: {'name': 'B1'},
            36: {'name': 'C2'},
            37: {'name': 'C#2'},
            38: {'name': 'D2'},
            39: {'name': 'D#2'},
            40: {'name': 'E2'},
            41: {'name': 'F2'},
            42: {'name': 'F#2'},
            43: {'name': 'G2'},
            44: {'name': 'G#2'},
            45: {'name': 'A2'},
            46: {'name': 'A#2'},
            47: {'name': 'B2'},
            48: {'name': 'C3'},
            49: {'name': 'C#3'},
            50: {'name': 'D3'},
            51: {'name': 'D#3'},
            52: {'name': 'E3'},
            53: {'name': 'F3'},
            54: {'name': 'F#3'},
            55: {'name': 'G3'},
            56: {'name': 'G#3'},
            57: {'name': 'A3'},
            58: {'name': 'A#3'},
            59: {'name': 'B3'},
            60: {'name': 'C4'},  # Middle C
            61: {'name': 'C#4'},
            62: {'name': 'D4'},
            63: {'name': 'D#4'},
            64: {'name': 'E4'},
            65: {'name': 'F4'},
            66: {'name': 'F#4'},
            67: {'name': 'G4'},
            68: {'name': 'G#4'},
            69: {'name': 'A4'},  # A440
            70: {'name': 'A#4'},
            71: {'name': 'B4'},
            72: {'name': 'C5'},
            73: {'name': 'C#5'},
            74: {'name': 'D5'},
            75: {'name': 'D#5'},
            76: {'name': 'E5'},
            77: {'name': 'F5'},
            78: {'name': 'F#5'},
            79: {'name': 'G5'},
            80: {'name': 'G#5'},
            81: {'name': 'A5'},
            82: {'name': 'A#5'},
            83: {'name': 'B5'},
            84: {'name': 'C6'},
            85: {'name': 'C#6'},
            86: {'name': 'D6'},
            87: {'name': 'D#6'},
            88: {'name': 'E6'},
            89: {'name': 'F6'},
            90: {'name': 'F#6'},
            91: {'name': 'G6'},
            92: {'name': 'G#6'},
            93: {'name': 'A6'},
            94: {'name': 'A#6'},
            95: {'name': 'B6'},
            96: {'name': 'C7'},
            97: {'name': 'C#7'},
            98: {'name': 'D7'},
            99: {'name': 'D#7'},
            100: {'name': 'E7'},
            101: {'name': 'F7'},
            102: {'name': 'F#7'},
            103: {'name': 'G7'},
            104: {'name': 'G#7'},
            105: {'name': 'A7'},
            106: {'name': 'A#7'},
            107: {'name': 'B7'},
            108: {'name': 'C8'},
        },
    },
}

scaleMapDic = {
    'Major' : [0, 2, 4, 5, 7, 9, 11],
    'minor' : [0, 2, 3, 5, 7, 8, 10],
    'Blues' : [0, 2,3, 5, 6, 7, 10,11],
}

tonalityGridDic = {
    'test' : [(57, 'Blues', 4), (64, 'Blues', 4), (57, 'Blues', 4), (64, 'Blues', 4)],
    '12BarBlues' : [('I','Blues',4), ('IV','Blues',2), ('I','Blues',2), ('V','Blues',1), ('IV','Blues',1), ('I','Blues',1), ('V','Blues',1), ]
    }
