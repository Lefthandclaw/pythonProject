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

autot = []

for i in range(1,11):
    rekkari = f"ABC-{i}"
    huippunopeus = random.randint(100, 200)
    autot.append(auto(rekkari, huippunopeus))

kilpailu = True
while kilpailu:
    for auto in autot:
        muutos = random.randint(-10, 15)
        auto.kiihdyta(muutos)

        auto.kulje(1)

        if auto.kuljettu >= 10000:
            kilpailu = False
            break

print(f"{'Rekkari':<10}{'Huippunopeus km/h':<20}{'Nopeus km/h':<15}{'Kuljettu matka (km)':<20}")
print("-" * 70)
for auto in autot:
    print(f"{auto.rekkari:<10}{auto.huippunopeus:<20}{auto.nopeus:<15}{auto.kuljettu:<20.1f}")