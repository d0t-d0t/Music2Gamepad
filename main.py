import time
import tkinter as tk
from tkinter import ttk
from core import MidiInstrument, GameControler, Mapping, beat_master, MidiOutput, WaveInstrument,verbose

from ableton_link import AbletonLink

import InstrumentMap, ControllerMap, RulerMap,mido
import sounddevice as sd

import sys
import traceback

def handle_exception(exc_type, exc_value, exc_traceback):
    # Print exception information
    print("Exception type:", exc_type)
    print("Exception value:", exc_value)
    print("Exception traceback:", "".join(traceback.format_tb(exc_traceback)))

# Set the function handle_exception as the global exception handler
sys.excepthook = handle_exception

tonality_dict = InstrumentMap.keyMapDic.get('Keyboard',{}).get('note',{})
tonality_grid_dict = InstrumentMap.tonalityGridDic


class MidiMsgLabel(tk.Label):
    def __init__(self, master=None,inst=None, **kwargs):
        super().__init__(master, **kwargs)
        inst.subscribe(self)

    def on_last_played_change(self, msg):
        if verbose:
            print('new midi msg')
        self.config(text=f"Last Midi midi: {msg.note}, velocity: {msg.velocity}, note:{tonality_dict.get(msg.note,{}).get('name')}")
    
    def stop(self):
        self.pack_forget()

class BeatMasterGUI:
    def __init__(self, master,beatmaster):
        self.master = master
        self.beatmaster = beatmaster

        # Create play button with built-in Tkinter icon
        self.play_button = tk.Button(master, text='Play', command=self.play)
        self.play_button.pack()

        # Create stop button with built-in Tkinter icon
        self.stop_button = tk.Button(master, text='Stop', command=self.stop)
        self.stop_button.pack()

        # Create BPM entry field
        bpm_label = tk.Label(master, text="BPM")
        bpm_label.pack()
        self.bpm_entry = tk.Entry(master,)
        self.bpm_entry.pack()
        self.bpm_entry.bind('<Return>', self.update_bpm)
        # Set default value
        default_bpm = self.beatmaster.bpm
        self.bpm_entry.insert(0, default_bpm)

        # Create a StringVar object to store the selected tonality
        default_tonality =tonality_dict.get(beatmaster.tonal).get('name')
        self.selected_tonality = tk.StringVar(value=default_tonality)
        # Create the Combobox widget
        tonality_label = tk.Label(master, text="Key")
        tonality_label.pack()
        self.tonality_cb = ttk.Combobox(master, textvariable= self.selected_tonality, values=[value['name'] for value in tonality_dict.values() if 'name' in value])
        self.tonality_cb.pack()
        # Bind the set_tonality function to the Combobox's <<ComboboxSelected>> event
        self.tonality_cb.bind("<<ComboboxSelected>>", self.set_tonality)

        self.selected_scale = tk.StringVar(value=beatmaster.scale)        
        scale_dict = InstrumentMap.scaleMapDic
        scale_label = tk.Label(master, text="Scale")
        scale_label.pack()
        self.scale_cb = ttk.Combobox(master, textvariable=self.selected_scale, values=list(scale_dict.keys()))
        self.scale_cb.pack()
        self.scale_cb.bind("<<ComboboxSelected>>", self.set_scale)

        self.beatmaster.add_observer(self)
        
        self.current_tonality = tk.Label(master, text=tonality_dict.get(beatmaster.tonal).get('name'),font=("Helvetica", 36))
        self.current_tonality.pack()




    def play(self):
        self.beatmaster.start()

    def stop(self):
        self.beatmaster.stop()

    def update_bpm(self, event):
        new_bpm = int(self.bpm_entry.get())
        self.beatmaster.bpm = new_bpm

    def set_scale(self,event):
            selected = self.scale_cb.get()
            self.beatmaster.scale = selected

    def set_tonality(self,event):
        # Get the selected tonality string
        selected = self.tonality_cb.get()
        # Find the key in the tonality_dict that corresponds to the selected string
        for key, value in tonality_dict.items():
            if value.get('name',None) == selected:
                # Set the tonality of the beatmaster
                self.beatmaster.change_tonality(key)
                break
    
    def on_tonal_change(self,tonal):
        #update current_tonality label
        self.current_tonality.config(text=tonality_dict.get(tonal).get('name'))

