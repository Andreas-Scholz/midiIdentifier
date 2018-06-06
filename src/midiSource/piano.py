import sys, pygame, pygame.midi
import pyaudio
import time
from audio import devices

# set up pygame
pygame.mixer.pre_init(44100,-16,2,2048)
pygame.init()
pygame.midi.init()

# list all midi devices
print("Midi devices")
print(devices.list_midi_input_devices())
# open a specific midi device
# inp = pygame.midi.Input(1)
inp = pygame.midi.Input(int(input("Choose a device: ")))

# for x in range(0, pygame.midi.get_count()):
#     print(pygame.midi.get_device_info(x)[1].decode("utf-8") )

# list all audio devices
print("Audio devices")
print(devices.list_output_devices())
# open an output device
out = pygame.midi.Output(int(input("Choose a device: ")), latency=0, buffer_size=4096)


# p = pyaudio.PyAudio()
# for i in range(p.get_device_count()):
#     print(p.get_device_info_by_index(i)["name"])




out.set_instrument(0)
# out.note_on(64, 127)
# time.sleep(1)
# out.note_off(64, 127)

# run the event loop
while True:
    if inp.poll():
        # no way to find number of messages in queue
        # so we just specify a high max value
        # print(inp.read(1000))
        out.write(inp.read(1))


    # wait 10ms - this is arbitrary, but wait(0) still resulted
    # in 100% cpu utilization
    pygame.time.wait(10)