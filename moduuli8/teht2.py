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


def hae_lentokentan_tiedot(maakoodi):
    sql = f"SELECT type, COUNT(*) FROM airport WHERE iso_country = '{maakoodi}' GROUP BY type"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if tulos:
        for tyyppi, maara in tulos:
            print(f"{tyyppi.capitalize()} lentokenttiä: {maara}")
    return


maakoodi = input("Anna maakoodi: ").upper()
hae_lentokentan_tiedot(maakoodi)
