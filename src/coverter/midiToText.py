import os

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
    return midi_files