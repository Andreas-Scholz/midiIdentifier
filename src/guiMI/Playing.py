from tkinter import *

class Playing(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Playing Song...", font=controller.title_font, background=controller.bg)
        label.grid(row=0, column=0, padx=10, pady=3)

        self.chosen_song = Label(self, text="")
        self.chosen_song.grid(row=1, column=0, padx=10, pady=3)

        button = Button(self, text="<-- Reset",
                           command=lambda: controller.change_frame("Listening", {}))
        button.grid(row=2, column=0, padx=10, pady=3)

    def load(self, params):
        self.chosen_song['text'] = params['chosen_song_name']

    def afterLoad(self, params):
        return 1