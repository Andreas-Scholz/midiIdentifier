import tkinter as tk
import threading
import time
from tkinter import font as tkfont
from audioMI import devices
from midiSourceMI.piano import Piano

#GLOBAL Variables

CHOSEN_INPUT = None
CHOSEN_OUTPUT = None

class MidiIdentifier(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Listening, Processing, Choose, Playing, Choose_input, Choose_output):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        # this is the startup frame
        self.change_frame("Choose_input", {})

    def change_frame(self, page_name, params):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.load(params)
        frame.tkraise()
        self.update()
        frame.afterLoad(params)

    # Variables accessible by all frames
    songs = {1: 'Britney Spears - I\'m fat', 2: 'Melania Trump - Help', 3: 'Donald Trump - Grab \'em by the pussy',
             4: 'Bon Jovi - Still not dead', 5: 'Karsten Schick - A man with no prejudices'}
    chosen_song = False

    devices = {1: 'bla', 2:'blubb'}
    chosen_device = False


class Listening(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Listening-Tab", font=controller.title_font)
        label.grid(row=0, column=0, padx=10, pady=3)

        self.status = tk.Label(self, text="")
        self.status.grid(row=1, column=0, padx=10, pady=3)

        button = tk.Button(self, text="Processing -->",
                           command=lambda: controller.change_frame("Processing", {}))
        button.grid(row=2, column=0, padx=10, pady=3)

    def load(self, params):
        return 1

    def afterLoad(self, params):
        global CHOSEN_OUTPUT
        global CHOSEN_INPUT
        piano = Piano(CHOSEN_INPUT,CHOSEN_OUTPUT)

        pianoThread = threading.Thread(target=piano.listen)
        # progressThread = threading.Thread(target=print_progress)

        print("Starting piano thread")
        pianoThread.start()
        while not piano.is_done():
            time.sleep(1)
            print("Progress: {}%".format(piano.get_progress()))
            self.status['text'] = "Progress: {}%".format(piano.get_progress())
            self.update()


class Processing(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Processing-Tab", font=controller.title_font)
        label.grid(row=0, column=0, padx=10, pady=3)
        button = tk.Button(self, text="<-- Reset",
                           command=lambda: controller.change_frame("Listening", {}))
        button.grid(row=1, column=0, padx=10, pady=3)
        button2 = tk.Button(self, text="Choose -->",
                            command=lambda: controller.change_frame("Choose", {}))
        button2.grid(row=1, column=2, padx=10, pady=3)

    def load(self, params):
        return 1

    def afterLoad(self, params):
        return 1


class Choose(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        rowc = 0
        label = tk.Label(self, text="Welchen Song meintest du?", font=controller.title_font)
        label.grid(row=rowc, column=0, padx=10, pady=3)
        rowc += 1

        for key, value in controller.songs.items():
            song_button = tk.Button(self, text=value, bg="#FFFFFF", width=30,
                                    command=lambda key=key, value=value: self.choose(controller, key, value))
            song_button.grid(row=rowc, column=0, padx=10, pady=3)
            rowc += 1

        button = tk.Button(self, text="<-- Reset",
                           command=lambda: controller.change_frame("Listening", {}))
        button.grid(row=rowc + 1, column=0, padx=10, pady=3)

    def load(self, params):
        return 1

    def afterLoad(self, params):
        return 1

    def choose(self, controller, id, name):
        chosen_song = id
        controller.change_frame("Playing", {'chosen_song_id': id, 'chosen_song_name': name})


class Playing(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Playing Song...", font=controller.title_font)
        label.grid(row=0, column=0, padx=10, pady=3)

        self.chosen_song = tk.Label(self, text="")
        self.chosen_song.grid(row=1, column=0, padx=10, pady=3)

        button = tk.Button(self, text="<-- Reset",
                           command=lambda: controller.change_frame("Listening", {}))
        button.grid(row=2, column=0, padx=10, pady=3)

    def load(self, params):
        self.chosen_song['text'] = params['chosen_song_name']

    def afterLoad(self, params):
        return 1


class Choose_input(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        rowc = 0
        label = tk.Label(self, text="Input-Device wählen", font=controller.title_font)
        label.grid(row=rowc, column=0, padx=10, pady=3)
        rowc += 1

        for value, key in devices.list_midi_input_devices().items():
            song_button = tk.Button(self, text=value, bg="#FFFFFF", width=30,
                                    command=lambda key=key, value=value: self.choose(controller, key, value))
            song_button.grid(row=rowc, column=0, padx=10, pady=3)
            rowc += 1

    def load(self, params):
        return 1

    def afterLoad(self, params):
        return 1

    def choose(self, controller, id, name):
        global CHOSEN_INPUT
        CHOSEN_INPUT = id
        controller.change_frame("Choose_output",{})

class Choose_output(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        rowc = 0
        label = tk.Label(self, text="Output-Device wählen", font=controller.title_font)
        label.grid(row=rowc, column=0, padx=10, pady=3)
        rowc += 1

        for value, key in devices.list_output_devices().items():
            song_button = tk.Button(self, text=value, bg="#FFFFFF", width=30,
                                    command=lambda key=key, value=value: self.choose(controller, key, value))
            song_button.grid(row=rowc, column=0, padx=10, pady=3)
            rowc += 1

    def load(self, params):
        return 1

    def afterLoad(self, params):
        return 1

    def choose(self, controller, id, name):
        global CHOSEN_OUTPUT
        CHOSEN_OUTPUT = id
        # print("Starting progress thread")
        # progressThread.start()

        #while not piano.is_done():
        #    time.sleep(1)
        #    print("Progress: {}%".format(piano.get_progress()))

        #pianoThread.join()
        #print("Finished. Midi file: \"" + piano.get_midi() + "\"")
        controller.change_frame("Listening",{})


if __name__ == "__main__":
    app = MidiIdentifier()
    app.mainloop()