class Metronome:
    def __init__(self,master, beatmaster, time_signature=(4, 4)):
        self.beatmaster = beatmaster
        self.time_signature = time_signature
        self.beat_count = 0
        self.measure_count=-1

        # Subscribe to the beat master
        self.beatmaster.subscribe(self.on_beat, beat_num=1, beat_base=1, is_loop=True)
        # Create a label to show the bpm
        self.beat_label = tk.Label(master, text=f"Not playing")
        self.beat_label.pack()

        self.start_time = time.time()

        # Create labels and entry fields for setting and updating the time signature
        self.time_signature_label = tk.Label(master, text=f"Time Signature: {self.time_signature}")
        self.time_signature_label.pack()

        self.time_signature_frame = tk.Frame(master)
        self.time_signature_frame.pack()

        self.numerator_entry = tk.Entry(self.time_signature_frame, width=5)
        self.numerator_entry.pack(side=tk.LEFT)
        self.numerator_entry.bind('<Return>', self.update_numerator)
        self.numerator_entry.insert(0, self.time_signature[0])
        self.denominator_entry = tk.Entry(self.time_signature_frame, width=5)
        self.denominator_entry.pack(side=tk.LEFT)
        self.denominator_entry.bind('<Return>', self.update_denominator)
        self.denominator_entry.insert(0, self.time_signature[1])

        
        self.tonality_grid_frame = tk.Frame(master)
        self.tonality_grid_frame.pack()

        self.tonality_grid = []
        tonality_grid_label = tk.Label(master, text="Progression grid")
        tonality_grid_label.pack()
        self.tonality_grid_cb = ttk.Combobox(master, textvariable= 'No grid selected', values=[key for key in tonality_grid_dict.keys()])
        self.tonality_grid_cb.pack()
        self.tonality_grid_cb.bind("<<ComboboxSelected>>", self.change_tonality_grid)

        # Create a variable to store the state of the checkbox
        metronome_sound_input_var = tk.IntVar()

        # Create the checkbox
        metronome_sound_input_checkbox = tk.Checkbutton(root, text="metronome sound", variable=use_wave_input_var)
        metronome_sound_input_checkbox.pack()

        # Bind the function to the checkbox
        metronome_sound_input_checkbox.config(command=self.toggle_metronome)



        # create ableton link
        self.ableton_link = AbletonLink(self)

        self.observers_list = [self.ableton_link]

        
    def  toggle_metronome(self):
        for observer in self.observers_list:
            observer.on_metronome_switch(use_wave_input_var.get())
    
    def update_numerator(self, event):
        new_numerator = int(self.numerator_entry.get())
        self.time_signature = (new_numerator, self.time_signature[1])
        self.time_signature_label.config(text=f"Time Signature: {self.time_signature}")
        for observer in self.observers_list:
            observer.on_signature_numerator_change(new_numerator)
    
    def update_denominator(self, event):   
        new_denominator = int(self.denominator_entry.get())
        self.time_signature = (self.time_signature[0], new_denominator)
        self.time_signature_label.config(text=f"Time Signature: {self.time_signature}")
        for observer in self.observers_list:
            observer.on_signature_denominator_change(new_denominator)

    def add_observer(self, observer):
        self.observers_list.append(observer)
    
    def remove_observer(self, observer):
        self.observers_list.remove(observer)

    def on_beat(self):
        self.beat_count += 1
        beat_countdown =  self.beat_count % self.time_signature[0] 
        count = self.time_signature[0] - beat_countdown
        self.beat_label.config(text=f"{count}")

        # Reset the beat count when we've reached the end of a measure
        if self.beat_count == self.time_signature[0]:
            self.beat_count = 0
            if len(self.tonality_grid) > 0:
                self.on_measure_change()

    def on_low_beat(self):
        # print("time since last beat",time.time()-self.start_time)
        self.start_time = time.time()

    def on_measure_change(self):
        tonality_obj = self.tonality_grid[self.measure_count]
        label = tonality_obj[0]
        label.config(bg= 'white')
        self.measure_count+=1
        if self.measure_count >= len(self.tonality_grid):
            self.measure_count = 0
        #get tonality obj
        tonality_obj = self.tonality_grid[self.measure_count]
        label = tonality_obj[0]
        label.config(bg= 'red')

        self.beatmaster.scale = tonality_obj[2]
        self.beatmaster.change_tonality(tonality_obj[1])
        
        pass

    def change_tonality_grid(self,event):
        for label in self.tonality_grid:
            label[0].grid_forget()
        self.tonality_grid = []
        tonality_list = tonality_grid_dict.get(self.tonality_grid_cb.get())
        measure_count = 0
        for tonality, scale, num_measures in tonality_list:
            for j in range(num_measures):
                row = measure_count // 4
                column = measure_count % 4
                text = '%'
                if j == 0:
                    if type(tonality) == str:
                        tonality = self.beatmaster.get_degree_scale(tonality)
                    text = f"{tonality_dict.get(tonality).get('name')}-{scale}"
                
                label = tk.Label(self.tonality_grid_frame, text=text)
                label.grid(row=row, column=column)
                tonality_obj = [label,tonality,scale]
                self.tonality_grid.append(tonality_obj)
                measure_count += 1

