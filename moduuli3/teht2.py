hytluokka = input("Syötä hyttiluokka (LUX, A, B, C):")

if hytluokka == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif hytluokka == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif hytluokka == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif hytluokka == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka.")