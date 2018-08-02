# midiIdentifier

## 1. RPi set-up
- Install a clean raspberry os image
- Download fluidsynth soundfont: ```wget https://downloads.sourceforge.net/project/androidframe/soundfonts/FluidR3_GM.sf2?r=https%3A%2F%2Fsourceforge.net%2Fprojects%2Fandroidframe%2Ffiles%2Fsoundfonts%2FFluidR3_GM.sf2%2Fdownload&ts=1528887471```
- rename the downloaded file to FluidR3_GM.sf2
- install fluidsynth ```sudo apt-get install fluidsynth```
- sudo apt-get install telnet
- sudo apt-get install screen
- sudo apt-get install git
- enable autostart of fluidsynrh as described above
- clone midiIdentifier repository
- add the repo to the pythonpath. Edit ~/.bashrc and add the following lines:
```
PYTHONPATH="${PYTHONPATH}:/home/pi/workspace/midiIdentifier/src"
export PYTHONPATH
```
- reload the .bashrc file with ```. ~/.bashrc```
- Install pyaudio ```sudo apt-get install python3-pyaudio ```


## 2. Start fluidsynth
```
fluidsynth -a alsa -m alsa_seq -i -s -o "shell.port=9988" -g 2 FluidR3_GM.sf2
```
To enable fluidsynth autostart:
```
crontab -e
```
Add the following line:
```
@reboot /usr/bin/screen -dm /usr/bin/fluidsynth -a alsa -m alsa_seq -i -s -o "shell.port=9988" -g 2 /home/pi/workspace/soundfonts/FluidR3_GM.sf2
```

## 3. To access fluidsynth via python:
```python
from telnetlib import Telnet
fluid = Telnet("localhost","9988")
fluid.write("noteon 0 64 127\n".encode('ascii'))
```

## 4. Display setup
Open /boot/config.txt
- Enter / Change in File:
```
max_usb_current=1
hdmi_group=2
hdmi_mode=87
hdmi_cvt 1024 600 60 6 0 0 0
hdmi_drive=1
```
__ATTENTION: NO SPACES BETWEEN "="!__
