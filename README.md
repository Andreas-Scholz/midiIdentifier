# midiIdentifier

## 1. Fluidsynth starten
Fluidsynth starten und auf Port 9988 horchen lassen.
Die Option "-g 2" macht die ausgabe lauter.
```
fluidsynth -a alsa -m alsa_seq -i -s -o "shell.port=9988" -g 2 FluidR3_GM.sf2
```
Um fluidsynth bei jedem neustart automatisch zu starten:
```
crontab -e
```
Und anschließend folgende Zeile einfügen:
```
@reboot /usr/bin/screen -dm /usr/bin/fluidsynth -a alsa -m alsa_seq -i -s -o "shell.port=9988" -g 2 /home/pi/workspace/soundfonts/FluidR3_GM.sf2
```

## 2. Mit Skript auf fluidsynth zugreifen
```python
from telnetlib import Telnet
fluid = Telnet("localhost","9988")
fluid.write("noteon 0 64 127\n".encode('ascii'))
```

## 3. RPi set-up
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
- You are good to go!