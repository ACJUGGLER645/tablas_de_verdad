import requests

pokemon = None


def get_name():
    global pokemon
    pokemon_name = input("Digita el nombre del pokemon: ").lower()

    if not pokemon_name.isalpha():
        print("\nDigita solo caracteres válidos (letras del abecedario).")
        return

    url_api = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    respuesta = requests.get(url_api)

    if respuesta.status_code == 200:
        pokemon = respuesta.json()
        print(f"\n✅ El nombre del Pokémon ingresado es: {pokemon['name'].upper()}")
    else:
        print(f"\n❌ No se encontró el Pokémon '{pokemon_name}'. Verifica el nombre.")


def get_data():
    global pokemon

    if not pokemon:
        print("❗ No se ha seleccionado un Pokémon aún.")
        return

    nombre = pokemon["name"]
    species_url = f"https://pokeapi.co/api/v2/pokemon-species/{nombre}"
    species_response = requests.get(species_url)


    generation = species_response.json()["generation"]["name"]
    hp = next(stat["base_stat"] for stat in pokemon["stats"] if stat["stat"]["name"] == "hp")
    altura = pokemon["height"] / 10
    peso = pokemon["weight"] / 10
    movimientos = []  # Creamos una lista vacía para guardar los movimientos
    for i in range(3):
        movimiento = pokemon["moves"][i]["move"]["name"]
        movimientos.append(movimiento)


    # Mostrar datos
    print(f"\n📘 Pokédex de {nombre.upper()}")
    print(f"Generación: {generation}")
    print(f"Salud base (HP): {hp}")
    print(f"Altura: {altura} m")
    print(f"Peso: {peso} kg")
    print("Movimientos:")
    for move in movimientos:
        print(f"  - {move}")


def show_data_pokemon():
    if pokemon:
        print(f"\n🔍 Pokémon actual: {pokemon['name'].upper()}")
    else:
        print("❗ No se ha seleccionado un Pokémon previamente.")


##data()

while True:
    print("\nMenu Pokedex")
    print("1. Datos de pokemon")  
    print("2. Ver información de pokemon")   
    print("3. Salir de la Pokedex")  
    
    try:
        opcion = int(input("\nDigita la opción: "))
    
    except ValueError:
        print("Recuerda digitar un valor numerico: ")

    if opcion == 1 :
        get_name()
    elif opcion == 2:
        get_data()
    elif opcion == 3:  
        print("Nos vemos luego, se el mejor entrenador Pokemon")
        break
    else:
        print("Opcón no valida, intenta de nuevo")