# Lists to store created objects
instrumentList = []
controllerList = []
mapperList = []
output_list = []
wave_list = []
message_list = []

# Dictionaries with static entries
instrumentMap = InstrumentMap.keyMapDic
controllerMap = ControllerMap.controllerMapDic 
mapperMap = RulerMap.rulerMapDic

def add_instrument(name=None):
    if not name:
        name = instrument_name_cb.get()
    portName = port_name_cb.get()
    isWave = bool(use_wave_input_var.get())
    inst = MidiInstrument(name=name, portName=portName, isWave = isWave)
    #add midi msg label
    note_label = MidiMsgLabel(root,inst=inst, text="Last Note: ")
    note_label.pack()
    message_list.append(note_label)
    
    if isWave:
        source_name = sound_device_cb.get()
        waveInst = WaveInstrument(name=name, source=source_name, midiInstrument=inst)
        wave_list.append(waveInst)

    instrumentList.append(inst)

def add_output():
    output_name = midi_output_cb.get()
    if output_name=='':
        print("No output selected")
        return
    output_list.append(MidiOutput(output_name))

def add_controller(name=None):
    if name is None:
        name = controller_name_cb.get()
    controllerList.append(GameControler(name=name))

def create_mapper():
    name = mapper_name_cb.get()
    if not name:
        print("select a mapper")
        return
    instrument = instrument_name_cb.get()
    if not instrument:
        print("select an instrument")
        return
    controller = controller_name_cb.get()
    if not controller:
        print("select a controller")
        return
    add_instrument(name=instrument)
    add_controller(name=controller)
    add_output()
    
    mapperList.append(Mapping(name=name, instrumentList=instrumentList, outputList=output_list, controllerList=controllerList))

    # forget all widgets
    create_mapper_button.pack_forget()
    mapper_name_cb.pack_forget()
    

    use_wave_input_checkbox.pack_forget()
    
    input_label.pack_forget()
    sound_device_cb.pack_forget()
    instrument_name_label.pack_forget()
    instrument_name_cb.pack_forget()
    port_name_label.pack_forget()
    port_name_cb.pack_forget()
    controller_name_label.pack_forget()
    controller_name_cb.pack_forget()
    midi_output_label.pack_forget()
    midi_output_cb.pack_forget()
    mapper_name_label.pack_forget()
    mapper_name_cb.pack_forget()
    create_mapper_button.pack_forget()
    delete_mapper_button.pack()

