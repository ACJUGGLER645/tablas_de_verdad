class Fracciones:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __str__(self): #Retorna
        numerador = self.numerador
        denominador = self.denominador
        variable = f"{numerador} / {denominador}"
        return variable

    def ingreso_de_datos(self):
        self.numerador = int(input("Digita el numerador: "))
        self.denominador = int(input("Digita el denominador: "))

    def mostrar_fracccion (self):
        print(f"{self.numerador} / {self.denominador}")

mi_fraccion = Fracciones(45,45)
mi_fraccion.mostrar_fracccion()
print(mi_fraccion)

