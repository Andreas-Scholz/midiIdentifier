from tkinter import *
from audioMI.MidiPlayer2 import MidiPlayer2

class Playing(Frame):

    def __init__(self, parent, controller, params):
        Frame.__init__(self, parent)
        self.controller = controller

        self.player = MidiPlayer2()

        label = Label(self, text="Playing Song...", font=controller.title_font, background=controller.bg)
        label.grid(row=0, column=0, padx=10, pady=30)

        self.chosen_song = Label(self, text="", font=controller.main_font)
        self.chosen_song.grid(row=1, column=0, padx=10, pady=controller.pady)

        button = Button(self, text="<-- Reset", width=controller.button_width, height=controller.button_height, font=controller.main_font,
                           command=lambda:self.reset(controller))
        button.grid(row=2, column=0, padx=10, pady=controller.pady)

    def load(self, controller, params):
        self.chosen_song['text'] = params['chosen_song_name']
        #self.player.play("../../files/midi/"+params['chosen_song_name'])

    def afterLoad(self, controller, params):
        return 1

    def reset(self,controller):
        self.player.stop()
        controller.change_frame('Listening', {})