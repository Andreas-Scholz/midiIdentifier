import os
import subprocess
import time
from mido import MidiFile
from midiSourceMI.piano import Piano

# MIDI_DIR = "../../files/midi/top1000/"
MIDI_DIR = "../../files/new_midi/"
OUT = "../../files/songs.json"
JSON_START = "[\n"
JSON_END = "]\n"
SONG_START = "\t{\n"
SONG_END = "\t},\n"
SONG_END_LAST = "\t}\n"

def __get_all_files_in_dir(dir, extension="mid"):
    files = []
    for file in os.listdir(dir):
        if file.endswith("." + extension):
            files.append(file)
    return files


def convertAll(dir):
    midi_files = __get_all_files_in_dir(dir, "mid")
    midi_text_files = __convert(midi_files)
    return midi_text_files


def __convert(midi_files):
    midi_text_files = dict()
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


# def _convert_midi_msg(msg):
#     if not msg.is_meta and not str(msg).startswith("program_change") and not str(msg).startswith("control_change"):
#         if msg.type == 'note_on':
#             return "n" + str(msg.note)
#         else:
#             return ""
#     else:
#         return ""

def _msg_is_note_on(msg):
    return not msg.is_meta and \
           not str(msg).startswith("program_change") and \
           not str(msg).startswith("control_change") and \
           msg.type == 'note_on'


def _convert_to_short_midi(midi_file_name, sm_max_length=20):
    # print("converting file: \"" + midi_file_name + "\"")

    short_midi = ""
    notes = []
    midi_file = MidiFile(MIDI_DIR + midi_file_name)
    length = 0
    for msg in midi_file:
        if length < sm_max_length and _msg_is_note_on(msg):
            notes.append(msg.note)
            short_midi += "n" + str(msg.note)
            length += 1
    return notes, short_midi


def main():
    start_time = time.time()

    midi_files = __get_all_files_in_dir(MIDI_DIR)
    output_file = open(OUT, "a+")

    short_midis = {}
    error_files = []

    output_file.write(JSON_START)
    for i, midi in enumerate(midi_files):
        if i%100 == 0:
            print(str(i))
        try:
            notes, short_midi = _convert_to_short_midi(midi, 20)
            short_midis[midi] = short_midi
            output_file.write(SONG_START)
            output_file.write("\t\t\"name\": \"" + midi + "\",\n")
            output_file.write("\t\t\"notes\": [")
            for j in range(len(notes)):
                note = str(notes[j])
                if j is not len(notes):
                    output_file.write(note + ",")
                else:
                    output_file.write(note)
            output_file.write("],\n")
            output_file.write("\t\t\"short_midi\": \"" + short_midi + "\"\n")
            if i != len(midi_files)-1:
                output_file.write(SONG_END)
            else:
                output_file.write(SONG_END_LAST)
        except:
            error_files.append(midi)
    output_file.write(JSON_END)

    # print(short_midis)
    print(error_files)

    piano = Piano.without_devices()
    #for sm in short_midis.keys():
        #print("Playing \"" + sm + "\"")
        #piano.play_midi(short_midis[sm])

    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()
