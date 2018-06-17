from tkinter import *
import threading
import time
from midiSourceMI.piano import Piano
import compare

class Listening(Frame):

    def __init__(self, parent, controller, params):
        Frame.__init__(self, parent)
        self.controller = controller

        label = Label(self, text="Listening-Tab", font=controller.title_font, background=controller.bg)
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
        controller.change_frame("Choose", {'midi':piano.get_midi()})