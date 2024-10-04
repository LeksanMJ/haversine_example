import requests
def get_coordinates(address: str) -> list:
    URL = "https://api-adresse.data.gouv.fr/search/?q="
    r = requests.get(URL + address)
    return r.json()['features'][0]['geometry']['coordinates'][::-1]

first_place = get_coordinates(" 31 avenue du Granier, 38240, Meylan")
second_place = get_coordinates(" 7 Rue Henri Le Chatelier, Grenoble")