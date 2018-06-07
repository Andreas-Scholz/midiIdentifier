import pygame
import pyaudio


def list_midi_input_devices():
    input_devices_available = dict()
    for x in range(0, pygame.midi.get_count()):
        """
        returns information about a midi device
        get_device_info(an_id) -> (interf, name, input, output, opened)
        """
        if pygame.midi.get_device_info(x)[2] == 1: #input device
            input_devices_available[pygame.midi.get_device_info(x)[1].decode("utf-8")] = x
    return input_devices_available

# list all audio output devices
def list_output_devices():
    p = pyaudio.PyAudio()
    output_devices_available = dict()
    for i in range(p.get_device_count()):
        if p.get_device_info_by_index(i)["maxOutputChannels"] > 0:  # output device
            output_devices_available[p.get_device_info_by_index(i)["name"]] = i
    return output_devices_available
