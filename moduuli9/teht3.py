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

auto = auto("ABC-123", 142)

auto.kiihdyta(60)

auto.kulje(1.5)

print(auto.nopeus)
print(auto.kuljettu)