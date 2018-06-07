import _thread
import time
import pygame, pygame.midi
from audioMI import devices

# set up pygame
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
pygame.midi.init()


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
                out.write(data)
                print(data)
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
