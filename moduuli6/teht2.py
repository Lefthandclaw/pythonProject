import random

noppa = []

tahkot = int(input("Nopan tahkojen yhteismäärä:"))

while noppa != tahkot:
    def noppaheitto():
        return random.randint(1, tahkot)
    noppa = noppaheitto()
    print(noppa)
