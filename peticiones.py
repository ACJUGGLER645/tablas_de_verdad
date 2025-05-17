import requests

#pikachu = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
#print(pikachu.json())

name_pokemon = input("Digita el nombre del pokemon: ").lower()
obtencion = requests.get (f"https://pokeapi.co/api/v2/pokemon/{name_pokemon}")

#for pokemon in obtencion.json()["moves"]:
 #   print(pokemon["move"]["name"])


prueba = requests.get (f"https://pokeapi.co/api/v2/pokemon-species/{name_pokemon}").json()["color"]["name"]
prueba_2 = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name_pokemon}").json()["location_area_encounters"]
print(prueba, prueba_2)

# Tarea
# 1. Ingreso por teclado de pokemon
# 2. Generar Pokedex (Peso, habilidades, altura, numero de pokemon)
# 3. Menu para ver información 1. Ingreso de datos 2. Ver informacion del pokemon 3. Sobreescribir pokemon 4. Salir


