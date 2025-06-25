import requests
from google import genai

client = genai.Client(api_key="AIzaSyBizqMhn7pe72biXXi6WLWd9iWEkZdNw3c")


class Pokemon():
    def __init__(self, name: str):
        url_api = f"https://pokeapi.co/api/v2/pokemon/{name}"
        respuesta_api : requests.Response = requests.get(url_api)

        if respuesta_api.status_code != 200:
            raise Exception ("No hay conección a la API")
        
        rta_pokemon = respuesta_api.json() # no se coloca el tipo de dato puesto que es any
        self.name: str = rta_pokemon["name"]
        self.height: float = rta_pokemon["height"] / 10
        self.weight: float = rta_pokemon["weight"] / 10
        self.id: int = rta_pokemon["id"]
        self.movimientos: list[str] = [mov["move"]["name"] for mov in rta_pokemon["moves"][:3]]

        #generación
        especies_url = f"https://pokeapi.co/api/v2/pokemon-species/{name}"
        respuesta_especie = requests.get(especies_url)
        rta_especie = respuesta_especie.json()
        self.generation: str = rta_especie["generation"]["name"]

        #location
        url_location = f"https://pokeapi.co/api/v2/pokemon/{name}/encounters"
        respuesta_location = requests.get(url_location)
        rta_location = respuesta_location.json()
        self.locations: list[str] = [lugar["location_area"]["name"] for lugar in rta_location[:3]]

        #Characteristics
        url_characteristics = f"https://pokeapi.co/api/v2/characteristic/{self.id}/"
        api_response_cha = requests.get(url_characteristics)
        data_characteristics = api_response_cha.json()
        descriptions_list = data_characteristics["descriptions"]
        # Valor por defecto
        self.description = "No hay descripción en español"
        # Buscar descripción en español
        for d in descriptions_list:
            if d["language"]["name"] == "es":
                self.description = d["description"]
                break

    def dic_info(self):
            return {
                 "name" : self.name, 
                 "id" : self.id, 
                 "height" : self.height, 
                 "weight" : self.weight, 
                 "generacion" : self.generation, 
                 "locations" : self.locations,
                 "movimientos" : self.movimientos,
                 "description" : self.description            
            }

    def show_info (self):
         print(f"📱 Pokemon: {self.name.upper()} el pokemon que {self.description}")
         print(f"Numero de pokemon: {self.id} de la {self.generation.capitalize()}")
         print(f"{self.name.capitalize()}, tiene un peso de {self.weight} kg y su altura es de {self.height} m")
         print(f"\n🍃Los movimientos más populares de {self.name} son:")
         for movimiento in self.movimientos:
              print(f"- {movimiento}")
         print(f"\n📝 Algunos lugares donde lo puedes encontrar son: ")
         if self.locations != []:
            for lugar in self.locations:
              print(f"- {lugar}")
         else:
             print("🚫 No hay lugares con encuentros de ese Pokemon")
    
def gemini(pokemon: Pokemon):
    info = pokemon.dic_info()
    prompt = f"Habla como la Pokédex con los siguientes datos del Pokémon, no te extiendas mucho:\n{info}"
    
    response = client.models.generate_content(
        model="gemini-2.5-flash-preview-05-20",
        contents=prompt,
        config=genai.types.GenerateContentConfig(system_instruction="Actúa como una Pokédex sabia y útil.")
    )

    print("\n🔍 Análisis de la Pokédex:")
    print(response.text)
    print("--------------------------------------------------")



'''
instancia = Pokemon("charizard")
print(instancia.dic_info())
instancia.show_info()
'''

def get_name():
    pokemon_name = input("🔎 Digita el nombre del Pokémon: ").lower()
    if not pokemon_name.isalpha():
        print("❗ Solo puedes usar letras del abecedario.")
        return None
    return pokemon_name

def get_data(pokemon_name):
    try:
        pokemon = Pokemon(pokemon_name)
        pokemon.show_info()
        return pokemon 
    except Exception as e:
        print(f"Error al obtener la información: {e}")
        return None


nombre_actual = None
pokemon_actual = None

while True:
    print("\n1. Ingreso nombre del Pokémon")   
    print("2. Ver resumen de la Pokédex (IA)")   
    print("3. Salir de la Pokédex")

    try:
        opcion = int(input("\n➡️ Digita la opción: "))
    except ValueError:
        print("Recuerda digitar un valor numérico :)")
        continue

    if opcion == 1:
        nombre_actual = get_name()
        pokemon_actual = get_data(nombre_actual)

    elif opcion == 2:
        if pokemon_actual:
            gemini(pokemon_actual)
        else:
            print("Primero debes ingresar un Pokémon.")

    elif opcion == 3:  
        print("👋 Nos vemos luego, ¡sé el mejor entrenador Pokémon!")
        break
    else:
        print("❗ Opción no válida, intenta de nuevo")




#Tarea
# Corrección de tarea: listas, tipos
# Clase Pokemon 
# Todo por fuera de las clases
# Implementar todo lo visto hasta hoy






