import random

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

class kilpailu:
    def __init__(self, nimi, pituuskm, autot):
        self.nimi = nimi
        self.pituuskm = pituuskm
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            muutos = random.randint(-10, 15)
            auto.kiihdyta(muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"{'Rekkari':<10}{'Huippunopeus km/h':<20}{'Nopeus km/h':<15}{'Kuljettu matka (km)':<20}")
        print("-" * 70)
        for auto in autot:
            print(f"{auto.rekkari:<10}{auto.huippunopeus:<20}{auto.nopeus:<15}{auto.kuljettu:<20.1f}")

    def kilpailu_ohi(self):
        for auto in autot:
            if auto.kuljettu >= self.pituuskm:
                return True
        return False

autot = []

for i in range(1,11):
    rekkari = f"ABC-{i}"
    huippunopeus = random.randint(100, 200)
    autot.append(auto(rekkari, huippunopeus))

kilpailu = kilpailu("Suuri romuralli", 8000, autot)

tunnit = 0
while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunnit = tunnit + 1

    if tunnit % 10 == 0:
        print(f"Tunti {tunnit}")
        kilpailu.tulosta_tilanne()

print(f"Kilpailu ohi, tunti {tunnit}")
kilpailu.tulosta_tilanne()