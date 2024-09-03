import random

kuutiot = int(input("Arpakuutioiden lukumäärä:"))

summa = 0

for i in range(kuutiot):
    summa += random.randint(1, 6)

print(f"silmälukujen summan {summa}")
