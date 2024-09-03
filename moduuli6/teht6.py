import math


def pizza(halkaisija, hinta):
    sade = halkaisija / 2
    pintaala = math.pi * sade ** 2
    yksikköhinta = pintaala / hinta
    return yksikköhinta


def ohjelma():
    halkaisija = float(input("Pizza 1 halkaisija senttimetreinä:"))
    halkaisija2 = float(input("Pizza 2 halkaisija senttimetreinä:"))

    hinta = float(input("Pizza 1 hinta:"))
    hinta2 = float(input("Pizza 2 hinta:"))

    yksikköhinta = pizza(halkaisija, hinta)
    yksikköhinta2 = pizza(halkaisija2, hinta2)
    if yksikköhinta2 < yksikköhinta:
        print("Pizza 2 on parempi vastine rahalle.")
    elif yksikköhinta2 > yksikköhinta:
        print("Pizza 1 on parempi vastine rahalle.")


ohjelma()
