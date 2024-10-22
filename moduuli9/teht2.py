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

auto = auto("ABC-123", 142)

auto.kiihdyta(30)
auto.kiihdyta(70)
auto.kiihdyta(50)

print(auto.nopeus)

auto.kiihdyta(-200)

print(auto.nopeus)