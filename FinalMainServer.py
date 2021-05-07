import socket
import threading

FindHosteNavn = socket.gethostname() #finder hostnavnet
Host = socket.gethostbyname(FindHosteNavn) #finder ip'en ud fra hostnavnet
Port = 65432 #port den lytter på (skal være over 1024)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(Host, Port)

server.listen()

Clienter = []
Kaldenavne = []


#Udgåender beskeder, sender beskeder til alle
def udgaaender(besked):
    for client in Clienter:
        client.send(besked)

#Chefen, Modtager alle beskeder og håntere/veligeholder forbindelsen til clienterne
def chefen():
    pass

#Modtager, modtager clientens forespørsel om at joine servern
def modtager():
    while True:
        client, adrasse = server.accept()
        print(f"Forbundet med {str(adrasse)},tillykke!")

        client.send("KALDENAVN".encode('utf-8'))
        kaldenavn = client.recv(1024)
        Kaldenavne.append(kaldenavn)
        Clienter.append(client)

        print(f"Clientens kladenavn er {kaldenavn}, altså, det kunde være værrere")
        broadcarst(f"{kaldenavn} har nu joinet servern, så held og lykke\n".encode("utf-8"))
        client.send("Velkommen til servern, hold den ordentlige tone, eller ikke, jeg er ligeglad.\n Dog skal du hygge dig, det er en regl".encode("utf-8"))

        thread = threading.Thread(target=chefen(), args=(client,))
        thread.start()