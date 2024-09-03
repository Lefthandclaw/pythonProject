def summa(lista):
    uusi_lista = []
    for luku in lista:
        if luku % 2 == 0:
            uusi_lista.append(luku)

    return uusi_lista

def ohjelma():


    luku_lista = [1, 2, 3, 4, 5]
    tulos = summa(luku_lista)
    print(tulos)
    print(luku_lista)

ohjelma()