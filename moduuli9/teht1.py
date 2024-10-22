class auto:
    def __init__(self, rekkari, huippunopeus):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu = 0


auto = auto("ABC-123", 142)

print(auto.rekkari)
print(auto.huippunopeus)
print(auto.nopeus)
print(auto.kuljettu)
