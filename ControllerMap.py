import vgamepad as vg

controllerMapDic = {
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
    'trackmania_keyboard' : {
   
            'preset':{
                'type':'keyboard',               

            },
            'accelerate':{'adress':'up'},
            'break':{'adress':'down'},
            'turn_left':{'adress':'left'},
            'turn_right':{'adress':'right'},

        
    },
    'vs_keyboard' : {
   
            'preset':{
                'type':'keyboard',               

            },
            'direction':{'adress':'direction'},
            'up':  {'adress':'up',
                    'main_input' : 'direction'},
            'down':{'adress':'down',
                    'main_input' : 'direction'},
            'left':{'adress':'left',
                    'main_input' : 'direction'},
            'right':{'adress':'right',
                    'main_input' : 'direction'},
            'enter':{'adress':'enter',
                #     'main_input' : 'direction'
                },

        
    },    
    'vs_keyboard_2' : {
   
            'preset':{
                'type':'keyboard',               

            },
            'direction':{'adress':'direction'},
            'up':  {'adress':'up' },
            'down':{'adress':'down'},
            'left':{'adress':'left'},
            'right':{'adress':'right'},
            'enter':{'adress':'enter'},
            'esc':{'adress':'esc'},
            'split':{'adress':'num_1'},

        
    },
    
    'vs_gamepad' : {
   
        'preset':{
        'type':'vgp_360',               

        },
        # 'direction':{'adress':'direction'},
        'left_trigger':  {'adress': 'left_t',
                        'pad':'gamepad1',
                        'input_type':'trigger',
                        'side': 'left',
                                # 'axe': 'x',
                #'main_input' : 'direction'
                },
        'right_trigger':{'adress': 'right_t',
                        'pad':'gamepad1',
                        'input_type':'trigger',
                        'side': 'right',
                        # 'axe': 'x',
                #'main_input' : 'direction'
                },
        'left_button':  {'adress': 'l_button',
                        'pad':'gamepad1',
                        'input_type':'button',
                        'button':vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER,

                },
        'right_button':{'adress': 'r_button',
                        'pad':'gamepad1',
                        'input_type':'button',
                        'button':vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER,

                },
                        
        # 'direction':{'adress':'direction'},
        'left_joystick_x':  {'adress': 'left_x',
                        'pad':'gamepad1',
                        'input_type':'joystick',
                                'side': 'left',
                                'axe': 'x',
                #'main_input' : 'direction'
                },
        'left_joystick_y':{'adress': 'left_y',
                        'pad':'gamepad1',
                        'input_type':'joystick',
                        'side': 'left',
                        'axe': 'y',
                #'main_input' : 'direction'
                },
        'right_joystick_x':{'adress': 'right_xy',
                        'pad':'gamepad1',
                        'input_type':'joystick',
                        'side': 'right',
                        'axe': 'x',
                        
                #'main_input' : 'direction'
                },
        'right_joystick_y':{'adress': 'right_xy',
                        'pad':'gamepad1',
                        'input_type':'joystick',
                        'side': 'right',
                        'axe': 'y',
                #'main_input' : 'direction'
                },
        'x':{'adress': 'x_button',
                'pad':'gamepad1',
                'input_type':'button',
                'button':vg.XUSB_BUTTON.XUSB_GAMEPAD_X,
                
        #     'main_input' : 'direction'
        },
        'y':{'adress': 'y_button',
                        'pad':'gamepad1',
                        'input_type':'button',
                        'button':vg.XUSB_BUTTON.XUSB_GAMEPAD_Y,
                },   
        'a':{'adress': 'a_button',
                        'pad':'gamepad1',
                        'input_type':'button',
                        'button':vg.XUSB_BUTTON.XUSB_GAMEPAD_A,
                },
        'b':{'adress': 'b_button',
                        'pad':'gamepad1',
                        'input_type':'button',
                        'button':vg.XUSB_BUTTON.XUSB_GAMEPAD_B,
                },
        
        },
    
    'sample' : {
        # 'z': {
        #     'type'  : 'm&k',
        #     'adress' : 'z'  ,
        #     'value_type': 'binary',
          
        # },
        # 'left_joystick_x': {
        #     'type'  : 'vgp_360',
        #     'adress' :' gp1.left_joystick' ,
        #     'value_type': '2d',
        #     'x_value_min':-32768,
        #     'x_value_max':-32767,
        #     'y_value_min':-32768,
        #     'y_value_max':-32767,
            
        # }
    }
}