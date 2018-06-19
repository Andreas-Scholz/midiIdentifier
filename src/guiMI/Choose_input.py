from tkinter import *
from audioMI import devices

class Choose_input(Frame):
    def __init__(self, parent, controller, params):
        Frame.__init__(self, parent)
        self.controller = controller
        rowc = 0
        label = Label(self, text="Input-Device wählen", font=controller.title_font, background=controller.bg)
        label.grid(row=rowc, column=0, padx=10, pady=30)
        rowc += 1
        for value, key in devices.list_midi_input_devices().items():
            song_button = Button(self, text=value, width=controller.button_width, height=controller.button_height, font=controller.main_font,
                                    command=lambda key=key, value=value: self.choose(controller, key, value))
            song_button.grid(row=rowc, column=0, padx=10, pady=controller.pady)
            rowc += 1

    def load(self, controller, params):
        return 1

    def afterLoad(self, controller, params):
        return 1

    def choose(self, controller, id, name):
        controller.input = id
        controller.change_frame("Listening",{})