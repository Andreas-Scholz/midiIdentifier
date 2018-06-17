from tkinter import *
import tkinter as tk
from audioMI import devices

class Choose_input(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        rowc = 0
        label = Label(self, text="Input-Device wählen", font=controller.title_font, background=controller.bg)
        label.grid(row=rowc, column=0, padx=10, pady=3)
        rowc += 1

        for value, key in devices.list_midi_input_devices().items():
            song_button = Button(self, text=value, width=30,
                                    command=lambda key=key, value=value: self.choose(controller, key, value))
            song_button.grid(row=rowc, column=0, padx=10, pady=3)
            rowc += 1

    def load(self, params):
        return 1

    def afterLoad(self, params):
        return 1

    def choose(self, controller, id, name):
        controller.change_frame("Choose_output",{'chosen_input':id})