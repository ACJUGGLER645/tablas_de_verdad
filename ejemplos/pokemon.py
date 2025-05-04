import tkinter.ttk as ttk
import tkinter as tk
from tkinter import Tk
import pydub
import pydub.playback
import requests
from io import BytesIO
from PIL import Image, ImageTk

def get_pokemon_info(pokemon_name: str) -> dict:
    endpoint: str = 'https://pokeapi.co/api/v2/pokemon'
    try:
        pokemon_info: dict = requests.get(f'{endpoint}/{pokemon_name}').json()
    except:
        raise Exception('No hay recurso xd')
    return pokemon_info

def pokemon_sound(pokemon_name: str) -> None:
    pokemon_info:dict = get_pokemon_info(pokemon_name)

    cry_url: str = pokemon_info['cries']['latest']

    try:
        binary: bytes = requests.get(cry_url).content
        temp_file = BytesIO(binary)
    except:
        raise Exception('No existe sonido')

    audio = pydub.AudioSegment.from_file_using_temporary_files(temp_file, format='ogg')
    pydub.playback.play(audio)

def pokemon_update(pokemon_name: str, label: ttk.Label):
    pokemon_info:dict = get_pokemon_info(pokemon_name)

    sprite_url:str = pokemon_info['sprites']['front_default']

    try:
        binary: bytes = requests.get(sprite_url).content
        temp_file = BytesIO(binary)
    except:
        raise Exception('No existe sprite')
    
    image: Image = Image.open(temp_file)
    image_tk: ImageTk = ImageTk.PhotoImage(image)

    label.configure(image=image_tk)
    label.image = image_tk

root = Tk()

pokemon_name: tk.StringVar = tk.StringVar()
pokemon_name.set('furret')

frame = ttk.Frame(root, padding=10)
frame.grid()

ttk.Label(frame, text='Pokemon >:)').grid(column=0, row=0)

label = ttk.Button(frame, command= lambda:pokemon_sound(pokemon_name.get()))
label.grid(column=0, row=1)
pokemon_update('furret', label)

ttk.Entry(frame, textvariable=pokemon_name).grid(column=0, row=2)
ttk.Button(frame, text='Buscar', command=lambda: pokemon_update(pokemon_name.get(), label)).grid(column=0, row=3)

root.mainloop()