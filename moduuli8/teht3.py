import mysql.connector
from geopy.distance import great_circle

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='mostafa',
    password='123123',
    collation='utf8mb4_unicode_ci',
    autocommit=True
)


def hae_lentokentan_tiedot(icao):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{icao}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()
    return tulos


icao1 = input("Anna ICAO 1: ").upper()
icao2 = input("Anna ICAO 2: ").upper()

koordinaatit1 = hae_lentokentan_tiedot(icao1)
koordinaatit2 = hae_lentokentan_tiedot(icao2)

if koordinaatit1 and koordinaatit2:
    etaisyys = great_circle(koordinaatit1, koordinaatit2).kilometers
    print(f"Lentokenttien etäisyys on {etaisyys:.2f} kilometriä.")
