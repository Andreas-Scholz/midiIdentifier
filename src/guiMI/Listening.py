from tkinter import *
import threading
import time
from midiSourceMI.piano import Piano

class Listening(Frame):

    def __init__(self, parent, controller, params):
        Frame.__init__(self, parent)
        self.controller = controller

        label = Label(self, text="Listening-Tab", font=controller.title_font, background=controller.bg, foreground=controller.fg)
        label.grid(row=0, column=0, padx=10, pady=30)

        self.status = Label(self, text="", font=controller.main_font)
        self.status.grid(row=1, column=0, padx=10, pady=controller.pady)

    def load(self, controller, params):
        return 1

    def afterLoad(self, controller, params):
        piano = Piano(controller.input)

        pianoThread = threading.Thread(target=piano.listen)
        # progressThread = threading.Thread(target=print_progress)

        print("Starting piano thread")
        pianoThread.start()
        while not piano.is_done():
            time.sleep(1)
            print("Progress: {}%".format(piano.get_progress()))
            self.status['text'] = "Progress: {}%".format(piano.get_progress())
            self.update()
        pianoThread.join()
        self.status['text'] = "Done"
        self.update()
        #midi = piano.get_midi_list()
        midi = piano.get_midi()
        midi_list = piano.get_midi_list()
        #del piano
        controller.change_frame("Choose", {'midi':midi, 'midi_list':midi_list})