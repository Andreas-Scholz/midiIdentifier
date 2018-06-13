import _thread
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

    def __init__(self, input_device_id, output_device_id, instrument_id=0):
        self.inp = pygame.midi.Input(input_device_id)
        self.out = pygame.midi.Output(output_device_id, latency=0, buffer_size=4096)
        self.setInstrument(instrument_id)

    def setInstrument(self, instrument_id=0):
        self.out.set_instrument(instrument_id)

    def setActive(self):
        try:
            _thread.start_new_thread(self._run_piano, ("piano", self.inp, self.out,))
        except:
            print("Error: unable to start thread")

    def _run_piano(self, thread_name, inp, out):
        while True:
            if inp.poll():
                data = inp.read(100)
                for sound in data: # more than one key can be pressed aat one time
                    key_data = sound[0] # ignore timestamp
                    key_value = str(key_data[1]) # the specific key that has been pressed
                    if(key_data[0] == KEY_DOWN):
                        fluid.write(("noteon 0 " + key_value + " 127\n").encode('ascii'))
                    if(key_data[0] == KEY_UP):
                        fluid.write(("noteoff 0 " + key_value + " 127\n").encode('ascii'))
                # print(data)
            # wait a short while to prevent 100% cpu utilization
            pygame.time.wait(100)


def main():
    # list all midi devices
    print("Midi devices")
    print(devices.list_midi_input_devices())
    inp = int(input("Choose a device: "))

    # list all audio devices
    print("Audio devices")
    print(devices.list_output_devices())
    out = int(input("Choose a device: "))

    piano = Piano(inp, out)
    piano.setActive()

    for i in range (1,10):
        print(i)
        time.sleep(10)


if __name__ == "__main__":
    main()
