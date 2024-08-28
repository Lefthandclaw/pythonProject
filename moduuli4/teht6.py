import random

while True:
    pistemäärä = int(input("Anna arvottavien pisteiden määrä:"))

    if pistemäärä > 0:
        ympyränsisällä = 0

        for _ in range(pistemäärä):
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)

            if x ** 2 + y ** 2 < 1:
                    ympyränsisällä += 1

        piinarvo = 4 * ympyränsisällä / pistemäärä
        print(f"Piin likiarvo on {piinarvo:.6f}")
        break
