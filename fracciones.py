class Fracciones:
    def __init__(self, numerador = 1, denominador = 1, new_numerador = 1, new_denominador = 1):
        self.numerador = numerador
        self.denominador = denominador
        self.new_numerador = new_numerador
        self.new_denominador = new_denominador

    def ingreso_de_datos(self):
        self.numerador = int(input("Digita el numerador: "))
        self.denominador = int(input("Digita el denominador: "))

    def nuevo_ingreso_de_datos(self):
        self.new_numerador = int(input("Digita el nuevo numerador: "))
        self.new_denominador = int(input("Digita el nuevo denominador: "))


mi_fraccion = Fracciones()

mi_fraccion.ingreso_de_datos()

print(f"La fracción es: {mi_fraccion.numerador}/{mi_fraccion.denominador}")

mi_fraccion.nuevo_ingreso_de_datos()
print(f"La nueva fracción es: {mi_fraccion.new_numerador}/{mi_fraccion.new_denominador}")


