import socket
import threading
import tkinter as tk
import tkinter.scrolledtext
from tkinter import simpledialog

HOST = "127.0.0.1"
PORT = 9090


class Client:
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

        bsk = tk.Tk()
        bsk.withdraw

        self.kaldenavn = simpledialog.askstring("Kaldenavn", "Vælg dit kaldenavn", parent=bsk)

        self.gui_done = False

        self.levende = True

        gui_thread = threading.Thread(target=self.gui)
        modtag_thread = threading.Thread(target=self.modtag)

        gui_thread.start()
        modtag_thread.start()

    def gui(self):
        self.vin = tk.Tk()
        self.vin.configure(bg="lightgray")

        self.chat_etiket = tk.Label(self.vin, text="Chat", bg="lightgray")
        self.chat_etiket.config(font=("Arial", 12))
        self.chat_etiket.pack(padx=20, pady=5)

        self.tekst_omraade = tk.scrolledtext.ScrolledText(self.vin)
        self.tekst_omraade.pack(padx=20, pady=5)
        self.tekst_omraade.config(state="disabled")

        self.bsk_etiket = tk.Label(self.vin, text="Besked", bg="lightgray")
        self.bsk_etiket.config(font=("Arial", 12))
        self.bsk_etiket.pack(padx=20, pady=5)

        self.input_omraade = tk.Text(self.vin, height=3)
        self.input_omraade.pack(padx=20, pady=5)

        self.send_knap = tk.Button(self.vin, text="Send", command=self.skriv)
        self.send_knap.config(font=("Arial", 12))
        self.send_knap.pack(padx=20, pady=5)

        self.gui_done = True

        self.vin.protocol("WM_DELETE_WINDOW", self.stop)

        self.vin.mainloop()

    def skriv(self):
        besked = f"{self.kaldenavn}: {self.input_omraade.get('1.0', 'end')}"
        self.sock.send(besked.encode("utf-8"))
        self.input_omraade.delete('1.0', 'end')

    def stop(self):
        self.levende = False
        self.vin.destroy()
        self.sock.close()
        exit(0)

    def modtag(self):
        while self.levende:
            try:
                besked = self.sock.recv(1024)
                if besked == "NICK":
                    self.sock.send(self.kaldenavn.encode("utf-8"))
                elif self.gui_done:
                    self.tekst_omraade.config(state="normal")
                    self.tekst_omraade.insert("end", besked)
                    self.tekst_omraade.yview("end")
                    self.tekst_omraade.config(state="disabled")
            except ConnectionAbortedError:
                break
            except:
                print("Fejl")
                self.sock.close()
                break

client = Client(HOST, PORT)
