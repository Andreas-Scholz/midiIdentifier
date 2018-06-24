from tkinter import *
from audioMI.MidiPlayer2 import MidiPlayer2
import functools

class Playing(Frame):

    def __init__(self, parent, controller, params):
        Frame.__init__(self, parent)
        self.controller = controller

        self.player = MidiPlayer2()

        label = Label(self, text="", font=controller.title_font, background=controller.bg, foreground=controller.fg, anchor="w", width=50)
        label.grid(row=0, column=0, padx=10, pady=30)

        final_string = "> PLAYING SONG:"
        self.delta = controller.delta
        self.delay = 0
        for i in range(len(final_string) + 1):
            s = final_string[:i]
            label.after(self.delay, functools.update_wrapper( functools.partial(label.config, text=s), label.config))
            self.delay += self.delta

        self.label2 = Label(self, text="", font=controller.title_font, background=controller.bg, foreground=controller.fg, anchor="w", width=50)
        self.label2.grid(row=1, column=0, padx=10, pady=controller.pady)

        self.button = Label(self, text="", font=controller.title_font, background=controller.bg, foreground=controller.prompt, anchor="w", width=50)
        self.button.grid(row=2, column=0, padx=10, pady=30)
        self.button.bind("<Button-1>", self.reset, controller)

    def load(self, controller, params):
        song_display = params['chosen_song_name'].replace(".mid","")
        final_string = "> " + song_display
        #self.chosen_song['text'] = params['chosen_song_name']
        for i in range(len(final_string) + 1):
            s = final_string[:i]
            self.label2.after(self.delay, functools.update_wrapper( functools.partial(self.label2.config, text=s), self.label2.config))
            self.delay += self.delta

        final_string = "> RESET"
        for i in range(len(final_string) + 1):
            s = final_string[:i]
            self.button.after(self.delay, functools.update_wrapper( functools.partial(self.button.config, text=s), self.button.config))
            self.delay += self.delta

        self.player.play("../../files/new_midi/"+params['chosen_song_name'])

    def afterLoad(self, controller, params):
        return 1

    def reset(self,controller):
        self.player.stop()
        self.controller.change_frame('Listening', {})