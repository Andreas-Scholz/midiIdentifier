from tkinter import *
from comparatorMI import compare
import functools

class Choose(Frame):
    def __init__(self, parent, controller, params):
        Frame.__init__(self, parent)
        self.controller = controller
        rowc = 0

        label = Label(self, text="", font=controller.title_font, background=controller.bg, foreground=controller.fg, anchor="w", width=controller.label_width)
        label.grid(row=rowc, column=0, padx=10, pady=30)

        final_string = "> Which song did you mean?"
        delta = controller.delta
        delay = 0
        for i in range(len(final_string) + 1):
            s = final_string[:i]
            update_text = lambda s=s: label.config(text=s)
            label.after(delay, update_text)
            delay += delta

        rowc += 1

        #archive = compare.getListArchive()
        #matches = compare.compare2(params['midi'], archive)
        print(params['midi_list'])
        archive = compare.getArchive()
        list_archive = compare.getListArchive()
        matches = compare.compare(params['midi'], archive)
        matches_lev = compare.levenshtein(params['midi'], archive)
        matches_count = compare.compare2(params['midi_list'], list_archive)

        for pair in matches:
            key = pair[1]
            value = pair[0]
            song_button = Label(self, text="", font=controller.title_font, background=controller.bg, foreground=controller.prompt, anchor="nw", width=controller.label_width)
            song_button.grid(row=rowc, column=0, padx=10, pady=controller.pady)
            song_button.bind("<Button-1>",lambda key=key, value=value: self.choose(controller, key, value))
            display_value = value.replace(".mid", "")
            final_string = "> " + display_value
            for i in range(len(final_string) + 1):
                s = final_string[:i]
                song_button.after(delay, functools.update_wrapper( functools.partial(song_button.config, text=s), song_button.config))
                delay += delta
            rowc += 1

        # button = Button(self, text="<-- Reset", width=controller.button_width, height=controller.button_height, font=controller.main_font,
        #                    command=lambda: controller.change_frame("Listening", {}))
        # button.grid(row=rowc + 1, column=0, padx=10, pady=3)
        button = Label(self, text="", font=controller.title_font, background=controller.bg, foreground=controller.prompt, anchor="w", width=controller.label_width)
        button.grid(row=rowc, column=0, padx=10, pady=controller.pady)
        button.bind("<Button-1>", self.reset, controller)
        final_string = "> Reset"
        for i in range(len(final_string) + 1):
            s = final_string[:i]
            button.after(delay, functools.update_wrapper( functools.partial(button.config, text=s), button.config))
            delay += delta

    def reset(self, controller):
        self.controller.change_frame("Listening", {})

    def load(self, controller, params):
        return 1

    def afterLoad(self, controller, params):
        return 1

    def choose(self, controller, id, name):
        controller.change_frame("Playing", {'chosen_song_id': id, 'chosen_song_name': name})