import requests

class Pokemon():
    def __init__(self, name: str):
    
        url_api : str = f"https://pokeapi.co/api/v2/pokemon/{name}"
        respuesta_api : requests.Response = requests.get(url_api)

        if respuesta_api.status_code != 200:
            raise Exception ("No hay conección a la API")
        rta_pokemon = respuesta_api.json() # no se coloca el tipo de dato puesto que es any

        self.name : str = rta_pokemon["name"]
        self.height : float = rta_pokemon["height"] / 10
        self.weight : float = rta_pokemon["weight"] / 10
    
    def get_height (self) -> float :
        return self.height
    
    def get_weight (self) -> float:
        return self.weight


lista : list = ["Puño magico", "Salto Embolvente"]#,"Beso intrepido", "Doble patada"]
for i in lista [:3]:
    print(i)

cadena_texto : str = "rcomer"

if cadena_texto != cadena_texto[::-1]:
    print("No es capicua")
else : print ("Es capicua")

print(cadena_texto[::-1])

firts_pokemon : Pokemon = Pokemon("Pikachu")


print(f"\nPikachu mide {firts_pokemon.get_height()} metros y pesa {firts_pokemon.get_weight()} kilogramos")
