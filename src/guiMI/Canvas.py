from tkinter import *
import tkinter as tk
from audioMI import devices

class Canvas(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        canv = tk.Canvas(self,width=1024, height=600)
        canv.create_rectangle(0, 0, 1024, 600, fill=controller.bg)
        canv.grid(row=0, column=0, sticky="")

    def load(self, params):
        return 1

    def afterLoad(self, params):
        return 1

    def choose(self, controller, id, name):
        return 1