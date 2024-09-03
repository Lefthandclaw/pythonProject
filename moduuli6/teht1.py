import random

noppa = []

while noppa != 6:
    def noppaheitto():
        return random.randint(1, 6)


    noppa = noppaheitto()
    print(noppa)
