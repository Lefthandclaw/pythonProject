numbers = []

num = ""

while num != " ":
    num = input("Syötä lukuja ja lopuksi tyhjän merkkijonon:")

    if num != " ":
        number = int(num)
        numbers.append(number)

numbers.sort(reverse=True)

for num in numbers[:5]:
    print(num)
