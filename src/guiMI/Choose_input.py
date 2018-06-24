from tkinter import *
from audioMI import devices
import functools

class Choose_input(Frame):
    def __init__(self, parent, controller, params):
        Frame.__init__(self, parent)
        self.controller = controller
        rowc = 0


        label = Label(self, text="", font=controller.title_font, background=controller.bg, foreground=controller.fg, anchor="w", width=controller.label_width)
        label.grid(row=rowc, column=0, padx=10, pady=30)

        final_string = "> CHOOSE AN INPUT DEVICE:"
        delta = controller.delta
        delay = 0
        for i in range(len(final_string) + 1):
            s = final_string[:i]
            update_text = lambda s=s: label.config(text=s)
            label.after(delay, update_text)
            delay += delta


        rowc += 1
        for value, key in devices.list_midi_input_devices().items():
            song_button = Label(self, text="", font=controller.title_font, background=controller.bg, foreground=controller.prompt, anchor="w", width=controller.label_width)
            song_button.grid(row=rowc, column=0, padx=10, pady=controller.pady)
            song_button.bind("<Button-1>",lambda value=value, key=key: self.choose(controller, key, value))
            final_string = "> " + value
            for i in range(len(final_string) + 1):
                s = final_string[:i]
                song_button.after(delay, functools.update_wrapper( functools.partial(song_button.config, text=s), song_button.config))
                delay += delta
            rowc += 1

    def load(self, controller, params):
        return 1

    def afterLoad(self, controller, params):
        return 1

    def choose(self, controller, id, name):
        controller.input = id
        controller.change_frame("Listening",{})