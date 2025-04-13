class Dogs:
    def __init__(self, nombre, raza, edad, color, en_vida):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.color = color
        self.en_vida = en_vida
    
    def imprimir_datos_perro(self):
        print(f"El nombre del perro es {self.nombre}")
        print(f"La raza del perro es {self.raza}")
        print(f"La edad del perro es {self.edad}")
        print(f"El color del perro es {self.color}")
        print(f"El perro esta en vida (T/F): {self.en_vida}")

    def cambio_de_datos(self, nueva_raza, cambio_en_vida):
        self.raza = nueva_raza
        self.en_vida = cambio_en_vida


primer_perrito = Dogs("Maya","Pitbull", 9, "Blanco con cafe", True)
segundo_perrito = Dogs("Paco", "Golder retriver", 9.9,"Amarillo", False)
tercer_perrito = Dogs("Negra","Criolla",12, "Negro", True)
cuarto_perrito = Dogs("Beyota", "Pitsky", 1.5,"Negro con blanco y cafe", True)
quinto_perrito = Dogs("Bruck","Pitsky",1.5,"Amarillo cafesoso", True)

primer_perrito.cambio_de_datos("Pitbull red nose", False)

primer_perrito.imprimir_datos_perro()