from tkinter import *
from comparatorMI import compare

class Choose(Frame):
    def __init__(self, parent, controller, params):
        Frame.__init__(self, parent)
        self.controller = controller
        rowc = 0
        label = Label(self, text="Welchen Song meintest du?", font=controller.title_font, background=controller.bg, foreground=controller.fg)
        label.grid(row=rowc, column=0, padx=10, pady=30)
        rowc += 1

        #archive = compare.getListArchive()
        #matches = compare.compare2(params['midi'], archive)
        print(params['midi_list'])
        archive = compare.getArchive()
        list_archive = compare.getListArchive()
        matches = compare.compare(params['midi'], archive)
        matches_lev = compare.levenshtein(params['midi'], archive)
        matches_count = compare.compare2(params['midi_list'], list_archive)

        for value, key in matches.items():
            key = str(key)
            song_button = Button(self, text=value+' ('+key+')', width=controller.button_width, height=controller.button_height, font=controller.main_font,
                                    command=lambda key=key, value=value: self.choose(controller, key, value))
            song_button.grid(row=rowc, column=0, padx=10, pady=controller.pady)
            rowc += 1

        button = Button(self, text="<-- Reset", width=controller.button_width, height=controller.button_height, font=controller.main_font,
                           command=lambda: controller.change_frame("Listening", {}))
        button.grid(row=rowc + 1, column=0, padx=10, pady=3)

    def load(self, controller, params):
        return 1

    def afterLoad(self, controller, params):
        return 1

    def choose(self, controller, id, name):
        controller.change_frame("Playing", {'chosen_song_id': id, 'chosen_song_name': name})