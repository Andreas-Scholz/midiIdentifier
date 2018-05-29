#!/usr/bin/python

import midiToText

MIDI_DIR = "./../files/midi/"



def main():
    print(midiToText.convertAll(MIDI_DIR))

if __name__ == '__main__':
    main()
