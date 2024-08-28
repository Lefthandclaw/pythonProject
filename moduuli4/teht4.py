import random

rnumero1 = random.randint(1, 10)

luku = 0

while luku != rnumero1:
    luku = int(input("Syötä luku:"))

    if luku < rnumero1:
        print("Liian pieni arvaus")
    elif luku > rnumero1:
        print("Liian suuri arvaus")
    elif luku == rnumero1:
        print("Oikein")