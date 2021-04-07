import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *

class Brugerflade(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.adgangskode()
        #self.chatrum()

    def adgangskode(self):
        self.luk = tk.Button(self, text="Luk", fg="red", command=self.master.destroy)
        self.luk.pack(side="right")

root = tk.Tk()
root.title("Chatrum")
app = Brugerflade(master=root)
app.mainloop()