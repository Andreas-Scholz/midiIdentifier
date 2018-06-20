#!/usr/bin/python

import subprocess
import midiToText
import operator
import time
from mido import MidiFile
from midiSourceMI.piano import Piano

from compare from comparatorMI import compare

MIDI_DIR = "./../files/midi/"
MIDI_FILE = "Alle_Meine_Entchen.mid"
MIDI_FILE2 = "for_elise_by_beethoven.mid"
MIDI_FILE3 = "alle_meine_entchen--heilpaedagogik-info-de.mp3.mid"
MIDI_FILE4 = "alle_meine_entchen--heilpaedagogik_modified.mid"
MIDI_FILE5 = "for_elise_by_beethoven_shortened.mid"

def get_midi_as_text(file):
    hex_representation = subprocess.check_output(
        "od -xAn " + "C:\\workspace\\uni\\midiIdentifier\\files\\midi\\" + "\"" + file + "\"", shell=False) \
        .decode("utf-8").replace('\n', ' ')
    return hex_representation


def convert(msg):
    if msg.type == 'note_on':
        return "n" + str(msg.note)
    else:
        return ""


def main():

    midi = "n60n62n64n65n67n67n69n69n69n69n67n69n69n69n69n67n65"

    # midi_file = MidiFile(MIDI_DIR + MIDI_FILE5)
    # for msg in midi_file:
    #     if not msg.is_meta and not str(msg).startswith("program_change") and not str(msg).startswith("control_change"):
    #         midi += convert(msg)

    # piano = Piano(1,2)
    piano = Piano.without_devices()
    piano.play_midi(midi)

    print(midi)

    # start_time = time.time()
    # single_midi_as_text = get_midi_as_text(MIDI_FILE5)
    # midi_text_files = midiToText.convertAll(MIDI_DIR)
    #
    # matches = compare(single_midi_as_text, midi_text_files)
    # sorted_matches = sorted(matches.items(), key=operator.itemgetter(1), reverse=True)[:20]
    # print(sorted_matches)
    # print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    main()
