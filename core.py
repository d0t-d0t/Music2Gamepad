import datetime,time
import threading
import mido
import InstrumentMap,ControllerMap,RulerMap
import  sys,keyboard
import vgamepad as vg
gamepad_dict = {}


#COMMON VARIABLES
# beat_master.bpm = 120
# tonal = 72#'C5'
verbose = False
instant_delay = 20

class BeatMaster:

    bpm : int = 60
    # tonal : int = 72
    ticks_per_beat : int = 48
    subscribers  = []
    running : bool = False
    tick_count : int = 1
    tick_interval : float = 0.0
    elapsed_time : float = 0.0
    input_on = True

    instruments =[]

    def __init__(self,bpm : int = 60, ticks_per_beat : int = 48):
        self._tonal = None
        self.thread = None
        
        #Observer lists
        self.bpm_observers = []
        self.play_observer = []
        self.tonal_observers = []

        self.bpm = bpm
        self.ticks_per_beat = ticks_per_beat
        self.tick_interval = 60.0 / float(bpm * ticks_per_beat)
        # self.tick_interval = 60.0 / float(bpm)

        print(f"tick_interval: {self.tick_interval}")
        
        
        self.tonal = 57
        self.scale = 'Major'

    def add_observer(self, observer, observer_type=['tonality']):
        for t in observer_type:
            match t:
                case 'tonality':
                    self.tonal_observers.append(observer)
                case 'bpm':
                    self.bpm_observers.append(observer)
                case 'play':
                    self.play_observer.append(observer)

    def remove_observer(self, observer, observer_type=['tonality']):
        for t in observer_type:
            match t:
                case 'tonality':
                    self.tonal_observers.remove(observer)
                case 'bpm':
                    self.bpm_observers.remove(observer)
                case 'play':
                    self.play_observer.remove(observer)

    def subscribe(self, callback, beat_num=1, beat_base=16, is_loop=False, args=()):
        tick_cible = self.ticks_per_beat * beat_num / beat_base
        self.subscribers.append({
            "callback": callback, 
            "calling_tick": int(tick_cible), 
            'is_loop': is_loop,
            'beat_num': beat_num,
            'beat_base': beat_base,
            'args': args
        })

    def update_subscribers(self):
        for subscriber in self.subscribers:
            beat_num = subscriber['beat_num']
            beat_base = subscriber['beat_base']
            tick_cible = self.ticks_per_beat * beat_num / beat_base
            subscriber['calling_tick'] = int(tick_cible)

    # def old_subscribe(self,callback, call_rule = ['next_beat',1], is_loop = False ):
    #     tick_cible = 0.0
    #     if isinstance(call_rule, list):
    #         # do something with list
    #         if call_rule[0] == 'next_beat':
    #             tick_cible = self.tick_count + call_rule[1] * self.ticks_per_beat
    #     elif isinstance(call_rule, int):
    #         # do something with int
    #         tick_cible = call_rule
    #     self.subscribers.append({"callback": callback, "calling_tick": int(tick_cible), 'is_loop': is_loop})
    
    def start(self,):
        self.running = True
        self.last_delta_time = time.time()
        if self.thread == None or not self.thread.is_alive():
            self.thread = threading.Thread(target=self._process)
            self.thread.start()
        for observer in self.play_observer:
            observer.on_play()

    def stop(self,):
        self.running = False
        for observer in self.play_observer:
            observer.on_stop()
        if self.thread.is_alive():
            self.thread.join()

    def _process(self):
        while self.running:
            current_time = time.perf_counter()
            delta = current_time - self.last_delta_time
            self.last_delta_time = current_time

            self.elapsed_time += delta
            ticks = int(self.elapsed_time / self.tick_interval)
            self.elapsed_time -= ticks * self.tick_interval

            for _ in range(ticks):
                for subscriber in self.subscribers[:]:
                    if self.tick_count % subscriber['calling_tick'] == 0:
                        subscriber['callback'](*subscriber['args'])
                        if not subscriber['is_loop']:
                            self.subscribers.remove(subscriber)
                self.tick_count += 1
            # remain = delta-1/100
            # if remain>0:
            time.sleep(0.001)
        # while self.running:
        #     delta =  time.time()-self.last_delta_time 
        #     self.last_delta_time = time.time()

        #     self.elapsed_time += delta #Why +=?, because if not enough need to keep the rest for next loop
        #     while self.elapsed_time >= self.tick_interval:
        #         for subscriber in self.subscribers:
        #             if self.tick_count % subscriber['calling_tick'] == 0:
        #                 subscriber['callback'](*subscriber['args'])
        #                 if not subscriber['is_loop']:
        #                     # remove suscriber form arra
        #                     self.subscribers.remove(subscriber)
        #         self.elapsed_time -= self.tick_interval 
        #         self.tick_count += 1
            


    def change_tonality(self, tonal):
        self.tonal = tonal

    def get_degree_scale(self, degree):
        DEGREE_DIC = {
                'I' : 0,
                'II' : 1,
                'III' : 2,
                'IV' : 3,
                'V' : 4,
                'VI' : 5,
                'VII' : 6,
        }
        # get new scale root at degree
        scale = InstrumentMap.scaleMapDic.get(beat_master.scale)
        degree_root = self.tonal + scale[DEGREE_DIC[degree]]
        return degree_root

    def get_relative_tone(self,key_name):
        #key_name is of shape rel_interval. We need to find the corresponding key in the layout
        if key_name.startswith('rel_')!=-1:
            interval_name = key_name.split('_')[1]
            octave = key_name.split('_')[2] if len(key_name.split('_'))>2 else 0
            INTERVAL_DIC = {
                '1st' : 0,
                '2nd' : 1,
                '3rd' : 2,
                '4th' : 3,
                '5th' : 4,
                '6th' : 5,
                '7th' : 6,
            }
            scale = InstrumentMap.scaleMapDic.get(beat_master.scale)
            interval_index = INTERVAL_DIC[interval_name]
            key_int = scale[interval_index]

            key_int = beat_master.tonal+key_int+(12*int(octave))
            return key_int
        else:
            print('ERROR: key_name is not relative:',key_name)

    @property
    def bpm(self):
        return self._bpm

    @bpm.setter
    def bpm(self, value):
        self._bpm = value
        self.tick_interval = 60.0 / float(value * self.ticks_per_beat)
        # self.tick_interval = 60.0 / float(value)
        self.update_subscribers()
        self._notify_bpm_observers()

    @property
    def tonal(self):
        return self._tonal

    @tonal.setter
    def tonal(self, value):
        if self._tonal != value:
            self._tonal = value
            self._notify_tonal_observers()

    def _notify_bpm_observers(self):
        for observer in self.bpm_observers:
            observer.on_bpm_change(self.bpm)

    def _notify_tonal_observers(self):
        for observer in self.tonal_observers:
            observer.on_tonal_change(self.tonal)


