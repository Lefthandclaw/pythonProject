numbers = []

num= ""

while num != " ":
    num = input("Syötä lukuja ja lopuksi tyhjän merkkijonon:")

    if num !=" ":
        number = int(num)
        numbers.append(number)

print("Pienin numero:", min(numbers))
print("Suurin numero:", max(numbers))