import sys
sys.path.append('../')
import tkinter as tk
from tkinter import font as tkfont
from guiMI.Canvas import Canvas
from guiMI.Listening import Listening
from guiMI.Processing import Processing
from guiMI.Choose import Choose
from guiMI.Playing import Playing
from guiMI.Choose_input import Choose_input
from guiMI.Choose_output import Choose_output

class Gui(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Courier', size=24, weight="bold")
        self.bg = "black"
        self.fg = "white"
        self.prompt = "SpringGreen2"
        self.main_font = tkfont.Font(family='Courier', size=16, weight='bold')
        self.pady = 10
        self.button_width = 60
        self.button_height = 1
        self.label_width = 50
        self.delta = 100

        self.container = tk.Frame(self,background=self.bg)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.input = None
        self.output = None

        self.frames = {}
        #for F in (Listening, Processing, Choose, Playing, Choose_input, Choose_output, Canvas):
        #    page_name = F.__name__
        #    frame = F(parent=self.container, controller=self)
        #    self.frames[page_name] = frame
        #    frame.configure(background=self.bg)
        #    frame.grid(row=0, column=0, sticky="n")

        #self.change_frame("Canvas", {})
        #self.change_frame("Choose_input", {})
        self.current_frame = Canvas(parent=self.container, controller=self)
        self.current_frame.configure(background=self.bg)
        self.current_frame.grid(row=0, column=0, sticky="n")
        self.change_frame('Choose_input', {})

    #def change_frame(self, page_name, params):
    #    '''Show a frame for the given page name'''
    #    frame = self.frames[page_name]
    #    canv = self.frames["Canvas"]
    #    frame.load(self, params)
    #    canv.tkraise()
    #    frame.tkraise()
    #    self.update()
    #    frame.afterLoad(self, params)

    def change_frame(self, type, params):
        if(type == 'Choose'):
            type_loaded = Choose
        if(type == 'Choose_input'):
            type_loaded = Choose_input
        if(type == 'Choose_output'):
            type_loaded = Choose_output
        if(type == 'Listening'):
            type_loaded = Listening
        if(type == 'Playing'):
            type_loaded = Playing
        if(type == 'Processing'):
            type_loaded = Processing
        self.current_frame.grid_forget()
        self.current_frame.destroy()
        self.current_frame = type_loaded(parent=self.container, controller=self, params=params)
        self.current_frame.configure(background=self.bg)
        self.current_frame.grid(row=0, column=0, sticky="nw")
        self.current_frame.tkraise()
        self.current_frame.load(self, params)
        self.current_frame.afterLoad(self, params)

if __name__ == "__main__":
    app = Gui()
    #app.style = ttk.Style()
    #app.style.theme_use("clam")
    app.geometry("1024x600")
    app.attributes('-fullscreen', True)
    app.mainloop()
