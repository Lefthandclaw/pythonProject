luku = int(input("Syötä kokonaisluku:"))

for i in range(2, int(luku ** 0.5) + 1):
    if luku % i == 0:
        print("Luku ei ole alkuluku.")
        break
else:
    print("Luku on alkuluku.")
