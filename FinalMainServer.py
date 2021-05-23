import socket
import threading

FindHosteNavn = socket.gethostname() #finder hostnavnet
Host = socket.gethostbyname(FindHosteNavn) #finder ip'en ud fra hostnavnet
Port = 65432 #port den lytter på (skal være over 1024)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((Host, Port))

server.listen()#bruger sockets lytte funktion til at lytte efter aktivitet på host og port
Clienter = []
Kaldenavne = []


#Udgåender beskeder, sender beskeder til alle
def udgaaender(besked):
    for client in Clienter:
        client.send(besked)


#Chefen, Modtager alle beskeder og håntere/veligeholder forbindelsen til clienterne
def chefen(client):
    while True:
        try:
            besked = client.recv(1024)
            print(f"{Kaldenavne[Clienter.index(client)]} skriver {besked}\n")
            udgaaender(besked)
        except:
            index = Clienter.index(client)
            Clienter.remove(client)
            kaldenavn = Kaldenavne[index]
            print(f"{kaldenavn} har forladt serveren")
            udgaaender(f"{kaldenavn} har forladt serveren, så i må klare jeg uden.\nHELD OG LYKKE!!!")
            Kaldenavne.remove(kaldenavn)
            #Kaldenavne.pop(kaldenavn) #bør måske virke bedre
            break


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
        udgaaender(f"{kaldenavn} har nu joinet servern, så held og lykke\n".encode("utf-8"))
        client.send("Velkommen til servern, hold den ordentlige tone, eller ikke, jeg er ligeglad.\nDog skal du hygge dig, det er en regl".encode("utf-8"))

        thread = threading.Thread(target=chefen, args=(client,))
        thread.start()
print(f"servern køre...\nVentet på clienter")
modtager()