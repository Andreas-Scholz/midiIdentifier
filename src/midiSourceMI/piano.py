import threading
import time
import pygame, pygame.midi
from audioMI import devices
from telnetlib import Telnet

# set up pygame
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
pygame.midi.init()

# set up fluidsynth
fluid = Telnet("192.168.0.21","9988")
# fluid = Telnet("pi","9988")

KEY_DOWN = 144
KEY_UP = 128

class Piano(object):

    progress = 0
    isDone = False
    midi = ""

    def __init__(self, input_device_id, output_device_id, instrument_id=0):
        self.inp = pygame.midi.Input(input_device_id)
        self.out = pygame.midi.Output(output_device_id, latency=0, buffer_size=4096)
        self.set_instrument(instrument_id)
        self._reset_all()

    def _reset_all(self):
        self.progress = 0
        self.isDone = False
        self.midi = ""

    def set_instrument(self, instrument_id=0):
        self.out.set_instrument(instrument_id)

    def is_done(self):
        return self.isDone

    def get_progress(self):
        return self.progress

    def get_midi(self):
        return self.midi

    def listen(self):
        self._reset_all()
        while self.progress <100:
            if self.inp.poll():
                data = self.inp.read(100)
                for sound in data: # more than one key can be pressed at one time
                    key_data = sound[0] # ignore timestamp
                    key_value = str(key_data[1]) # the specific key that has been pressed
                    if(key_data[0] == KEY_DOWN):
                        fluid.write(("noteon 0 " + key_value + " 127\n").encode('ascii'))
                        self.midi += ("n" + key_value)
                    if(key_data[0] == KEY_UP):
                        fluid.write(("noteoff 0 " + key_value + " 127\n").encode('ascii'))
                    self.progress += 5
            # wait a short while to prevent 100% cpu utilization
            pygame.time.wait(100)
        self.isDone = True

    def play_midi(self, midi):
        notes = midi.split('n')
        for note in notes:
            fluid.write(("noteon 0 " + str(note) + " 127\n").encode('ascii'))
            pygame.time.wait(500)

def main():
    # list all midi devices
    print("Midi input devices")
    print(devices.list_midi_input_devices())
    inp = int(input("Choose a midi input device: "))

    # list all audio devices
    print("Audio output devices")
    print(devices.list_output_devices())
    out = int(input("Choose an audio output device: "))

    print("Creating piano")
    piano = Piano(inp, out)

    # piano.setActive()
    print("Creating threads")
    pianoThread = threading.Thread(target=piano.listen)
    # progressThread = threading.Thread(target=print_progress)

    print("Starting piano thread")
    pianoThread.start()
    # print("Starting progress thread")
    # progressThread.start()

    while not piano.is_done():
        time.sleep(1)
        print("Progress: {}%".format(piano.get_progress()))

    pianoThread.join()
    print("Finished. Midi file: \"" + piano.get_midi() + "\"")

    print("GUI thread continuing some other stuff...")
    for i in range (1,10):
        print(i)
        time.sleep(10)


if __name__ == "__main__":
    main()
