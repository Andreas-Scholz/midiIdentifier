from tkinter import *
import threading
import time
from midiSourceMI.piano import Piano

class Listening(Frame):

    def __init__(self, parent, controller, params):
        Frame.__init__(self, parent)
        self.controller = controller

        label = Label(self, text="", font=controller.title_font, background=controller.bg, foreground=controller.fg, anchor="w", width=15)
        label.grid(row=0, column=0, padx=10, pady=30)

        final_string = "> PLAY A SONG:"
        delta = controller.delta
        delay = 0
        for i in range(len(final_string) + 1):
            s = final_string[:i]
            update_text = lambda s=s: label.config(text=s)
            label.after(delay, update_text)
            delay += delta

        label2 = Label(self, text="", font=controller.title_font, background=controller.bg, foreground=controller.prompt, anchor="w", width=15)
        label2.grid(row=1, column=0, padx=10, pady=30)

        final_string = "> PROGRESS:"
        for i in range(len(final_string) + 1):
            s = final_string[:i]
            update_text = lambda s=s: label2.config(text=s)
            label2.after(delay, update_text)
            delay += delta

        self.status = Label(self, text="", font=controller.title_font, background=controller.bg, foreground=controller.bg, anchor="w", width=15)
        self.status.grid(row=1, column=1, padx=10, pady=controller.pady)
        show_status = lambda: self.status.config(foreground=controller.prompt)
        self.status.after(delay, show_status)

    def load(self, controller, params):
        return 1

    def afterLoad(self, controller, params):
        piano = Piano(controller.input)

        pianoThread = threading.Thread(target=piano.listen)
        # progressThread = threading.Thread(target=print_progress)

        print("Starting piano thread")
        pianoThread.start()
        while not piano.is_done():
            time.sleep(1)
            print("Progress: {}%".format(piano.get_progress()))
            self.status['text'] = "{}%".format(piano.get_progress())
            self.update()
        pianoThread.join()
        self.status['text'] = "DONE"
        self.update()
        #midi = piano.get_midi_list()
        midi = piano.get_midi()
        midi_list = piano.get_midi_list()
        #del piano
        controller.change_frame("Choose", {'midi':midi, 'midi_list':midi_list})