kuukaudet = (
"tammikuu", "helmikuu", "maaliskuu", "huhtikuu", "toukokuu", "kesäkuu", "heinäkuu", "elokuu", "syyskuu", "lokakuu",
"marraskuu", "joulukuu")
kuukausinumero = int(input("Kuukauden numero: "))

kuu = kuukaudet[kuukausinumero - 1]

if kuukausinumero in (1, 2, 12):
    print("Talvi")

if kuukausinumero in (3, 4, 5):
    print("kevät")

if kuukausinumero in (6, 7, 8):
    print("Kesä")

if kuukausinumero in (9, 10, 11):
    print("Syksy")