beat_master = BeatMaster(bpm=120)



#MUSICAL INPUTS
class Input:
    key = 'A'
    mapped = False
    mapping = None
    cValue = 0

    def __init__(self,*args,**kwargs) -> None:
        self.instrument = kwargs.get('parent',Instrument)
        pass    

class MidiInput(Input):
  
    inputType = 'note'#or control
    noteOffMessageType = 'note_off'
    noteOffValue = 0
    last_msg = None
    
    retrigger = 10
    lastCall = 0
    isOn = False

    def __init__(self,*args,**kwargs) -> None:
        self.lastCall = datetime.datetime.now()
        self.instrument = kwargs.get('parent',MidiInstrument)
        self.inputType = kwargs.get('input_type','')
        self.key = kwargs.get('key','')
        pass    

    def _treat_msg(self,msg : mido.Message):
        self.last_msg = msg

        if verbose:
            print('TREATING MESSAGE: ',msg)
        if not self.mapped:
            if verbose:
                print('INPUT NOT MAPPED: ')
            return None
        if self.inputType == 'note':
            value = msg.velocity
        else:
            value = msg.value
        
        #check if note off
        if value == self.noteOffValue and msg.type== self.noteOffMessageType:
            if verbose:
                print('NOTE OFF')
            #TODO handle note off rules
            self.cValue=0
            self.isOn = False
            self.mapping.trigger_rule(self, True)
        #else check if retrigger
        else:
            newTime = datetime.datetime.now()
            delta = newTime-self.lastCall
            delay = int(delta.total_seconds() * 1000)
            if delay < self.retrigger:
                if verbose:
                    print('RETRIGER DELAY NOT PASSED')
                return None
            else:
                lastCall = newTime
                self.isOn=True
                self.cValue=value
                self.mapping.trigger_rule(self)
        pass

    def _map():
        pass

import sounddevice as sd
from scipy.signal import butter, lfilter
import numpy as np
import aubio    
# import time as Time

