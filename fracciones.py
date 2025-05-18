class Fracciones:
    def __init__(self, numerador, denominador):
        if denominador == 0:
            raise Exception("El denominador no puede ser 0")
        mcd = gcd(numerador, denominador)
        self.numerador = numerador // mcd
        self.denominador = denominador // mcd

    def __str__(self):
        if self.denominador == 1:
            return str(self.numerador)
        return f'{self.numerador} / {self.denominador}'

    def __add__(self, fraccion_2):
        numerador = (self.numerador * fraccion_2.denominador) + (fraccion_2.numerador * self.denominador)
        denominador = (self.denominador * fraccion_2.denominador)
        mcd = gcd(numerador, denominador)
        return Fracciones(numerador // mcd, denominador // mcd)

    def __sub__(self, fraccion_2):
        numerador = (self.numerador * fraccion_2.denominador) - (fraccion_2.numerador * self.denominador)
        denominador = (self.denominador * fraccion_2.denominador)
        mcd = gcd(numerador, denominador)
        return Fracciones(numerador // mcd, denominador // mcd)

    def __mul__(self, fraccion_2):
        numerador = self.numerador * fraccion_2.numerador
        denominador = self.denominador * fraccion_2.denominador
        mcd = gcd(numerador, denominador)
        return Fracciones(numerador // mcd, denominador // mcd)

    def __truediv__(self, fraccion_2):
        if fraccion_2.numerador == 0:
            raise ZeroDivisionError("No se puede dividir entre una fracción con numerador 0")
        numerador = self.numerador * fraccion_2.denominador
        denominador = self.denominador * fraccion_2.numerador
        mcd = gcd(numerador, denominador)
        return Fracciones(numerador // mcd, denominador // mcd)

    def Sobre_escribir(self):
        while True:
            try:
                nuevo_numerador = int(input("Digite el nuevo numerador: "))
                nuevo_denominador = int(input("Digite el nuevo denominador: "))
                if nuevo_denominador == 0:
                    raise ZeroDivisionError("El denominador no puede ser 0")
                mcd = gcd(nuevo_numerador, nuevo_denominador)
                self.numerador = nuevo_numerador // mcd
                self.denominador = nuevo_denominador // mcd
                print("Fracción sobreescrita correctamente:")
                print(self)
                break
            except ValueError:
                print("Error: Solo se permiten números enteros.")
            except ZeroDivisionError as e:
                print(f"Error: {e}")

def gcd(a, b):    
    while b:
        a, b = b, a % b
    return a

while True:
    try:
        numerador = int(input("Digite el numerador: "))
        denominador = int(input("Digite el denominador: "))
        entrada = Fracciones(numerador, denominador)
        print(f"Fracción creada correctamente: {entrada}")
        break
    except ValueError:
        print("Error: Solo se permiten números.")
    except Exception as e:
        print(f"Error: {e}")

while True:
    print("\nMenu")
    print("1. Mostrar fracción")
    print("2. Sobreescribir fracción")
    print("3. Salir")

    try:
        opcion_menu = int(input("Selecciona una opción: "))
    except ValueError:
        print("Error: Debes digitar un número.")
        continue

    if opcion_menu == 1:
        print(f"La fracción actual es: {entrada}")
    elif opcion_menu == 2:
        entrada.Sobre_escribir()
    elif opcion_menu == 3:
        print("Chau")
        break
    else:
        print("Opción no válida, intenta de nuevo.")