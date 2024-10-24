class hissi:
    def __init__(self,alempikerros, ylempikerros):
        self.alempikerros = alempikerros
        self.ylempikerros = ylempikerros
        self.nykykerros = alempikerros

    def kerrosylös(self):
        if self.nykykerros < self.ylempikerros:
            self.nykykerros += 1

    def kerrosalas(self):
        if self.nykykerros > self.alempikerros:
            self.nykykerros -= 1

    def siirrykerros(self, kerros):
        if kerros < self.alempikerros or kerros > self.ylempikerros:
            return

        while self.nykykerros < kerros:
            self.kerrosylös()
        while self.nykykerros > kerros:
            self.kerrosalas()

tasot = hissi(1, 10)

tasot.siirrykerros(3)
print(tasot.nykykerros)

tasot.siirrykerros(1)
print(tasot.nykykerros)
