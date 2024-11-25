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

class talo:
    def __init__(self,alempikerros, ylempikerros, hissit):
        self.alempikerros = alempikerros
        self.ylempikerros = ylempikerros
        self.hissit = [hissi(alempikerros, ylempikerros) for _ in range(hissit)]

    def aja_hissiä(self, hissinumero, kohde):
        if 0 <= hissinumero < len(self.hissit):
            self.hissit[hissinumero].siirrykerros(kohde)

    def palohälytys(self):
        for hissi in self.hissit:
            hissi.siirrykerros(self.alempik   erros)

talohissit = talo(1, 10, 3)

talohissit.aja_hissiä(0, 5)
print(talohissit.hissit[0].nykykerros)

talohissit.aja_hissiä(1, 7)
print(talohissit.hissit[1].nykykerros)

talohissit.aja_hissiä(2, 4)
print(talohissit.hissit[2].nykykerros)

talohissit.palohälytys()
print(talohissit.hissit[0].nykykerros)
print(talohissit.hissit[1].nykykerros)
print(talohissit.hissit[2].nykykerros)