class WaveInstrument():

    def __init__(self,*args,**kwargs) -> None:
        # Get a list of all available sound devices
        devices = sd.query_devices()
        self.name = kwargs.get('name')
        self.source_name = kwargs.get('source')
        self.previous_msg =  mido.Message('note_off', note=0, velocity=0)
        self.band_list =[[1,100],
                        #  [40,86], (guitar)


                        # 86]
                        ]
        # kwargs.get('band_list',[(0,11000)])
        # convert midi note to frequency
        for band in self.band_list:
            band[0] = self.note_and_distance_to_hz(band[0])[2]
            band[1] = self.note_and_distance_to_hz(band[1])[1]

        # Constants
        self.SAMPLE_RATE = 22050
        self.FRAME_SIZE = 1024 #the more bass you have to detect the more it needs to be high
        self.HOP_SIZE = self.FRAME_SIZE // 2
        self.RMS_THRESHOLD = 0.001

        # Create a new pYIN pitch detection object
        self.algorithm =kwargs.get('algorithm','yinfast')
        self.pitcher = aubio.pitch(self.algorithm , self.FRAME_SIZE, self.HOP_SIZE, self.SAMPLE_RATE)
        self.pitcher.set_unit("Hz")
        
        device_info = next(d for d in devices if d['name'] == self.source_name)
        # stream = sd.InputStream(device=device_info['index'], callback=self.callback, channels=1, samplerate=SAMPLE_RATE, blocksize=HOP_SIZE)
        # stream.start()
        self.stream = sd.InputStream(device=device_info['index'], callback=self.callback, channels=1, samplerate=self.SAMPLE_RATE, blocksize=self.HOP_SIZE)
        self.stream_condition = threading.Condition()
        self.stream_thread = threading.Thread(target=self.start_stream)

        # # Create a virtual MIDI output port
        # self.outport = mido.open_output('virtual', virtual=True)
        self.MidiInstrument = kwargs.get('midiInstrument',None)
        self.start()
        # self.inport = self.MidiInstrument.inport

    def start_stream(self):
        with self.stream_condition:
            self.stream.start()
            while self.stream.active:
                self.stream_condition.wait()

    def stop_stream(self):
        with self.stream_condition:
            self.stream.stop()
            self.stream_condition.notify_all()

    def start(self):
        self.stream_thread.start()

    # Create the callback function
    def callback(self,indata, frames, time, status):
        # try:  
            
            # add time control
            #start_time = Time.time()

            # Convert the input data to an aubio float vector
            full_indata = np.frombuffer(indata, dtype=np.float32)


            for i,band in enumerate(self.band_list):
                # print('BAND:',band)
                indata = self.bandpass_filter(full_indata, band[0], band[1], self.SAMPLE_RATE)
                # Calculate the RMS
                
                rms = np.sqrt(np.mean(np.square(indata)))
                
                if rms < self.RMS_THRESHOLD:
                    velocity = 0
                    midi = 0
                    distance = 0    
                    msg = mido.Message('note_off', note=self.previous_msg.note, velocity=0)
                else:
                    fvec = aubio.fvec(indata)

                    # Perform pitch detection
                    pitch = self.pitcher(fvec)

                    # Apply a logarithmic scale to the RMS
                    rms_log = np.log1p(rms * 1000)  # The factor 1000 can be adjusted

                    # Scale the logarithmic RMS to the range of MIDI velocity values
                    velocity = int(rms_log * (127 / np.log1p(1000)))  # The denominator should match the factor in the previous line

                    #duration = Time.time() - start_time
                    if pitch[0] > 0:
                        midi,note,distance = self.hz_to_note_and_distance(pitch[0])
                        # Print the detected pitch
                        # if verbose:
                        # 
                        if verbose:    
                            print(f"Band {i} Detected pitch {note} Hz, midi {midi}, distance {distance} at {velocity}")
                        
                        msg = mido.Message('note_on', note=midi, velocity=velocity)
                    else:
                        msg = mido.Message('note_off', note=self.previous_msg.note, velocity=0)

            
            if msg.note != self.previous_msg.note or msg.type != self.previous_msg.type:
                if msg.type == self.previous_msg.type:
                    # release previous note
                    prev_rel_msg = mido.Message('note_off', note=self.previous_msg.note, velocity=0)
                    self.MidiInstrument._read_messages(prev_rel_msg)
                self.MidiInstrument._read_messages(msg)

            self.previous_msg = msg
        # except Exception as e:
        #     print('ERROR IN Waveinstrument CALLBACK:',e)
        #     pass
    
    def stop(self):
        self.stop_stream()
        if self.stream_thread.is_alive():
            self.stream_thread.join()


    # Define the band-pass filter
    def bandpass_filter(self,data, lowcut, highcut, fs, order=5):
        nyq = 0.5 * fs
        low = lowcut / nyq
        high = highcut / nyq
        # print(low,high)
        if low < 0 or high > 1:
            raise ValueError(f"Invalid cut-off frequencies: lowcut and highcut must be between 0 and fs/2.{low} {high}")
        b, a = butter(order, [low, high], btype='band')
        if data.ndim > 1:
            return np.array([lfilter(b, a, channel) for channel in data.T]).T
        else:
            return lfilter(b, a, data)
        

    def hz_to_note_and_distance(self,frequency):
        # Convert frequency to MIDI note number
        midi_num = 12 * np.log2(frequency / 440) + 69

        # Round MIDI note number to nearest integer
        midi_num_rounded = round(midi_num)

        if midi_num_rounded < 0 or midi_num_rounded > 127:
            midi_num_rounded = 0

        # Convert MIDI note number to note name and octave
        note_octave = aubio.midi2note(int(midi_num_rounded))

        # Calculate distance
        distance = (midi_num - midi_num_rounded)

        return midi_num_rounded,note_octave, distance
    
    def note_and_distance_to_hz(self, midi_num):
        # Convert MIDI note number and distance to frequency
        frequency = 440 * 2 ** ((midi_num - 69) / 12)

        # Calculate frequencies for +0.5 and -0.5 distances
        frequency_plus = 440 * 2 ** ((midi_num + 0.5 - 69) / 12)
        frequency_minus = 440 * 2 ** ((midi_num - 0.5 - 69) / 12)

        return frequency, frequency_plus, frequency_minus

