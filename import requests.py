import requests
from google import genai

# Inicializamos el cliente Gemini
client = genai.Client(api_key="AIzaSyBizqMhn7pe72biXXi6WLWd9iWEkZdNw3c")

class Pokemon:
    def __init__(self, name: str):
        url_api = f"https://pokeapi.co/api/v2/pokemon/{name}"
        respuesta_api: requests.Response = requests.get(url_api)

        if respuesta_api.status_code != 200:
            raise Exception("No hay conexión a la API o el Pokémon no existe.")

        rta_pokemon = respuesta_api.json()
        self.name: str = rta_pokemon["name"]
        self.height: float = rta_pokemon["height"] / 10
        self.weight: float = rta_pokemon["weight"] / 10
        self.id: int = rta_pokemon["id"]
        self.movimientos: list[str] = [mov["move"]["name"] for mov in rta_pokemon["moves"][:3]]

        # Generación
        especies_url = f"https://pokeapi.co/api/v2/pokemon-species/{name}"
        respuesta_especie = requests.get(especies_url)
        rta_especie = respuesta_especie.json()
        self.generation: str = rta_especie["generation"]["name"]

        # Ubicaciones
        url_location = f"https://pokeapi.co/api/v2/pokemon/{name}/encounters"
        respuesta_location = requests.get(url_location)
        rta_location = respuesta_location.json()
        self.locations: list[str] = [lugar["location_area"]["name"] for lugar in rta_location[:3]]

    def get_info_dict(self) -> dict:
        return {
            "nombre": self.name,
            "id": self.id,
            "altura": self.height,
            "peso": self.weight,
            "generación": self.generation,
            "movimientos": self.movimientos,
            "ubicaciones": self.locations
        }

def hablar_con_gemini(pokemon: Pokemon):
    info = pokemon.get_info_dict()
    descripcion = (
        f"Nombre: {info['nombre']}\n"
        f"ID: {info['id']}\n"
        f"Altura: {info['altura']} m\n"
        f"Peso: {info['peso']} kg\n"
        f"Generación: {info['generación']}\n"
        f"Movimientos principales: {', '.join(info['movimientos'])}\n"
        f"Ubicaciones comunes: {', '.join(info['ubicaciones']) if info['ubicaciones'] else 'No disponible'}"
    )

    prompt = (
        f"Habla como la pokedex con los siguientes datos del pokemon, no te extiendas mucho{descripcion}\n\n"
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash-preview-05-20",
        contents=prompt,
        config=genai.types.GenerateContentConfig(
            system_instruction="Actúa como una Pokédex sabia y útil."
        )
    )

    print("\n🔍 Análisis de la Pokédex:")
    print(response.text)
    print("--------------------------------------------------")

# Ejecución principal
def main():
    print("🔴 Bienvenido a la Pokédex Inteligente con Gemini\n")

    while True:
        nombre = input("🔎 Ingresa el nombre de un Pokémon ('exit' para salir): ").lower()
        if nombre == "exit":
            print("👋 Hasta la próxima, entrenador Pokémon.")
            break

        try:
            pokemon = Pokemon(nombre)
            hablar_con_gemini(pokemon)
        except Exception as e:
            print(f"⚠️ Error: {e}")

main()
