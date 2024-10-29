import requests
import json

paikkakunta = input("Anna paikkakunta: ")
api = "ae3e1dc3d0f2ba6d742d28cad8600293"
linkki = f"https://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&appid={api}"

response = requests.get(linkki)

if response.status_code == 200:
    data = response.json()
    sää = data["weather"][0]["description"]
    lämpötila = data["main"]["temp"]
    lämpötilacelcius = lämpötila - 273.15

    print(f"Säätila {sää}")
    print(f"Lämpötila {lämpötilacelcius}")