class Instrument:   
    name = ''
    input_dic = {}
    def __init__(self,*args,**kwargs) -> None:
        self.instrumentName = kwargs.get('name','unknown')  
        self._observers = []
        pass

    def get_input(self,input_name)-> Input:
        return self.input_dic.get(input_name)

    def subscribe(self, observer):
        self._observers.append(observer)

    def unsubscribe(self, observer):
        self._observers.remove(observer)

    @property
    def last_played(self):
        return self._last_played
    
    @last_played.setter
    def last_played(self, value):
        self._last_played = value
        self._notify_last_played_observers()
    
    def _notify_last_played_observers(self):
        if verbose:print('NOTIFYING OBSERVERS')
        for observer in self._observers:
            observer.on_last_played_change(self._last_played)


    def notify(self):
        for observer in self._observers:
            observer.update(self)

    def stop(self):
        self._observers.clear()

class MidiInstrument(Instrument):
    
    def __init__(self,*args,**kwargs) -> None:
        #call super
        super().__init__(*args,**kwargs)
        self.name = kwargs.get('name')
        if not kwargs.get('isWave',False):
            
            keyMap = InstrumentMap.keyMapDic.get(self.name,{})
            self.portName = kwargs.get('portName','Keystation Pro 88:Keystation Pro 88 MIDI 1 24:0')        
            self.inport = mido.open_input(self.portName,callback= self._read_messages)
        else:
            keyMap = InstrumentMap.keyMapDic.get('Keyboard',{})
            # get virtual port created in wave_instrument
            self.inport =  None
            # self.inport = mido.open_input('virtual', callback=self._read_messages, virtual=True)

        #instanciate midiInput
        preset_dic = {}
        for type in keyMap:
            for key in  keyMap[type]:
                if key=='preset':
                    preset_dic = keyMap[type][key]
                else:
                    self._add_input(type,key,keyMap[type][key],preset_dic)

        self.last_input = None
        pass    
    
    def _add_input(self,input_type,key,note_dic,preset_dic):
        for k in preset_dic:
            if type(note_dic.get(k,None))==type(None):
                note_dic[k] = preset_dic[k]
        if input_type.find('note')!=-1:
            note_dic['input_type']='note'
        note_dic['key']=key
        note_dic['parent']=self
        self.input_dic[key] = MidiInput(**note_dic) #self.input_dic[input_type][key] 
        pass
    
    def _get_MidiInput(self, msgType,msgNote) -> MidiInput:
        if msgType.find('note')!=-1:
            msgType='note'            # 46 : {
            #     'name': 'charleston'
            # },='note'
        midiInput =  self.input_dic.get(msgNote,None)# self.input_dic.get(msgType,{}).get(msgNote,None)
        return midiInput

    def _read_messages(self,msg):      
        midiInput = self._get_MidiInput(msg.type,msg.note)
        # print('HANDLING:\n',msg.type,msg.note)
        if type(midiInput)!=type(None):
            if verbose:            
                print('MIDI INPUT HANDLED:\n',msg)

            self.last_played = msg
            midiInput._treat_msg(msg)
        else : 
            if verbose:            
                print('MIDI INPUT NOT HANDLED:\n',msg)

    def stop(self):
        if self.inport:
            self.inport.close()
        super().stop()

class MidiOutput:
    def __init__(self, port_name):
        self.outport = mido.open_output(port_name)

    def send_message(self, msg):
        self.outport.send(msg)                     
 
    def stop(self):
        if self.outport:
            self.outport.close()

