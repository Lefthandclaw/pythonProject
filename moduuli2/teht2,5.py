e1 = float(input("Anna leiviskät: "))
e2 = float(input("Anna naulat: "))
e3 = float(input("Anna luodit: "))
grammat_e1 = e1 * 20 * 32 * 13.3
grammat_e2 = e2 * 32 * 13.3
grammat_e3 = e3 * 13.3

kaikkigrammat= grammat_e1 + grammat_e2 + grammat_e3
kilo= int(kaikkigrammat // 1000)
loputgrammat= kaikkigrammat % 1000
print("Massa nykymittojen mukaan:")
print(f"{kilo} kilogrammaa ja {loputgrammat:.2f} grammaa.")
