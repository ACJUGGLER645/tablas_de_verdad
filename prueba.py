'''
1. Sacar el gcd entre numerador y denominador
2. Dividir el numerador y denominador entre el gcd
'''
class Fracciones:
    def __init__(self, numerador, denominador):
        mcd = gcd(numerador, denominador)
        self.numerador = int(numerador/mcd)
        self.denominador = int (denominador/mcd)
    
    def __str__(self):
        return f'{self.numerador} / {self.denominador}'
        
    def __add__(self, fraccion_2):
        numerador = (self.numerador * fraccion_2.denominador) + (fraccion_2.numerador * self.denominador)
        denominador = (self.denominador * fraccion_2.denominador)
        mcd = gcd(numerador, denominador)
        numerador /= mcd
        denominador /= mcd
        suma_de_fracciones = Fracciones(numerador, denominador)
        return suma_de_fracciones
    
    def __sub__(self, fraccion_2):
        numerador = (self.numerador * fraccion_2.denominador) - (fraccion_2.numerador * self.denominador)
        denominador = (self.denominador * fraccion_2.denominador)
        mcd = gcd(numerador, denominador)
        numerador /= mcd
        denominador /= mcd
        resta_de_fracciones = Fracciones(numerador, denominador)
        return resta_de_fracciones
    
    def __mul__(self, fraccion_2):
        numerador = (self.numerador * fraccion_2.numerador) 
        denominador = (self.denominador * fraccion_2.denominador)
        mcd = gcd(numerador, denominador)
        numerador /= mcd
        denominador /= mcd
        multiplicacion_de_fracciones = Fracciones(numerador, denominador)
        return multiplicacion_de_fracciones
    
    def __truediv__(self, fraccion_2):
        numerador = (self.numerador * fraccion_2.denominador) 
        denominador = (self.denominador * fraccion_2.numerador)
        mcd = gcd(numerador, denominador)
        numerador /= mcd
        denominador /= mcd
        division_de_fracciones = Fracciones(numerador, denominador)
        return division_de_fracciones
    
def gcd(a, b):    
    while b:
        a, b = b, a%b
    return a

        
print(Fracciones(16,9)+Fracciones(8,9))
print(Fracciones(16,9)-Fracciones(8,9))
print(Fracciones(16,9)*Fracciones(8,9))
print(Fracciones(16,9)/Fracciones(8,9))

# 