#GAME CONTROLLERS 
class GameControler:
    #hold a collection of GCI
    name = 'GC1'

    input_dic = {}
    
    def __init__(self,*args,**kwargs) -> None:
        self.name = kwargs.get('name')
        controlMap_dic = ControllerMap.controllerMapDic.get(self.name,{})
        # for each input
        preset_dic = {}
        for key in controlMap_dic:
            if key=='preset':
                preset_dic = controlMap_dic[key]
            else:
                result_dic = fuse_preset_dic(preset_dic,controlMap_dic[key])
                result_dic['name']=key
                self._add_input(**result_dic)

        pass

    def _add_input(self,*args,**kwargs):
        kwargs['parent'] = self
        self.input_dic[kwargs.get('adress')] = GameControlerInput(**kwargs)
        pass

    def get_gci(self,input_name):
        gci:GameControlerInput = self.input_dic.get(input_name,None)
        return gci

    def stop(self):
        for gci in self.input_dic.values():
            gci.stop()

class GameControlerInput(threading.Thread):
    #Control a single input of a game controller
    #they can be of different type keybord,gamepad,joystick...
    #they can be binary or floating
    #Input emission has to be thread based as it can have a sustain timing/ smooth release function and need to do it without blocking 
    gci_type : str
    gci_adress : str
    min : int
    max : int
    isBinary : bool

    started = False
    alive = True
    pause = False
    isOn = False
    main_input = None
    normally_off = True
    lastCheck = 0
    #exrimés en milliseconde
    current = 0
    cible = 0
    timeToRelease = 1000
    timeToPress = 0
    refreshrate = 1/60


    sem = threading.Semaphore(value=1)

    def __init__(self,*args,**kwargs) -> None:
        super().__init__()
        self.gci_type= kwargs.get('type')
        self.keep_pressed = kwargs.get('keep_pressed',False)
        self.gci_adress= kwargs.get('adress')
        
        self.parent = kwargs.get('parent')
        self.main_input = self.parent.get_gci(kwargs.get('main_input',None))  # get the main input from kwargs
        if self.gci_type == 'keyboard':
            self.min = 0
            self.max = 1
            self.isBinary = True
        elif self.gci_type == 'vgp_360':
            #get or create gamepad
            self.pad_name = kwargs.get('pad')   
            self.gamepad = gamepad_dict.get(self.pad_name)
            
            if self.gamepad == None:
                self.gamepad = vg.VX360Gamepad()
                gamepad_dict[self.pad_name] = self.gamepad

            self.input_type = kwargs.get('input_type')

            if self.input_type == 'joystick':
                self.min = -32768
                self.max = 32767
                self.isBinary = False
                if kwargs.get('side') == 'left':
                    self.definition = self.gamepad.left_joystick_float
                else:
                    self.definition = self.gamepad.right_joystick_float
                self.axe = kwargs.get('axe')
            elif self.input_type == 'trigger':
                self.side = kwargs.get('side')
                self.min = 0
                self.max = 255
                self.isBinary = False
                if self.side == 'left':
                    self.definition = self.gamepad.left_trigger_float
                else:
                    self.definition = self.gamepad.right_trigger_float
                
            elif self.input_type == 'button':
                self.definition = self.gamepad.press_button
                self.button = kwargs.get('button')
                self.isBinary = True
                
        pass

    def launch_input_watch(self,*args,**kwargs):
        self.press_input()
        while self.isOn:
            if datetime.datetime.timestamp >= self.releaseTime:
                self.isOn=False

        #calculate final input value

        #kill previous thread if there is one
        #launch new thread and add it to the trheadlist
        pass

    def press_input(self,*args,**kwargs):
        
        # if self.main_input is None or self.main_input.isOn:
        if self.gci_type == 'keyboard':
            # check if button is already pressed

            try:
                # if not keyboard.is_pressed(self.gci_adress):
                    if verbose:
                        print('PRESSING INPUT',self.gci_adress)
                    if  self.keep_pressed :
                        if not keyboard.is_pressed(self.gci_adress):
                            if verbose:
                                print('KEEP PRESSED')
                            keyboard.press(self.gci_adress)
                    else:
                        print('PRESS AND RELEASE')
                        keyboard.press_and_release(self.gci_adress) 
            except:
                #print('ERROR PRESSING KEYBOARD:',self.gci_adress)
                pass
        elif self.gci_type == 'vgp_360':
            if self.input_type == 'joystick':
                if self.axe == 'x':
                    self.definition(x_value_float = self.cible)
                elif self.axe == 'y':
                    self.definition(y_value_float = self.cible)
            elif self.input_type == 'trigger':
                self.definition(value_float = self.cible)
            elif self.input_type == 'button':
                self.definition(button = self.button)
            self.gamepad.update()
        
        
        

    def release_input(self,*args,**kwargs):
        
        if self.gci_type == 'keyboard':
            try:
                # if keyboard.is_pressed(self.gci_adress):
                    if verbose:
                        print('RELEASING INPUT',self.gci_adress)
                    keyboard.release(self.gci_adress) 
            except:
                pass
        elif self.gci_type == 'vgp_360':
            if self.input_type == 'trigger':
                self.definition(value_float = 0)

            elif self.input_type == 'joystick':
                if self.axe == 'x':
                    self.definition(x_value_float = 0)
                elif self.axe == 'y':
                    self.definition(y_value_float = 0)
            elif self.input_type == 'button':
                self.gamepad.release_button(button = self.button)
            self.gamepad.update()
        pass


    def run(self):
        self.lastCheck = datetime.datetime.now()
        while self.alive:
            self.sem.acquire()
            newcheck =datetime.datetime.now()
            delta = self.lastCheck-newcheck
            delay = int(delta.total_seconds() * 1000)
            if not self.pause: 
                release = False
                if self.main_input is None or self.main_input.isOn :  # check the main input here or self.current>0
                
                    #print('THREAD LOOPING:',self.gci_adress)
                    if self.cible != 0 :# and self.current != self.cible
                        press = False
                        if type(self.timeToPress)!=type(None):
                            # if verbose:            
                            #     print('WAITING FOR PRESS :', self.timeToPress)
                            if self.timeToPress>=0:
                                self.timeToPress +=delay
                            if self.timeToPress<=0:
                                press = True
                        if press:
                            self.current = self.cible
                            self.press_input()
                            self.isOn=True
                            # self.timeToPress=None
                            if self.timeToRelease!=None:
                                self.cible = 0
                    elif self.cible == 0  and self.isOn:#self.current:
                        
                        if type(self.timeToRelease)!=type(None):
                            if verbose:            
                                print('WAITING FOR RELEASE :', self.timeToRelease)
                            if self.timeToRelease>=0:
                                self.timeToRelease +=delay
                            if self.timeToRelease<=0:
                                release = True
                            
                        else:
                            release = True
                        
                                    
                    else:
                        #print('CURRENT = CIBLE: ',self.gci_adress,' ', self.cible)
                        pass
                    
                    # if not self.isOn and self.current > 0 and self.timeToPress<=0:
                    #     self.press_input()
                    #     self.isOn=True
                    #     # self.timeToPress=None
                    #     if self.timeToRelease!=None:
                    #         self.cible = 0
                    # else:
                    #     self.release_input()
                    #     self.isOn=False
                    #     self.timeToRelease= None
                elif self.main_input is not None and not self.main_input.isOn:
                    release = self.normally_off
                if not self.keep_pressed and release and self.isOn:
                            print('RELEASING INPUT:',self.gci_adress)
                            self.current = self.cible
                            self.release_input()
                            self.isOn=False
                            self.timeToRelease= None
             
            self.lastCheck =newcheck
            self.sem.release()
            time.sleep(self.refreshrate)

        pass
    def calculate_input_value(self,value, ruleDic):
        #     rule_dic = {
        #         'valueType'  : 'velocity',#fixe
        #         'valueMax' : 255,
        #         'sustain' : 'velocity',#fixe
        #         'threshold' : 10,
                
        #         'curve' : 'linear',
        #         'retrigger' : 10 ,
        #         'reverse' :False,
        #    }
        valueType = ruleDic.get('valueType',None)
        if valueType == 'velocity':
            #get min, max and curve
            min =  ruleDic.get('valueMin',0)
            max =  ruleDic.get('valueMax',1)

    def stop(self):
        self.alive = False
        self.release_input()
        if self.is_alive():
            self.join()

