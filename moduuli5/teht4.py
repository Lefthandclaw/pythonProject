kaupunki_lista = []

for i in range(1, 6):
    kaupungit = input(f"Syötä kaupungin nimi {i}:")
    kaupunki_lista.append(kaupungit)

for kaupungit in kaupunki_lista:
    print(kaupungit)
