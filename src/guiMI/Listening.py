from tkinter import *
import threading
import time
from midiSourceMI.piano import Piano

class Listening(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        label = Label(self, text="Listening-Tab", font=controller.title_font, background=controller.bg)
        label.grid(row=0, column=0, padx=10, pady=30)

        self.status = Label(self, text="", font=controller.main_font)
        self.status.grid(row=1, column=0, padx=10, pady=controller.pady)

        button = Button(self, text="Processing -->", width=controller.button_width, height=controller.button_height, font=controller.main_font,
                           command=lambda: controller.change_frame("Processing", {}))
        button.grid(row=2, column=0, padx=10, pady=controller.pady)

    def load(self, params):
        return 1

    def afterLoad(self, params):
        piano = Piano(params['chosen_input'], params['chosen_output'])

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