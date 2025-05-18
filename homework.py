import requests

pokemon = None


def get_name():
    global pokemon
    pokemon_name = input("Digita el nombre del pokemon: ").lower()

    if not pokemon_name.isalpha():
        print("\nDigita solo caracteres válidos (letras del abecedario).")
        return

    url_api = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    respuesta_api = requests.get(url_api)

    if respuesta_api.status_code == 200:
        pokemon = respuesta_api.json()
        print(f"\nEl nombre del Pokémon digitado es: {pokemon['name'].capitalize()}")
    else:
        print(f"\nNo se encontró el Pokémon '{pokemon_name.upper()}'. Verifica el nombre.")


def get_data():
    global pokemon

    if not pokemon:
        print("No se ha seleccionado un Pokémon aún.")
        return

    nombre = pokemon["name"]
    especies_url = f"https://pokeapi.co/api/v2/pokemon-species/{nombre}"
    especies_respuesta = requests.get(especies_url)

    #Basic Data
    generation = especies_respuesta.json()["generation"]["name"]
    id_pokemon = pokemon["id"]
    altura = pokemon["height"] / 10 #Se pasa a m está en decimetros
    peso = pokemon["weight"] /10 #Se pasa a kg está en hectogramos
    movimientos = []
    for i in range(3):
        movimiento = pokemon["moves"][i]["move"]["name"]
        movimientos.append(movimiento)

    #Location Data

    location_url =  f"https://pokeapi.co/api/v2/pokemon/{nombre}/encounters"
    location_respuesta = requests.get(location_url)
    #location = location_respuesta.json()[0]["location_area"]["name"]
    locations = []
    for i in range (2):
        location = location_respuesta.json()[i]["location_area"]["name"]
        locations.append(location)
    print(locations)

    #print_data

    print(f"\n📘 Pokédex de {nombre.upper()}")
    print(f"Numero de pokemon: {id_pokemon}")
    print(f"Generación: {generation.capitalize()}")
    print(f"Altura: {altura} m")
    print(f"Peso: {peso} kg")
    print("⚡Movimientos⚡:")
    for move in movimientos:
        print(f"  * {move}")
    print(f"📍Zonas en donde se puede encontrar a {nombre.upper()}")
    for location in locations:
        print(f" * {location.capitalize()}")

'''
def show_data_pokemon():
    if pokemon:
        print(f"\nPokémon actual: {pokemon['name'].upper()}")
    else:
        print("No se haz seleccionado un Pokémon previamente")
'''

while True:
    print("\nMenu Pokedex")
    print("1. Ingreso nombre pokemon")  
    print("2. Ver información de pokemon")   
    print("3. Salir de la Pokedex")  
    
    try:
        opcion = int(input("\nDigita la opción: "))
    
    except ValueError:
        print("Recuerda digitar un valor numerico:) ")

    if opcion == 1 :
        get_name()
    elif opcion == 2:
        get_data()
    elif opcion == 3:  
        print("Nos vemos luego, se el mejor entrenador Pokemon")
        print("Chauu")
        break
    else:
        print("Opcón no valida, intenta de nuevo")

print ("Hey")


