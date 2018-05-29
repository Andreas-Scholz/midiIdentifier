import os
import subprocess



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
    for file in midi_files:
        hex_representation = subprocess.check_output(
            "od -xAn " + "C:\\workspace\\uni\\midiIdentifier\\files\\midi\\" + file, shell=True)\
            .decode("utf-8").replace('\n', ' ')
        midi_text_files[file] = hex_representation
    return midi_text_files
