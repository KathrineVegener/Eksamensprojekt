import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *


class mainWindow:
    def __init__(self):
        self.root = Tk()

        chatnavn = Label(self.root, text="Chatrummet")
        chatnavn.pack(pady=10)

        

        # infinite loop
        mainloop()

if __name__ == '__main__':
    main = mainWindow()
