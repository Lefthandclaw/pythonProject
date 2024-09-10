def bensiini():
    return float(input("Syötä bensiini määrä nestegallonoina: "))


def ohjelma():
    määrä = bensiini()

    while määrä > 0:
        print(f"bensiini on {määrä * 3.785}")
        määrä = bensiini()


ohjelma()
