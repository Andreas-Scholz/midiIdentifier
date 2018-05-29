#!/usr/bin/python

import subprocess
import midiToText
from compare import compare

MIDI_DIR = "./../files/midi/"
MIDI_FILE = "Alle_Meine_Entchen.mid"
MIDI_FILE2 = "for_elise_by_beethoven.mid"
MIDI_FILE3 = "alle_meine_entchen--heilpaedagogik-info-de.mp3.mid"
MIDI_FILE4 = "alle_meine_entchen--heilpaedagogik_modified.mid"

def get_midi_as_text(file):
    hex_representation = subprocess.check_output(
        "od -xAn " + "C:\\workspace\\uni\\midiIdentifier\\files\\midi\\" + file, shell=True) \
        .decode("utf-8").replace('\n', ' ')
    return hex_representation

def main():
    single_midi_as_text = get_midi_as_text(MIDI_FILE4)
    midi_text_files = midiToText.convertAll(MIDI_DIR)
    print(type(single_midi_as_text))
    print(type(midi_text_files))
    matches = compare(single_midi_as_text, midi_text_files)
    print (matches)

if __name__ == '__main__':
    main()