def delete_mapper():
    for lists in [instrumentList, controllerList, mapperList, output_list, wave_list,message_list]:
        for i in lists:
            i.stop()
            lists.clear()

    input_label.pack()
    sound_device_cb.pack()
    instrument_name_label.pack()
    instrument_name_cb.pack()
    port_name_label.pack()
    port_name_cb.pack()
    controller_name_label.pack()
    controller_name_cb.pack()
    midi_output_label.pack()
    midi_output_cb.pack()
    mapper_name_label.pack()
    mapper_name_cb.pack()
    create_mapper_button.pack()
    delete_mapper_button.pack_forget()

def toggle_input_on():
    beat_master.input_on = bool(input_on_var.get())

# Create main window
root = tk.Tk()


input_label = tk.Label(root, text="Input Device")
input_label.pack()

# Create the dropdown selector for sound devices
sound_device_cb = ttk.Combobox(root, values=[device['name'] for device in sd.query_devices()])
sound_device_cb.pack()
sound_device_cb.config(state='disabled')

# Create a function to be called when the checkbox is toggled
def toggle_use_wave_input():
    if use_wave_input_var.get():
        # If the checkbox is checked, disable the instrument name combobox and set its value to 'virtual'
        sound_device_cb.config(state='normal')
        instrument_name_cb.config(state='disabled')
        instrument_name_cb.set('Keyboard')
        port_name_cb.config(state='disabled')
        port_name_cb.set('')
        # Show the sound device dropdown selector
        input_label.pack()
        sound_device_cb.pack()
        
        
    else:
        # If the checkbox is unchecked, enable the instrument name combobox and clear its value
        sound_device_cb.config(state='disabled')
        instrument_name_cb.config(state='normal')
        instrument_name_cb.set('')
        port_name_cb.config(state='normal')
        # Hide the sound device dropdown selector
        # sound_device_cb.pack_forget()
        # input_label.pack_forget()

# Create a variable to store the state of the checkbox
use_wave_input_var = tk.IntVar()

# Create the checkbox
use_wave_input_checkbox = tk.Checkbutton(root, text="Use wave input", variable=use_wave_input_var)
use_wave_input_checkbox.pack()

# Bind the function to the checkbox
use_wave_input_checkbox.config(command=toggle_use_wave_input)

# Create form for adding an instrument
instrument_name_label = tk.Label(root, text="Instrument Name")
instrument_name_label.pack()
instrument_name_cb = ttk.Combobox(root, values=list(instrumentMap.keys()))
instrument_name_cb.pack()

port_name_label = tk.Label(root, text="Port Name")
port_name_label.pack()
port_name_cb = ttk.Combobox(root, values=mido.get_input_names())
port_name_cb.pack()

# add_instrument_button = tk.Button(root, text="Add Instrument", command=add_instrument)
# add_instrument_button.pack()

# Create form for adding a controller
controller_name_label = tk.Label(root, text="Controller Name")
controller_name_label.pack()
controller_name_cb = ttk.Combobox(root, values=list(controllerMap.keys()))
controller_name_cb.pack()

# add_controller_button = tk.Button(root, text="Add Controller", command=add_controller)
# add_controller_button.pack()

# Create form for adding a midi output
midi_output_label = tk.Label(root, text="Midi Output")
midi_output_label.pack()
midi_output_cb = ttk.Combobox(root, values=mido.get_output_names())
midi_output_cb.pack()

# add_output_button = tk.Button(root, text="Add Output", command=add_output)
# add_output_button.pack()


# Create form for creating a mapper
mapper_name_label = tk.Label(root, text="Mapper Name")
mapper_name_label.pack()
mapper_name_cb = ttk.Combobox(root, values=list(mapperMap.keys()))
mapper_name_cb.pack()

create_mapper_button = tk.Button(root, text="Create Mapper", command=create_mapper)
create_mapper_button.pack()

