def kryptering(ord,key):
    # Vi indsætter alfabetet som en liste, som vi leder i senere koden.
    alfabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','Æ','Ø','Å']

    # n er længden på det input, vi indsætter som skal krypteres.
    n = len(ord)

    # Vores output er en tom string, som der bliver skrevet i senere
    output=""

    #Tælleren i er 0, så den starter fra første bogstav.
    i=0
    while i<n:
        #Så længe i er større end n, så finder vi pladsen/ indexet for hvert bogstav i det ord, vi skriver ind som skal krypteres.
        ukrypteretIndex = alfabet.index(ord[i].upper())

        # Her lægger vi key'en til det ukrypteret index og bruger modolo af længden af alfabetet for at den starter forfra efter å.
        krytperetIndex = (ukrypteretIndex + key) % len(alfabet)

        # Den tomme streng (vores output) bliver lagt til det krypteret index af alfabetet.
        output += alfabet[krytperetIndex]

        # Til sidst lægger vi 1 til i og så starter loopet forfra igen.
        i += 1
    return output


def dekryptering(ord,key):
    #Vi indsætter alfabetet som en liste, som vi leder i senere koden.
    alfabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','Æ','Ø','Å']

    #n er længden på det input, vi indsætter som skal dekrypteres.
    n = len(ord)

    #Vores output er en tom string, som der bliver skrevet i senere
    output = ""

    #Tælleren i er 0, så den starter fra start.
    i = 0
    while i<n:
        #Så længe i er større end n, så finder vi pladsen/ indexet for hvert bogstav i det ord, vi skriver ind som skal dekrypteres.
        ukrypteretIndex = alfabet.index(ord[i].upper())

        #Her lægger vi key'en til det ukrypteret index og bruger modolo af længden af alfabetet for at den starter forfra efter å.
        krytperetIndex = (ukrypteretIndex + key) % len(alfabet)

        #Den tomme streng (vores output) bliver lagt til det krypteret index af alfabetet.
        output += alfabet[krytperetIndex]

        #Til sidst lægger vi 1 til i og så starter loopet forfra igen.
        i+=1
    return output

#Her indsættes det ord, som skal krypteres og en key-længde.
print(kryptering('eow',3))

#Her indsættes det krypterede ord og en key-længde, som er i minus fordi vi dekrypterer nu.
print(dekryptering('sw',-8))