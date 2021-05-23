import socket
import threading
import tkinter as tk
import tkinter.scrolledtext
from tkinter import simpledialog
# Importer en masse lækre ting og sager som vi skal bruge til vores program.


FindHostename = socket.gethostname()
# Finder hostname.
HOST = socket.gethostbyname(FindHostename)
# Finder ip'en.
PORT = 65432
# Porten den lytter på (skal være over 1024).


class Client:
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        # Forbinder til en host og en port.

        bsk = tk.Tk()
        bsk.withdraw()
        # Vækker tkinter.

        self.kaldenavn = simpledialog.askstring("Kaldenavn", "Vælg dit kaldenavn", parent=bsk)
        # Beder om et kaldenavn til brugeren.

        self.gui_done = False
        self.levende = True
        # Referencepunkter som vi bruger senere ;)

        gui_thread = threading.Thread(target=self.gui)
        modtag_thread = threading.Thread(target=self.modtag)
        # Definer threading, så vi kan køre gui og modtag på samme tid.

        gui_thread.start()
        modtag_thread.start()
        # Påbegynder threading af gui og modtag.

    def gui(self):
        self.vin = tk.Tk()
        self.vin.configure(bg="lightgray")  # "vin er en forkortelse for "vindue."
        # Laver et vindue til chatten i farven "lightgray" (lysegrå på dansk).

        self.chat_etiket = tk.Label(self.vin, text="Chat", bg="lightgray")
        self.chat_etiket.config(font=("Arial", 12))
        self.chat_etiket.pack(padx=20, pady=5)
        # Skirver "Chat" i toppen af skærmen med fonten Arial og skriftstørrelse 12.

        self.tekst_omraade = tk.scrolledtext.ScrolledText(self.vin)
        self.tekst_omraade.pack(padx=20, pady=5)
        self.tekst_omraade.config(state="disabled")
        # Laver et tekst område med evnen til at scrolle, hvis det skulle blive nødvendigt :)
        # Dette er chattens hovedområde, hvor man kan se hvad man og andre har skrevet.

        self.bsk_etiket = tk.Label(self.vin, text="Besked", bg="lightgray")
        self.bsk_etiket.config(font=("Arial", 12))
        self.bsk_etiket.pack(padx=20, pady=5)
        # Skriver "Besked" under tekst omådet.

        self.input_omraade = tk.Text(self.vin, height=3)
        self.input_omraade.pack(padx=20, pady=5)
        # Laver et indput område, hvor man kan skrive sin besked inden man sender den.

        self.send_knap = tk.Button(self.vin, text="Send", command=self.skriv)
        self.send_knap.config(font=("Arial", 12))
        self.send_knap.pack(padx=20, pady=5)
        # Laver en knap til at sende sine beskeder. Den sender det, som står i input området.

        self.gui_done = True
        # Stadig noget vi bruger senere ;)

        self.vin.protocol("WM_DELETE_WINDOW", self.stop)
        # Stopper programmet, hvis man lukker gui'en.

        self.vin.mainloop()
        # Looper gui funktionen.

    def skriv(self):
        besked = f"{self.kaldenavn}: {self.input_omraade.get('1.0', 'end')}"
        # Definerer "besked" som brugerens kaldenavn og det, som står i input området.
        self.sock.send(besked.encode("utf-8"))
        # Sender en encoded besked til serveren.
        self.input_omraade.delete('1.0', 'end')
        # Fjerner al tekst fra input område.

    def stop(self):
        self.levende = False
        self.vin.destroy()
        self.sock.close()
        exit(0)
        # Hvis self.levende er False, luk vinduet, serverforbindelsen og programmet.
        # Brug exit code 0.

    def modtag(self):
        while self.levende:
            try:
                besked = self.sock.recv(1024).decode("utf-8")
                # Definer "besked" som noget modtaget information af 1024 bytes, som bliver decoded med utf-8.
                print(besked)
                # Print beskeden.
                if besked == "KALDENAVN":
                    self.sock.send(self.kaldenavn.encode("utf-8"))
                    # Hvis besked er "KALDENAVN," send brugerens kaldenavn til serveren, encoded med utf-8.
                elif self.gui_done:
                    self.tekst_omraade.config(state="normal")
                    self.tekst_omraade.insert("end", besked)
                    self.tekst_omraade.yview("end")
                    self.tekst_omraade.config(state="disabled")
                    # Ellers, hvis self.gui_done er True, indsæt besked i tekstområde med scrollcapabilities.
            except ConnectionAbortedError:
                break
                # Hvis der er en forbindelsesfejl, stop det while-loop.
            except:
                print("Fejl")
                self.sock.close()
                break
                # Hvis der er en fejl, som ikke er en forbindelsesfejl, skriv "Fejl," luk forbindelsen og
                # luk programmet.


client = Client(HOST, PORT)
# definer "client" som klassen Client, som modtager den host og port vi fandt i starten af programmet.
