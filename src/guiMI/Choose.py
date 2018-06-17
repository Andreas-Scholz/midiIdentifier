from tkinter import *

class Choose(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        rowc = 0
        label = Label(self, text="Welchen Song meintest du?", font=controller.title_font, background=controller.bg)
        label.grid(row=rowc, column=0, padx=10, pady=30)
        rowc += 1

        # Variables accessible by all frames
        songs = {1: 'Britney Spears - I\'m fat', 2: 'Melania Trump - Help', 3: 'Donald Trump - Grab \'em by the pussy',
                 4: 'Bon Jovi - Still not dead', 5: 'Karsten Schick - A man with no prejudices'}

        for key, value in songs.items():
            song_button = Button(self, text=value, width=controller.button_width, height=controller.button_height, font=controller.main_font,
                                    command=lambda key=key, value=value: self.choose(controller, key, value))
            song_button.grid(row=rowc, column=0, padx=10, pady=controller.pady)
            rowc += 1

        button = Button(self, text="<-- Reset",
                           command=lambda: controller.change_frame("Listening", {}))
        button.grid(row=rowc + 1, column=0, padx=10, pady=3)

    def load(self, params):
        return 1

    def afterLoad(self, params):
        return 1

    def choose(self, controller, id, name):
        controller.change_frame("Playing", {'chosen_song_id': id, 'chosen_song_name': name})