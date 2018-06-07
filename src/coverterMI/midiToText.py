import os
import subprocess
from mido import MidiFile

def __get_files_in_dir(dir, extension="mid"):
    files = []
    for file in os.listdir(dir):
        if file.endswith("." + extension):
            files.append(file)
    return files


def convertAll(dir):
    midi_files = __get_files_in_dir(dir, "mid")
    midi_text_files = __convert(midi_files)
    return midi_text_files


def __convert(midi_files):
    midi_text_files = dict()
    print(len(midi_files))
    for i, file in enumerate(midi_files):
        if i % 100 == 0:
            print(i)
        try:
            hex_representation = subprocess.check_output(
                "od -xAn " + "C:\\workspace\\uni\\midiIdentifier\\files\\midi\\Bsmall\\" + "\"" + file + "\"",
                shell=False) \
                .decode("utf-8").replace('\n', ' ')
            midi_text_files[file] = hex_representation
        except:
            midi_text_files[file] = ""
    return midi_text_files


def convert(dir, filename):
    pass