#BINDING

class Mapping:
    rulesDic = {}
    gciDic = {}
    instDic = {}
    outputList = []

    def __init__(self,*args,**kwargs) -> None:
        for gci in kwargs.get('controllerList'):
            self.gciDic [gci.name] = gci

        for inst in kwargs.get('instrumentList'):
            self.instDic [inst.name] = inst

        for outp in kwargs.get('outputList'):
            self.outputList.append(outp)


        self.kwargs = kwargs

        self.map(kwargs)
        beat_master.add_observer(self)
        pass

    def on_tonal_change(self,tonal):
        # self.rulesDic = {}
        self.map(self.kwargs,re_only=True)
        pass

    def map(self, kwargs,re_only=False):
        rulerMap_dic = RulerMap.rulerMapDic.get(kwargs.get('name'),{})
        # for each input
        preset_dic = {}
        for inst_name in rulerMap_dic:
            if re_only:
                # Create a list of keys to remove
                keys_to_remove = []
                for key_name, key_dic in self.rulesDic[inst_name].copy().items():
                    print(key_dic)
                    for rule_name, rule in key_dic.copy().items():
                        if rule.is_relative:
                            del self.rulesDic[inst_name][key_name][rule_name]
                            # keys_to_remove.append(rule_name)

                        # Remove the keys from the dictionary
                    # for rule_name in keys_to_remove:
                    #     del self.rulesDic[inst_name][key_name][rule_name]
            inst_obj : Instrument
            inst_obj = self.instDic.get(inst_name)
            if type(inst_obj)==type(None):
                print('INSTRUMENT NOT FOUND:',inst_name)
                continue
            if self.rulesDic.get(inst_name)==None:
                self.rulesDic[inst_name]={}

            for key_name in rulerMap_dic[inst_name]:
                if key_name=='preset':
                    preset_dic = rulerMap_dic[inst_name][key_name]
                else:
                    # search if key_name is a string corrseponding to a re layout
                    is_relative = False
                    if type(key_name)==str:
                        key_int = beat_master.get_relative_tone(key_name)
                        is_relative = True
                        pass
                    elif not re_only:
                        key_int = key_name
                    else:
                        # key_int = key_name
                        continue
                    key_obj = inst_obj.get_input(key_int)
                    
                    if type(key_obj)==type(None):
                        print('INSTRUMENT KEY NOT FOUND:',key_name)
                        continue
                    if self.rulesDic[inst_name].get(key_int)==None:
                        self.rulesDic[inst_name][key_int]={}
                    key_obj.mapped = True  
                    key_obj.mapping = self                  
                    for rule_name in rulerMap_dic[inst_name][key_name]:
                        result_dic = fuse_preset_dic(preset_dic,rulerMap_dic[inst_name][key_name][rule_name])

                        #GC TODO solve gci naming error
                        gc_name = result_dic.get('gci')
                        gc_object : GameControler = self.gciDic.get(gc_name)
                        if type(gc_object)==type(None):
                            print('GC NOT FOUND:',gc_name, 'in dic',result_dic)
                            continue
                        #GCI
                        gci_name = result_dic.get('gci_adress')
                        gci_object = gc_object.get_gci(gci_name)
                        if type(gci_object)==type(None):
                            print('GCI NOT FOUND:',gci_name, 'whith GC:',gc_name)
                            continue
                        result_dic['gci_object']=gci_object
                        result_dic['name']=rule_name
                        result_dic['key']=key_obj
                        result_dic['inst']=inst_obj
                        result_dic['is_relative']=is_relative
                        self.add_rule(**result_dic)

    def add_rule(self,*args,**kwargs):        
        self.rulesDic[kwargs.get('inst').name][kwargs.get('key').key][kwargs.get('name')]= Rule(*args,**kwargs)
    
    def trigger_rule(self,input:Input,off=False):
        #Get Instrument dic
        instrument_name = input.instrument.name
        instruDic = self.rulesDic.get(instrument_name,{})        
        if len(instruDic)>0:
            
            ruleDic = instruDic.get(input.key,[])   
            # If exist, for Rule in list
            for r in ruleDic :
                # check if propagate
                
                #trigger input 
                rule = ruleDic.get(r)
                
                if rule.propagate:
                    # get last mido message of input
                
                    msg = input.last_msg
                    if rule.overwrite != None:
                        if type(rule.overwrite)!=int:
                            over_key = beat_master.get_relative_tone(rule.overwrite)
                        else:
                            over_key = rule.overwrite
                        msg.note = over_key 

                    for outp in self.outputList:
                        outp.send_message(msg)


                if verbose:            
                    print('TRIGGERING RULES: ',r)
                # if rule.cible == 0:
                #     rule.send_gc_input(0)
                # else: 
                if not off and rule.threshold<=input.cValue:
                    if verbose:            
                        print('TRIGGERING RULES: ',r)
                    if beat_master.input_on:
                        rule.send_gc_input(input.cValue)
                elif off:
                    
                    if verbose:            
                        print('RELEASING RULES: ',r)
                    if beat_master.input_on:
                        rule.send_gc_input(0,True)
        else:
            print('ERROR, TRIGGER BUT NO RULE FOUND: ',instrument_name)    

        pass

    def stop(self):
        for gci in self.gciDic.values():
            gci.stop()
        for inst in self.instDic.values():
            inst.stop()
        for outp in self.outputList:
            outp.stop()
