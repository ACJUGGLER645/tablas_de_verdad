class Fracciones:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __str__(self):
        return f'{self.numerador} / {self.denominador}'
mi_fraccion = Fracciones(1, 2)



print(mi_fraccion)
