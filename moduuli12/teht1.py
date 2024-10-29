import requests

linkki = "https://api.chucknorris.io/jokes/random"
vastaus = requests.get(linkki)

if vastaus.status_code == 200:
    data = vastaus.json()
    print(data.get("value"))
