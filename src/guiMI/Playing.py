from tkinter import *

class Playing(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Playing Song...", font=controller.title_font, background=controller.bg)
        label.grid(row=0, column=0, padx=10, pady=30)

        self.chosen_song = Label(self, text="", font=controller.main_font)
        self.chosen_song.grid(row=1, column=0, padx=10, pady=controller.pady)

        button = Button(self, text="<-- Reset", width=controller.button_width, height=controller.button_height, font=controller.main_font,
                           command=lambda: controller.change_frame("Listening", {}))
        button.grid(row=2, column=0, padx=10, pady=controller.pady)

    def load(self, params):
        self.chosen_song['text'] = params['chosen_song_name']

    def afterLoad(self, params):
        return 1