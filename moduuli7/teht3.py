kentät = {}

while True:
    syöte = int(
        input("Haluatko syöttää uuden lentoaseman(1), hakea jo syötetyn lentoaseman tiedot(2) vai lopettaa(3)?: "))

    if syöte == 1:
        ICAO = input("Lentoaseman ICAO-koodi: ")
        nimi = input("Lentoaseman nimi: ")
        kentät[ICAO] = nimi

    elif syöte == 2:
        haku = input("ICAO-koodi: ")
        if haku in kentät:
            print(f"{kentät[haku]}")

    elif syöte == 3:
        break
