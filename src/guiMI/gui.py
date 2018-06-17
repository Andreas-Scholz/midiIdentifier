import tkinter as tk
from tkinter import font as tkfont
from tkinter import ttk
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

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.bg = "SlateGray3"

        container = tk.Frame(self,background=self.bg)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Listening, Processing, Choose, Playing, Choose_input, Choose_output, Canvas):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.configure(background=self.bg)
            frame.grid(row=0, column=0, sticky="")

        self.change_frame("Canvas", {})
        self.change_frame("Choose_input", {})

    def change_frame(self, page_name, params):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        canv = self.frames["Canvas"]
        frame.load(params)
        canv.tkraise()
        frame.tkraise()
        self.update()
        frame.afterLoad(params)


if __name__ == "__main__":
    app = Gui()
    #app.style = ttk.Style()
    #app.style.theme_use("clam")
    app.attributes('-fullscreen', True)
    print(app.tk.call('ttk::themes'))
    app.mainloop()