class Rule:    
    name =''
    gci : GameControlerInput
    gci_adress : str
    rule_dic = {
                    "cible": 1,
                    "time_to_cible":0,
                    "release_mode":'gain',
                    'max_beat':4
    }
    cible = 0
    press_mode = 'instant'
    press_time = 0
    release_mode : str
    release_time : float
    release_max_beat :float
    
    def __init__(self,*args,**kwargs) -> None:
        self.name = kwargs.get('name')
        self.gci = kwargs.get('gci_object')
        self.gci_adress = kwargs.get('gci_adress')
        self.is_relative = kwargs.get('is_relative',False)
        self.cible = kwargs.get('cible')
        self.threshold = kwargs.get('threshold',0)
        self.press_mode = self.rule_dic.get('press_mode','instant')
        if self.press_mode == 'instant':
            self.press_time = 0
        #calculate release
        self.release_mode = kwargs.get('release_mode')            
        self.release_max_beat = kwargs.get('release_max_beat',1)
        if self.release_mode == 'bpm':
            if verbose:            
                print('this one is bpm:',self.gci_adress)
            self.release_time = (60/beat_master.bpm)*self.release_max_beat*1000
        elif self.release_mode == 'instant':
            self.release_time = instant_delay

        self.propagate = kwargs.get('propagate',False)
        self.overwrite = kwargs.get('overwrite',None)
        pass
    
    def send_gc_input(self,instrument_input_value, off = False):

        if type(self.gci)!=type(None):
            # launch thread
            if not self.gci.started:
                if verbose:            
                    print('LAUNCHING GCI INPUT TRHEAD:',self.gci_adress)
                self.gci.started = True
                self.gci.start()
                print('THREAD STARTED:',self.gci_adress)
            
            #calculate press
            if not off:
                if self.release_mode == 'gain':
                    self.release_time = self.release_max_beat*1000*(instrument_input_value/128)#60/beat_master.bpm)*

                self.gci.sem.acquire()
                try:
                    print('sem acquired:',self.gci_adress)
                    
                    if type(self.cible) in [int,float]:
                        if self.gci.cible != self.cible:
                            self.gci.cible = self.cible                    
                    elif type(self.cible) == dict:
                        value = self.cible.get('value',0)
                        if value == 'gain':
                            value =  instrument_input_value/128
                        sign = self.cible.get('sign',1)
                        self.gci.cible = value*sign


                    self.gci.timeToPress = self.press_time
                    if self.gci.cible != 0:
                        if self.release_mode not in ['hold','note_off']:
                            
                            self.gci.timeToRelease = self.release_time
                        else:
                            self.gci.keep_pressed = True
                            self.gci.timeToRelease = None
                    else:
                        self.gci.timeToRelease = 0
                except Exception as e:
                    print('ERROR:',self.gci_adress, ' ',e)
                
                self.gci.sem.release()
                print('sem released:',self.gci_adress)
            else:
                if verbose:
                    print('RELEASE MODE:',self.release_mode)
                if self.release_mode == 'note_off':
                    if verbose:
                        print('NOTE OFF:',self.gci_adress)
                    self.gci.sem.acquire()
                    self.gci.cible = 0
                    self.gci.current = self.gci.cible
                    self.gci.release_input()
                    self.gci.isOn=False
                    self.gci.timeToRelease= None

                    self.gci.sem.release()
                pass
        else:
            print('WARNING : input ',self.input, ' Not found in ',self.game_Controler)

        pass

