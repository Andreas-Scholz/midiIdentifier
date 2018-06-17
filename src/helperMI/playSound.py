import time
from telnetlib import Telnet


# fluid = Telnet("pi","9988")
fluid = Telnet("192.168.0.21","9988")
fluid.write("noteon 0 64 127\n".encode('ascii'))
time.sleep(3)
fluid.write("noteoff 0 64 127\n".encode('ascii'))





"""
import pygame.midi
import pyaudio

pygame.midi.init()

def list_midi_input_devices():
    input_devices_available = dict()
    for x in range(0, pygame.midi.get_count()):
        ""
        returns information about a midi device
        get_device_info(an_id) -> (interf, name, input, output, opened)
        ""
        if pygame.midi.get_device_info(x)[2] == 1: #input device
            input_devices_available[pygame.midi.get_device_info(x)[1].decode("utf-8")] = x
    return input_devices_available

# list all audio output devices
def list_output_devices():
    p = pyaudio.PyAudio()
    output_devices_available = dict()
    for i in range(p.get_device_count()):
        if p.get_device_info_by_index(i)["maxOutputChannels"] > 0:  # output device
            print("Device [" + str(i) + "]: " + str(p.get_device_info_by_index(i)))
            output_devices_available[p.get_device_info_by_index(i)["name"]] = i
    return output_devices_available


print(list_output_devices())
midi_devices = pygame.midi.get_count()
for device in range(0,midi_devices):
    print(str(pygame.midi.get_device_info(device)))
player = pygame.midi.Output(int(input("Choose audio device: ")))
player.set_instrument(0)
print("Note on")
# player.note_on(64, 127)
player.write([[[0xc0,0,0],20000],[[0x90,60,100],20500]])
time.sleep(3)
player.note_off(64, 127)
print("Note off")
print("Note on")
player.write_short(0x90,65,100)
# player.note_on(64, 127)
time.sleep(3)
player.note_off(64, 127)
print("Note off")
print("Note on")
player.note_on(64, 127,1)
time.sleep(3)
player.note_off(64, 127)
print("Note off")
del player
pygame.midi.quit()
"""

