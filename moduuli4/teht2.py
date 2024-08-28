num = 0

while num >= 0:
    num = int(input("Syötä tuumat: "))

    vastaus = num * 2.54

    if vastaus >= 0:
        print(f"{vastaus} tuumaa")