# COMMON DEF
        
def fuse_preset_dic(preset_dic,occurence_dic):
    for k in preset_dic:
        if type(occurence_dic.get(k,None))==type(None):
                occurence_dic[k] = preset_dic[k]
    return occurence_dic

gC_Dic = {}

if __name__ == "__main__":
    io=mido.get_ioport_names()
    midi_inputs = mido.get_input_names()#USB DM10 MIDI Interface
    # inport = mido.open_input(midi_inputs[0])
    # inport = mido.open_input('USB DM10 MIDI Interface:USB DM10 MIDI Interface MIDI 1 24:0')
    #OPEN INSTRUMENT PORT
    instrumentList=[]
    instrumentList.append( MidiInstrument(portName=midi_inputs[0],#'USB DM10 MIDI Interface:USB DM10 MIDI Interface MIDI 1 24:0',
                          name = 'gamepad')
                          )
    
    #CREATE CONTROLLER
    controllerList=[]
    controllerList.append(
            GameControler(
                          name = 'vs_keyboard'
                          )
    )
    

    #LINK CONTROLLER TO INSTRUMENT WITH RULES
    mapper = Mapping( name = 'DM10_to_VS',
                     instrumentList = instrumentList,
                     controllerList = controllerList )
    
    while True:
        pass

    
    # # inport = mido.open_input('Keystation Pro 88:Keystation Pro 88 MIDI 1 24:0')

    # for msg in inport:
    #         print(msg)