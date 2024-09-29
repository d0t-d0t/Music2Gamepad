# Music2GamePad

## Description

The main goal of this project is to provide ways to use any music instrument, including voice as game controller. 

## Functions and Limitations
For the moment you can:
    - emulate keyboard and gmaepad input with midi input
    - emulate midi input with any sound source comming from a sound device (e.g. a microphone)
    - repeat a midi input trough an output
    

## Installation and Requirement
I developped this programm for my personnal use so it isn't user friendly at all, even if there is a GUI tkinter to make it easier to use.

It may change in the futur, but for now you may have to dig in code to get it.

It is probably fully working only on Windows.
At early stage it was working on linux, but I stopped cross OS dev.

There is currently no package to ease the installation. If you want to try it you would have to install yourself needed library.

```bash
pip install tkinter mido sounddevice pythonosc threading git+https://git.aubio.org/aubio/aubio/ vgamepad numpy scipy

```
(installation of aubio directly from git do solve some issues, e.g.: windows using french as system will have issu with pre-compiled binary)

You may also need LoopMidi from https://www.tobias-erichsen.de/software.html to be able to repeat midi output trough a virtual midi input. On windows, midi input are excllusive, so if you capture 

## Launch and Use

- launch main.py

### MAP instument to controller

#### your want to use a wave sound input (e.g. a microphone):
    - check 'use wave input'
    - select your input device in 'input device'

#### you want to use midi input (e.g. midi keyboard)
    - select an 'instrument name' (if midi input are not of keyboard type, you need to add it manually in InsturmentMap.py>>>keyMapDic)
    - select 'Port name'. It is the midi input port of you instrument

- select a controller name. (look into ControllerMap.py to get what is what and add one manually if you have specific needs)

- Midi Output: if you want to repeat the midi signal, select a  

- Mapper Name:  Mappers are dictionnary that list all the specific rules (You would have to look in RulerMap.py to understand and add mapping rules)

- Click on 'Create Mapper' and now your music input should emulate controller output

