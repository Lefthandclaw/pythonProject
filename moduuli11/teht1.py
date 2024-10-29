class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        print(f"Kirja: {self.nimi}, Kirjoittaja: {self.kirjoittaja}, Sivumäärä: {self.sivumaara}")

class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        print(f"Lehti: {self.nimi}, Päätoimittaja: {self.paatoimittaja}")

akuankka = Lehti("Aku ankka", "Aki hyyppä")
hyttino6 = Kirja("Hytti n:o 6", "Rosa Liksom", "200 sivua")

akuankka.tulosta_tiedot()
hyttino6.tulosta_tiedot()