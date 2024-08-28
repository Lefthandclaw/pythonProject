yritys = 0

while yritys < 5:
    ktunnus = input("Syötä käyttäjätunnus:")
    salasana = input("Syötä salasana:")

    if ktunnus != "python" or salasana != "rules" :
        print("Väärin.")
        yritys+= 1
    else:
        print("Tervetuloa")
        break

if yritys == 5:
    print("Pääsy evätty")
