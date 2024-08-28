sukupuoli = input("Syötä sukupuoli:").lower()
hemoglobiiniarvo = int(input("Syötä hemoglobiiniarvo:"))

if sukupuoli == "mies":
    if hemoglobiiniarvo < 134:
        print("Hemoglobiiniarvo on alhainen.")
    elif hemoglobiiniarvo > 195:
        print("Hemoglobiiniarvo on korkea.")
    else:
        print("Hemoglobiiniarvo on normaali.")

if sukupuoli == "nainen":
    if hemoglobiiniarvo < 117:
        print("Hemoglobiiniarvo on alhainen.")
    elif hemoglobiiniarvo > 175:
        print("Hemoglobiiniarvo on korkea.")
    else:
        print("Hemoglobiiniarvo on normaali.")