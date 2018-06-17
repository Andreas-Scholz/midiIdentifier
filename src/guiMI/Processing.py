from tkinter import *
import compare

class Processing(Frame):

    def __init__(self, parent, controller, params):
        Frame.__init__(self, parent)
        self.controller = controller
        rowc = 0
        self.matches = {}

        label = Label(self, text="Processing-Tab", font=controller.title_font, background=controller.bg)
        label.grid(row=rowc, column=0, padx=10, pady=30)
        button = Button(self, text="<-- Reset", width=int(controller.button_width/2), height=controller.button_height, font=controller.main_font,
                           command=lambda: controller.change_frame("Listening", {}))
        rowc += 1

        button.grid(row=rowc, column=0, padx=10, pady=3)
        button2 = Button(self, text="Choose -->", width=int(controller.button_width/2), height=controller.button_height, font=controller.main_font,
                            command=lambda: controller.change_frame("Choose", {}))
        button2.grid(row=rowc, column=2, padx=10, pady=3)
        rowc += 1

        for key, value in self.matches.items():
            song_button = Button(self, text=value, width=controller.button_width, height=controller.button_height, font=controller.main_font,
                                 command=lambda key=key, value=value: self.choose(controller, key, value))
            song_button.grid(row=rowc, column=0, padx=10, pady=controller.pady)
            rowc += 1

    def load(self, controller, params):
        archive = compare.getArchive()
        self.matches = compare.compare(params['midi'], archive)
        self.update()


    def afterLoad(self, controller, params):
        return 1