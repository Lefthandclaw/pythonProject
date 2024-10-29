class auto:
    def __init__(self, rekkari, huippunopeus):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu = 0

    def kiihdyta(self, muutos):
        uusinopeus = self.nopeus + muutos

        if uusinopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif uusinopeus < 0:
            self.nopeus = 0
        else:
            self.nopeus = uusinopeus

    def kulje(self, tunti):
        matka = self.nopeus * tunti
        self.kuljettu += matka

class sähköauto(auto):
    def __init__(self, rekkari, huippunopeus, akku):
        super().__init__(rekkari, huippunopeus)
        self.akku = akku

class polttomoottoriauto(auto):
    def __init__(self, rekkari, huippunopeus, tankki):
        super().__init__(rekkari, huippunopeus)
        self.tankki = tankki

sähkö = sähköauto("ABC-15", 180, 52.5)
polttomoottori = polttomoottoriauto("ACD-123", 165, 32.5)

sähkö.kiihdyta(69)
polttomoottori.kiihdyta(69)

sähkö.kulje(3)
polttomoottori.kulje(3)

print(f"Sähköauto kulkenu {sähkö.kuljettu} km")
print(f"Polttomoottoriauto kulkenu {polttomoottori.kuljettu} km")