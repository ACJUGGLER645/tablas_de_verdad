class Dogs:
    def __init__(self, nombre, raza, edad, color):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.color = color
    
    def imprimir_datos_perro(self):
        print(f"El nombre del perro es {self.nombre}")
        print(f"La raza del perro es {self.raza}")
        print(f"La edad del perro es {self.edad}")
        print(f"El color del perro es {self.color}")

    def cambio_de_datos(self, nueva_raza):
        self.raza = nueva_raza


primer_perrito = Dogs("Maya","Pitbull", 9, "Blanco con cafe")
segundo_perrito = Dogs("Paco", "Golder retriver", 9.9,"Amarillo")
tercer_perrito = Dogs("Negra","Criolla",12, "Negro")
cuarto_perrito = Dogs("Beyota", "Pitsky", 1.5,"Negro con blanco y cafe")
quinto_perrito = Dogs("Bruck","Pitsky",1.5,"Amarillo cafesoso")

primer_perrito.cambio_de_datos("Pitbull red nose")

primer_perrito.imprimir_datos_perro()