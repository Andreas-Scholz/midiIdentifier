# midiIdentifier

## 1. Fluidsynth starten
Fluidsynth starten und auf Port 9988 horchen lassen.
Die Option "-g 2" macht die ausgabe lauter.
```
fluidsynth -a alsa -m alsa_seq -i -s -o "shell.port=9988" -g 2 FluidR3_GM.sf2
```

## 2. Mit Skript auf fluidsynth zugreifen
```python
from telnetlib import Telnet
fluid = Telnet("localhost","9988")
fluid.write("noteon 0 64 127\n".encode('ascii'))
```

