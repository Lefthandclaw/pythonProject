nimet = set()

while True:
    nimi = input("Syötä nimejä:")

    if nimi == "":
        break

    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        nimet.add(nimi)
        print("Uusi nimi")

for nimi in nimet:
    print(nimi)