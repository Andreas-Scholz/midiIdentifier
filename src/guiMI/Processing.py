from tkinter import *

class Processing(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Processing-Tab", font=controller.title_font, background=controller.bg)
        label.grid(row=0, column=0, padx=10, pady=3)
        button = Button(self, text="<-- Reset",
                           command=lambda: controller.change_frame("Listening", {}))
        button.grid(row=1, column=0, padx=10, pady=3)
        button2 = Button(self, text="Choose -->",
                            command=lambda: controller.change_frame("Choose", {}))
        button2.grid(row=1, column=2, padx=10, pady=3)

    def load(self, params):
        return 1

    def afterLoad(self, params):
        return 1