delete_mapper_button = tk.Button(root, text="Delete Mapper", command=delete_mapper)
# Create a checkbox to toggle the beatmaster.input_on variable
input_on_var = tk.IntVar()
input_on_checkbox = tk.Checkbutton(root, text="Input On", variable=input_on_var, command=toggle_input_on)
input_on_checkbox.pack()

gui = BeatMasterGUI(root,beat_master)
metronome= Metronome(root,beat_master)




# class TonalityGrid(tk.Frame):
#     def __init__(self, master=None, progression=None, **kwargs):
#         super().__init__(master, **kwargs)
#         self.progression = progression
#         self.labels = []
#         self.current_index = 0
#         self.create_labels()
#         self.subscribe_tonality_changes()

#     def create_labels(self):
#         tonalitys = InstrumentMap.keyMapDic.get('Keyboard',{}
#                                                          ).get(
#                                                             'note',{}
#                                                             )
#         for i, tonal in enumerate(self.progression):
#             row = i // 4  # Calculate the row based on the index
#             column = i % 4  # Calculate the column based on the index
#             label_text =  tonalitys.get(tonal,{}).get('name',tonal)
#             label = tk.Label(self, text=f"{label_text}")
#             label.grid(row=row, column=column, sticky='w')
#             self.labels.append(label)
    
#     def subscribe_tonality_changes(self):
#         for i, tonal in enumerate(self.progression):
#             # Subscribe the change_tonality function to be called at the start of each bar
#             beat_master.subscribe(beat_master.change_tonality,
#                                   beat_num=(i + 1), 
#                                   beat_base=1, args=(tonal,),
#                                   is_loop=True
#                                 )
#     def on_tonal_change(self):
#         for i, label in enumerate(self.labels):
#             if i == self.current_index:
#                 label.config(bg='red')
#             else:
#                 label.config(bg='white')
#         self.current_index = (self.current_index + 1) % len(self.labels)

# # 12-bar blues progression in C
# blues_progression = [60, 60, 60, 60, 65, 65, 60, 60, 67, 65, 60, 60]

# # Create a TonalityGrid and pack it into the root window
# tonality_grid = TonalityGrid(root, blues_progression)
# tonality_grid.pack()

# # Subscribe the on_tonal_change method of the TonalityGrid to be called whenever the tonality changes
# beat_master.add_observer(tonality_grid)


# class LabelObserver:
#     def __init__(self, bpm_label, tonality_label):
#         self.bpm_label = bpm_label
#         self.tonality_label = tonality_label

#     def on_tonal_change(self):
#         self.bpm_label.config(text=f"BPM: {beat_master.bpm}")
#         tonality = InstrumentMap.keyMapDic.get('Keyboard',{}
#                                                          ).get(
#                                                             'note',{}
#                                                             )
    
#         tonality =  tonality.get(beat_master.tonal,{}).get('name',beat_master.tonal)
#         self.tonality_label.config(
#             text=f"Tonality: {tonality}")

# Create an observer for the labels
# label_observer = LabelObserver(bpm_label, tonality_label)

# # Subscribe the update_labels function to be called whenever the bpm or tonality changes
# beat_master.add_observer(label_observer)

#beat_master.subscribe(on_beat,call_rule = ['next_beat',1], is_loop = True)


# 12-bar blues progression in C
# blues_progression = [60, 60, 60, 60, 65, 65, 60, 60, 67, 65, 60, 60]

# for i, tonal in enumerate(blues_progression):
#     # Subscribe the change_tonality function to be called at the start of each bar
#     beat_master.subscribe(beat_master.change_tonality,
#                            beat_num=(i + 1), 
#                            beat_base=1, args=(tonal,),
#                            is_loop=True
#                         )


# def on_beat():
#     bpm_label.config(bg='red' if bpm_label.cget('bg') == 'white' else 'white')


# beat_master.subscribe(on_beat, beat_num=4, beat_base=4, is_loop=True)

# def update():
#     beat_master._process()
#     root.after(1000 // 60, update)  # 60 frames per second



# beat_master.start()
# update()

try:
    root.mainloop()
except Exception as e:
    print(e)