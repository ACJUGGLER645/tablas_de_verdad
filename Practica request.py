
'''
# Practica de 
import requests

class Pokemon ():
    def __init__(self, name):
        self.name = name
        self.id = id


name = "Charmander"
url = f"https://pokeapi.co/api/v2/pokemon/{2}"
api_response = requests.get(url)
data = api_response.json()
id_data = data["id"]
name_data = data["name"]
print(name_data)


url_characteristics = f"https://pokeapi.co/api/v2/characteristic/{id_data}/"
api_response_cha = requests.get(url_characteristics)
if api_response_cha.status_code == 200: 
    data_characteristics = api_response_cha.json()
    descriptions = data_characteristics["descriptions"]
    for d in descriptions:
        if d["language"]["name"] == "es":
            print(f"Descripción característica: {d['description']}")
            break
'''

info = {
    "pokemon": {
        "name": "charmander",
        "type": ["fire"],
        "abilities": [
            {"name": "blaze"},
            {"name": "solar-power"}
        ]
    }
}

datos = info["pokemon"]
nombre = datos["name"]
tipo = datos["type"][0]
habilidades = datos["abilities"]
for i, habilidad in enumerate(habilidades, start=1):
    print(f"{i}. {habilidad["name"]}")

pokemones = ["pikachu", "bulbasaur", "charmander"]
for i, nombre in enumerate(pokemones, start=1):
    print(i, nombre)

