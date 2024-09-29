rulerMapDic = {
    
    'layout':{
        'instrument':{
            'rule_1':{
                        'preset':{
                                'name' : 'A#2',
                                'start_signal': 'note_on',
                                'release_signal': 'note_on',
                                'treshold' : 5,
                                'retrigger' : 10,
                                'curve' :  'linear',#log2
            
                            
                        }
                    },
        }
        
    },
    'DM10_to_trackmania_keyboard':{
        'DM10':{
            'preset':{
                'gci' : 'trackmania_keyboard'
            },
            46:{
                'left_on':{
                    "gci_adress":'left',
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'gain'},
                'right_off':{
                    "gci_adress":'right',
                    "cible": 0,
                    "time_to_cible":0,
                    "release_mode": None},
            },
            38:{
                'right_on':{
                    "gci_adress":'right',
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'gain'},
                'left_off':{
                    "gci_adress":'left',
                    "cible": 0,
                    "time_to_cible":0,
                    "release_mode": None},
            },
            36:{
                'accelerate_on':{
                    "gci_adress":'up',
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'bpm'},
            },
            49:{
                'break_on':{
                    "gci_adress":'down',
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'gain'},
            },
            34:{
                'break_off':{
                    "gci_adress":'down',
                    "cible": 0,
                    "time_to_cible":0,
                    "release_mode":None},
            },

        }
    },
    'DM10_to_VS':{
        'DM10':{
            'preset':{
                'gci' : 'vs_keyboard'
            },
            51:{
                'validate':{
                    "gci_adress":'enter',#to direction for kick need
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'bpm'},
            },
            38:{
                'direction_on':{
                    "gci_adress":'direction',#to direction for kick need
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'gain'},
            },
            47:{
                'left_on':{
                    'main_input':'direction_on',
                    "gci_adress":'left',
                    "threshold": 64,
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'hold'},
                'right_off':{
                    "gci_adress":'right',
                    "cible": 0,
                    "time_to_cible":0,
                    "release_mode": None},
            },
            46:{
                'right_on':{
                    'main_input':'direction_on',
                    "gci_adress":'right',
                    "threshold": 64,
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'hold'},
                'left_off':{
                    "gci_adress":'left',
                    "cible": 0,
                    "time_to_cible":0,
                    "release_mode": None},
            },
            
            36:{
                'down_on':{
                    'main_input':'direction_on',
                    "gci_adress":'down',
                    "threshold": 64,
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'hold'},
                'up_off':{
                    "gci_adress":'up',
                    "cible": 0,
                    "time_to_cible":0,
                    "release_mode": None},
            },
            49:{
                'up_on':{
                    'main_input':'direction_on',
                    "gci_adress":'up',
                    "threshold": 32,
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'hold'},
                'down_off':{
                    "gci_adress":'down',
                    "cible": 0,
                    "time_to_cible":0,
                    "release_mode": None},
            },

        }
    },
    'DM10_to_VS2':{
        'DM10':{
            'preset':{
                'gci' : 'vs_keyboard_2'
            },
            36:{
                'direction_on':{
                    "gci_adress":'enter',#to direction for kick need
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'bpm'},
            },
            47:{
                'left_on':{
                    'main_input':'direction_on',
                    "gci_adress":'left',
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'gain'},
                'right_off':{
                    "gci_adress":'right',
                    "cible": 0,
                    "time_to_cible":0,
                    "release_mode": None},
            },
            46:{
                'right_on':{
                    'main_input':'direction_on',
                    "gci_adress":'right',
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'gain'},
                'left_off':{
                    "gci_adress":'left',
                    "cible": 0,
                    "time_to_cible":0,
                    "release_mode": None},
            },
            
            38:{
                'down_on':{
                    'main_input':'direction_on',
                    "gci_adress":'down',
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'gain'},
                'up_off':{
                    "gci_adress":'up',
                    "cible": 0,
                    "time_to_cible":0,
                    "release_mode": None},
            },
            49:{
                'up_on':{
                    'main_input':'direction_on',
                    "gci_adress":'up',
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'gain'},
                'down_off':{
                    "gci_adress":'down',
                    "cible": 0,
                    "time_to_cible":0,
                    "release_mode": None},
            },

        }
    },
    'DM10_to_VS_x360':{
        'DM10':{
            'preset':{
                'gci' : 'vs_gamepad'
            },
            51:{
                'validate':{
                    "gci_adress":'x_button',#to direction for kick need
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'bpm'},
            },
            47:{
                'left_on':{
                    
                    "gci_adress":'left_x',
                    "cible": {'sign':-1,'value':'gain'},
                    "time_to_cible":0,
                    "release_mode":'hold'},

            },
            46:{
                'right_on':{
                    
                    "gci_adress":'left_x',
                    "cible": {'sign':1,'value':'gain'},
                    "time_to_cible":0,
                    "release_mode":'hold'},

            },
            
            38:{
                'down_on':{
                    
                    "gci_adress":'left_y',
                    "cible": {'sign':-1,'value':'gain'},
                    "time_to_cible":0,
                    "release_mode":'hold'},

            },
            49:{
                'up_on':{
                    
                    "gci_adress":'left_y',
                    "cible": {'sign':1,'value':'gain'},
                    "time_to_cible":0,
                    "release_mode":'hold'},

            },

        },
    },
    'DM10_to_x360':{
        'DM10':{
            'preset':{
                'gci' : 'vs_gamepad',                
                #'propagate': True,
            },
            51:{
                'X':{
                    "gci_adress":'x_button',#to direction for kick need
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'gain'},
            },
            60:{
                'Y':{
                    "gci_adress":'y_button',#to direction for kick need
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'gain'},
            },
            63:{
                'A':{
                    "gci_adress":'a_button',#to direction for kick need
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'gain'},
            },
            45:{
                'B':{
                    "gci_adress":'b_button',#to direction for kick need
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'gain'},
            },
            43:{
                'left_trigger':{
                    "gci_adress":'left_t',#to direction for kick need
                    "cible": {'sign':1,'value':'gain'},
                    "time_to_cible":0,
                    "release_mode":'bpm'},
            },
            36:{
                'right_trigger':{
                    "gci_adress":'right_t',#to direction for kick need
                    "cible": {'sign':1,'value':'gain'},
                    "time_to_cible":0,
                    "release_mode":'bpm'},
            },
            47:{
                'left_on':{
                    
                    "gci_adress":'left_x',
                    "cible": {'sign':-1,'value':'gain'},
                    "time_to_cible":0,
                    "release_mode":'gain',
                    #'overwrite': 'rel_1st_0',
                    },

            },
            46:{
                'right_on':{
                    
                    "gci_adress":'left_x',
                    "cible": {'sign':1,'value':'gain'},
                    "time_to_cible":0,
                    "release_mode":'gain',
                    #'overwrite': 'rel_5th_0',
                    },

            },
            
            38:{
                'down_on':{
                    
                    "gci_adress":'left_y',
                    "cible": {'sign':-1,'value':'gain'},
                    "time_to_cible":0,
                    "release_mode":'gain',
                    #'overwrite': 'rel_3rd_0',
                    },

            },
            49:{
                'up_on':{
                    
                    "gci_adress":'left_y',
                    "cible": {'sign':1,'value':'gain'},
                    "time_to_cible":0,
                    "release_mode":'gain',
                    #'overwrite': 'rel_7th_0',
                    },

            },

        },
    },
    'DM10_to_x360_DeadCells':{
        'DM10':{
            'preset':{
                'gci' : 'vs_gamepad'
            },
            46:{
                'X':{
                    "gci_adress":'x_button',#to direction for kick need
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'instant'},
            },
            49:{
                'Y':{
                    "gci_adress":'y_button',#to direction for kick need
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'instant'},
            },
            47:{
                'A':{
                    "gci_adress":'a_button',#to direction for kick need
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'instant'},
            },
            36:{
                'B':{
                    "gci_adress":'b_button',#to direction for kick need
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'instant'},
                # 'up_on':{
                    
                #     "gci_adress":'left_y',
                #     "cible": {'sign':1,'value':'gain'},
                #     "time_to_cible":0,
                #     "release_mode":'gain'},
            },
            26:{
                'LB':{
                    "gci_adress":'l_button',#to direction for kick need
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'instant'},
            },
            34:{
                'RB':{
                    "gci_adress":'r_button',#to direction for kick need
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'instant'},
            },
            43:{
                'left_trigger':{
                    "gci_adress":'left_t',#to direction for kick need
                    "cible": {'sign':1,'value':'gain'},
                    "time_to_cible":0,
                    "release_mode":'bpm'},
            },
            45:{
                'right_trigger':{
                    "gci_adress":'right_t',#to direction for kick need
                    "cible": {'sign':1,'value':'gain'},
                    "time_to_cible":0,
                    "release_mode":'bpm'},
            },
            63:{
                'left_on':{
                    
                    "gci_adress":'left_x',
                    "cible": {'sign':-1,'value':'gain'},
                    "time_to_cible":0,
                    "release_mode":'gain'},

            },
            38:{
                'right_on':{
                    
                    "gci_adress":'left_x',
                    "cible": {'sign':1,'value':'gain'},
                    "time_to_cible":0,
                    "release_mode":'gain'},

            },
            
            60:{
                'down_on':{
                    
                    "gci_adress":'left_y',
                    "cible": {'sign':-1,'value':'gain'},
                    "time_to_cible":0,
                    "release_mode":'gain'},

            },
            51:{
                'up_on':{
                    
                    "gci_adress":'left_y',
                    "cible": {'sign':1,'value':'gain'},
                    "time_to_cible":0,
                    "release_mode":'gain'},

            },

        },
    },
    'Keyboard_to_x360_DeadCells':{
        'Keyboard':{
            'preset':{
                'gci' : 'vs_gamepad'
            },
            'rel_3rd_-2':{
                'X':{
                    "gci_adress":'x_button',#to direction for kick need
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'instant'},
            },
            'rel_5th_-2':{
                'Y':{
                    "gci_adress":'y_button',#to direction for kick need
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'instant'},
            },
            'rel_1st_-2':{
                'A':{
                    "gci_adress":'a_button',#to direction for kick need
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'instant'},
            },
            'rel_7th_-3':{
                'B':{
                    "gci_adress":'b_button',#to direction for kick need
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'instant'},
                # 'up_on':{
                    
                #     "gci_adress":'left_y',
                #     "cible": {'sign':1,'value':'gain'},
                #     "time_to_cible":0,
                #     "release_mode":'gain'},
            },
            26:{
                'LB':{
                    "gci_adress":'l_button',#to direction for kick need
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'instant'},
            },
            34:{
                'RB':{
                    "gci_adress":'r_button',#to direction for kick need
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'instant'},
            },
            43:{
                'left_trigger':{
                    "gci_adress":'left_t',#to direction for kick need
                    "cible": {'sign':1,'value':'gain'},
                    "time_to_cible":0,
                    "release_mode":'bpm'},
            },
            45:{
                'right_trigger':{
                    "gci_adress":'right_t',#to direction for kick need
                    "cible": {'sign':1,'value':'gain'},
                    "time_to_cible":0,
                    "release_mode":'bpm'},
            },
            'rel_1st_0':{
                'left_on':{
                    
                    "gci_adress":'left_x',
                    "cible": {'sign':-1,'value':'gain'},
                    "time_to_cible":0,
                    "release_mode":'hold'},

            },
            'rel_5th_0':{
                'right_on':{
                    
                    "gci_adress":'left_x',
                    "cible": {'sign':1,'value':'gain'},
                    "time_to_cible":0,
                    "release_mode":'hold'},

            },
            
            'rel_7th_-1':{
                'down_on':{
                    
                    "gci_adress":'left_y',
                    "cible": {'sign':-1,'value':'gain'},
                    "time_to_cible":0,
                    "release_mode":'hold'},

            },
            'rel_3rd_0':{
                'up_on':{
                    
                    "gci_adress":'left_y',
                    "cible": {'sign':1,'value':'gain'},
                    "time_to_cible":0,
                    "release_mode":'hold'},

            },

        },
    },
    'DM10_to_x360_hades':{
        'DM10':{
            'preset':{
                'gci' : 'vs_gamepad',
                'propagate': True,
            },
            60:{
                'X':{
                    "gci_adress":'x_button',#to direction for kick need
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'bpm',
                    'overwrite': 'rel_7th_0',
                    },
            },
            36:{
                'Y':{
                    "gci_adress":'y_button',#to direction for kick need
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'bpm'},
            },
            45:{
                'A':{
                    "gci_adress":'a_button',#to direction for kick need
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'bpm'},
            },
            63:{
                'A':{
                    "gci_adress":'a_button',#to direction for kick need
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'bpm'},
            },
            51:{
                'B':{
                    "gci_adress":'b_button',#to direction for kick need
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'bpm'},
                # 'up_on':{
                    
                #     "gci_adress":'left_y',
                #     "cible": {'sign':1,'value':'gain'},
                #     "time_to_cible":0,
                #     "release_mode":'gain'},
            },
            26:{
                'LB':{
                    "gci_adress":'l_button',#to direction for kick need
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'instant'},
            },
            34:{
                'RB':{
                    "gci_adress":'r_button',#to direction for kick need
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'instant'},
                'right_on':{                    
                    "gci_adress":'left_x',
                    "cible": {'sign':1,'value':0},
                    "time_to_cible":0,
                    "release_mode":'instant'},
                'down_on':{                    
                    "gci_adress":'left_y',
                    "cible": {'sign':-1,'value':0},
                    "time_to_cible":0,
                    "release_mode":'instant'},
            },
            102:{
                'left_trigger':{
                    "gci_adress":'left_t',#to direction for kick need
                    "cible": {'sign':1,'value':'gain'},
                    "time_to_cible":0,
                    "release_mode":'bpm'},
            },
            103:{
                'right_trigger':{
                    "gci_adress":'right_t',#to direction for kick need
                    "cible": {'sign':1,'value':'gain'},
                    "time_to_cible":0,
                    "release_mode":'bpm'},
            },
            47:{
                'left_on':{
                    
                    "gci_adress":'left_x',
                    "cible": {'sign':-1,'value':'gain'},
                    "time_to_cible":0,
                    "release_mode":'gain',
                    'overwrite': 'rel_5th_0',
                    },

            },
            46:{
                'right_on':{
                    
                    "gci_adress":'left_x',
                    "cible": {'sign':1,'value':'gain'},
                    "time_to_cible":0,
                    "release_mode":'gain',
                    'overwrite': 'rel_1st_0',},

            },
            
            38:{
                'down_on':{
                    
                    "gci_adress":'left_y',
                    "cible": {'sign':-1,'value':'gain'},
                    "time_to_cible":0,
                    "release_mode":'gain',
                    'overwrite': 'rel_3rd_0',},

            },
            49:{
                'up_on':{
                    
                    "gci_adress":'left_y',
                    "cible": {'sign':1,'value':'gain'},
                    "time_to_cible":0,
                    "release_mode":'gain',
                    'overwrite': 'rel_7th_0',
                    },

            },

        },
    },
        'DM10_to_x360_elemental':{
        'DM10':{
            'preset':{
                'gci' : 'vs_gamepad'
            },
            60:{
                'X':{
                    "gci_adress":'x_button',#to direction for kick need
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'bpm'},
            },
            36:{
                'Y':{
                    "gci_adress":'y_button',#to direction for kick need
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'bpm'},
            },
            45:{
                'A':{
                    "gci_adress":'a_button',#to direction for kick need
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'bpm'},
            },
            63:{
                'A':{
                    "gci_adress":'a_button',#to direction for kick need
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'bpm'},
            },
            51:{
                'B':{
                    "gci_adress":'b_button',#to direction for kick need
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'bpm'},
                # 'up_on':{
                    
                #     "gci_adress":'left_y',
                #     "cible": {'sign':1,'value':'gain'},
                #     "time_to_cible":0,
                #     "release_mode":'gain'},
            },
            26:{
                'LB':{
                    "gci_adress":'l_button',#to direction for kick need
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'instant'},
            },
            34:{
                'RB':{
                    "gci_adress":'r_button',#to direction for kick need
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'instant'},
                'right_on':{                    
                    "gci_adress":'left_x',
                    "cible": {'sign':1,'value':0},
                    "time_to_cible":0,
                    "release_mode":'instant'},
                'down_on':{                    
                    "gci_adress":'left_y',
                    "cible": {'sign':-1,'value':0},
                    "time_to_cible":0,
                    "release_mode":'instant'},
            },
            102:{
                'left_trigger':{
                    "gci_adress":'left_t',#to direction for kick need
                    "cible": {'sign':1,'value':'gain'},
                    "time_to_cible":0,
                    "release_mode":'bpm'},
            },
            103:{
                'right_trigger':{
                    "gci_adress":'right_t',#to direction for kick need
                    "cible": {'sign':1,'value':'gain'},
                    "time_to_cible":0,
                    "release_mode":'bpm'},
            },
            47:{
                'left_on':{
                    
                    "gci_adress":'left_x',
                    "cible": {'sign':-1,'value':'gain'},
                    "time_to_cible":0,
                    "release_mode":'instant'},

            },
            46:{
                'right_on':{
                    
                    "gci_adress":'left_x',
                    "cible": {'sign':1,'value':'gain'},
                    "time_to_cible":0,
                    "release_mode":'instant'},

            },
            
            38:{
                'down_on':{
                    
                    "gci_adress":'left_y',
                    "cible": {'sign':-1,'value':'gain'},
                    "time_to_cible":0,
                    "release_mode":'instant'},

            },
            49:{
                'up_on':{
                    
                    "gci_adress":'left_y',
                    "cible": {'sign':1,'value':'gain'},
                    "time_to_cible":0,
                    "release_mode":'instant'},

            },

        },
    },
    'DM10_to_elemental_keyboard':{
        'DM10':{
            'preset':{
                'gci' : 'vs_keyboard_2',
                'propagate': True,
            },
            # 36:{
            #     'direction_on':{
            #         "gci_adress":'enter',#to direction for kick need
            #         "cible": 1,
            #         "time_to_cible":0,
            #         "release_mode":'bpm'},
            # },
            47:{
                'left_on':{
                    # 'main_input':'direction_on',
                    "gci_adress":'left',
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'instant'},
                # 'right_off':{
                #     "gci_adress":'right',
                #     "cible": 0,
                #     "time_to_cible":0,
                #     "release_mode": None},
            },
            46:{
                'right_on':{
                    # 'main_input':'direction_on',
                    "gci_adress":'right',
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'instant'},
                # 'left_off':{
                #     "gci_adress":'left',
                #     "cible": 0,
                #     "time_to_cible":0,
                #     "release_mode": None},
            },
            
            38:{
                'down_on':{
                    # 'main_input':'direction_on',
                    "gci_adress":'down',
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'instant'},
                # 'up_off':{
                #     "gci_adress":'up',
                #     "cible": 0,
                #     "time_to_cible":0,
                #     "release_mode": None},
            },
            49:{
                'up_on':{
                    # 'main_input':'direction_on',
                    "gci_adress":'up',
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'instant'},
                # 'down_off':{
                #     "gci_adress":'down',
                #     "cible": 0,
                #     "time_to_cible":0,
                #     "release_mode": None},
            },
            51:{
                'validate':{
                    # 'main_input':'direction_on',
                    "gci_adress":'enter',
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'instant'},
                # 'down_off':{
                #     "gci_adress":'down',
                #     "cible": 0,
                #     "time_to_cible":0,
                #     "release_mode": None},
            },
            63:{
                'escape':{
                    # 'main_input':'direction_on',
                    "gci_adress":'esc',
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'instant'},
                # 'down_off':{
                #     "gci_adress":'down',
                #     "cible": 0,
                #     "time_to_cible":0,
                #     "release_mode": None},
            },
            60:{
                'split':{
                    # 'main_input':'direction_on',
                    "gci_adress":'num_1',
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'instant'},
                # 'down_off':{
                #     "gci_adress":'down',
                #     "cible": 0,
                #     "time_to_cible":0,
                #     "release_mode": None},
            },



        }
    },
    'DM10_to_e4l_keyboard_melo':{
        'DM10':{
            'preset':{
                'gci' : 'vs_keyboard_2',
                'propagate': True,
            },
            # 36:{
            #     'direction_on':{
            #         "gci_adress":'enter',#to direction for kick need
            #         "cible": 1,
            #         "time_to_cible":0,
            #         "release_mode":'bpm'},
            # },
            47:{
                'left_on':{
                    # 'main_input':'direction_on',
                    "gci_adress":'left',
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'instant',
                    'overwrite': 'rel_1st_0',
                    },

            },
            46:{
                'right_on':{
                    # 'main_input':'direction_on',
                    "gci_adress":'right',
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'instant',
                    'overwrite': 'rel_5th_0',
                    },

            },
            
            38:{
                'down_on':{
                    # 'main_input':'direction_on',
                    "gci_adress":'down',
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'instant',
                    'overwrite': 'rel_7th_0',
                    },

            },
            49:{
                'up_on':{
                    # 'main_input':'direction_on',
                    "gci_adress":'up',
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'instant',
                    'overwrite': 'rel_3rd_0',
                    },

            },
            51:{
                'validate':{
                    # 'main_input':'direction_on',
                    "gci_adress":'enter',
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'instant',
                    'overwrite': 'rel_1st_2',
                    },
                    



            },
            63:{
                'escape':{
                    # 'main_input':'direction_on',
                    "gci_adress":'esc',
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'instant',
                    'overwrite': 'rel_7th_1',
                    },

            },
            60:{
                'split':{
                    # 'main_input':'direction_on',
                    "gci_adress":'num_1',
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'instant',
                    'overwrite': 'rel_3rd_1',
                    },

            },
            36:{
                'split':{
                    # 'main_input':'direction_on',
                    "gci_adress":'num_1',
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'instant',
                    'overwrite': 'rel_1st_1',
                    },

            },
            
            45:{
                'split':{
                    # 'main_input':'direction_on',
                    "gci_adress":'num_1',
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'instant',
                    'overwrite': 'rel_6th_0',
                    },
            },
            
            43:{
                'split':{
                    # 'main_input':'direction_on',
                    "gci_adress":'num_1',
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'instant',
                    'overwrite': 'rel_7th_0',
                    },

            },



        }
    },
    'Keyboard_to_Keyboard':{
        'Keyboard':{
            'preset':{
                'gci' : 'vs_keyboard_2'
            },
            'rel_1st_-1':{
                'left_on':{
                    # 'main_input':'direction_on',
                    "gci_adress":'up',
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'note_off',
                    'overwrite': 'rel_1st_0',
                    },

            },
            'rel_2nd_-1':{
                'left_on':{
                    # 'main_input':'direction_on',
                    "gci_adress":'up',
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'note_off',
                    'overwrite': 'rel_1st_0',
                    },
                    'up_on':{
                    # 'main_input':'direction_on',
                    "gci_adress":'right',
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'note_off',
                    'overwrite': 'rel_3rd_0',
                    }

            }, 
            'rel_3rd_-1':{
                'up_on':{
                    # 'main_input':'direction_on',
                    "gci_adress":'right',
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'note_off',
                    'overwrite': 'rel_3rd_0',
                    },

            }, 
            'rel_4th_-1':{
                'up_on':{
                    # 'main_input':'direction_on',
                    "gci_adress":'right',
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'note_off',
                    'overwrite': 'rel_3rd_0',
                    },
                    'right_on':{
                    # 'main_input':'direction_on',
                    "gci_adress":'down',
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'note_off',
                    'overwrite': 'rel_5th_0',
                    },


            },

            'rel_5th_-1':{
                'right_on':{
                    # 'main_input':'direction_on',
                    "gci_adress":'down',
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'note_off',
                    'overwrite': 'rel_5th_0',
                    },

            },
            

            'rel_6th_-1':{
                'right_on':{
                    # 'main_input':'direction_on',
                    "gci_adress":'down',
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'note_off',
                    'overwrite': 'rel_5th_0',
                    },
                'down_on':{
                    # 'main_input':'direction_on',
                    "gci_adress":'left',
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'note_off',
                    'overwrite': 'rel_7th_0',
                    },


            },
            
            'rel_7th_-1':{
                'down_on':{
                    # 'main_input':'direction_on',
                    "gci_adress":'left',
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'note_off',
                    'overwrite': 'rel_7th_0',
                    },

            },
            'rel_1st_-2':{
                'left_on':{
                    # 'main_input':'direction_on',
                    "gci_adress":'up',
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'note_off',
                    'overwrite': 'rel_1st_0',
                    },

            },
            'rel_2nd_-2':{
                'left_on':{
                    # 'main_input':'direction_on',
                    "gci_adress":'up',
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'note_off',
                    'overwrite': 'rel_1st_0',
                    },
                    'up_on':{
                    # 'main_input':'direction_on',
                    "gci_adress":'right',
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'note_off',
                    'overwrite': 'rel_3rd_0',
                    }

            }, 
            'rel_3rd_-2':{
                'up_on':{
                    # 'main_input':'direction_on',
                    "gci_adress":'right',
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'note_off',
                    'overwrite': 'rel_3rd_0',
                    },

            }, 
            'rel_4th_-2':{
                'up_on':{
                    # 'main_input':'direction_on',
                    "gci_adress":'right',
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'note_off',
                    'overwrite': 'rel_3rd_0',
                    },
                    'right_on':{
                    # 'main_input':'direction_on',
                    "gci_adress":'down',
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'note_off',
                    'overwrite': 'rel_5th_0',
                    },


            },

            'rel_5th_-2':{
                'right_on':{
                    # 'main_input':'direction_on',
                    "gci_adress":'down',
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'note_off',
                    'overwrite': 'rel_5th_0',
                    },

            },
            

            'rel_6th_-2':{
                'right_on':{
                    # 'main_input':'direction_on',
                    "gci_adress":'down',
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'note_off',
                    'overwrite': 'rel_5th_0',
                    },
                'down_on':{
                    # 'main_input':'direction_on',
                    "gci_adress":'left',
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'note_off',
                    'overwrite': 'rel_7th_0',
                    },


            },
            
            'rel_7th_-2':{
                'down_on':{
                    # 'main_input':'direction_on',
                    "gci_adress":'left',
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'note_off',
                    'overwrite': 'rel_7th_0',
                    },

            },
            # 'rel_1st_1':{
            #     'validate':{
            #         # 'main_input':'direction_on',
            #         "gci_adress":'enter',
            #         "cible": 1,
            #         "time_to_cible":0,
            #         "release_mode":'note_off',
            #         'overwrite': 'rel_1st_2',
            #         },
                    



            # },
            # 'rel_7th_-1':{
            #     'escape':{
            #         # 'main_input':'direction_on',
            #         "gci_adress":'esc',
            #         "cible": 1,
            #         "time_to_cible":0,
            #         "release_mode":'note_off',
            #         'overwrite': 'rel_7th_1',
            #         },

            # },
            # 60:{
            #     'split':{
            #         # 'main_input':'direction_on',
            #         "gci_adress":'num_1',
            #         "cible": 1,
            #         "time_to_cible":0,
            #         "release_mode":'instant',
            #         'overwrite': 'rel_3rd_1',
            #         },

            # },
            # 36:{
            #     'split':{
            #         # 'main_input':'direction_on',
            #         "gci_adress":'num_1',
            #         "cible": 1,
            #         "time_to_cible":0,
            #         "release_mode":'instant',
            #         'overwrite': 'rel_1st_1',
            #         },

            # },
            
            # 45:{
            #     'split':{
            #         # 'main_input':'direction_on',
            #         "gci_adress":'num_1',
            #         "cible": 1,
            #         "time_to_cible":0,
            #         "release_mode":'instant',
            #         'overwrite': 'rel_6th_0',
            #         },
            # },
            
            # 43:{
            #     'split':{
            #         # 'main_input':'direction_on',
            #         "gci_adress":'num_1',
            #         "cible": 1,
            #         "time_to_cible":0,
            #         "release_mode":'instant',
            #         'overwrite': 'rel_7th_0',
            #         },

            # },


        },
    },
    


    


}