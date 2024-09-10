import mysql.connector

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
    sql = f"SELECT name, municipality FROM airport WHERE ident = '{icao}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()
    if tulos:
        lentokentan_nimi, sijaintikunta = tulos
        print(lentokentan_nimi + ", " + sijaintikunta)
    return


icao = input("Anna ICAO-koodi: ").upper()
hae_lentokentan_tiedot(icao)
