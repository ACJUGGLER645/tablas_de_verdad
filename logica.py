#Ejercicio 1 
'''
numeros = []
pares = []
impares = []

cantidad_de_numeros = int(input("Ingresa cuantos numeros quieres agregar a la lista (No menor a 0 y mayor a 10 y que sean enteros): "))

if cantidad_de_numeros > 0 and cantidad_de_numeros < 11:
    for num in range (cantidad_de_numeros):
        numero = int(input(f" Digita el numero {num + 1}: "))
        numeros.append(numero)
    for num in numeros:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)

    print(pares)
    print(impares)
    print(len(impares))
    print(len(pares))

else:
    print("Digita un valor entre el rango mencionado")
'''
#Ejercicio 2 
'''
numero = int(input("Ingresa un numero mayor a 0: "))
suma = []
suma_multiplos_de_3 = 0

if numero > 0:
    for num in range (numero):
        if num % 3 == 0:
            suma.append(num)
    suma_multiplos_de_3 = sum(suma)
    print(suma_multiplos_de_3)
else:
    print("Digita un valor correcto")

#Corregido 

numero = int(input("Ingresa un numero mayor a 0: "))
suma = []
suma_multiplos_de_3 = 0

if numero > 0:
    for num in range(1, numero + 1):
        if num % 3 == 0:
            suma.append(num)
    suma_multiplos_de_3 = sum(suma)
    print(suma_multiplos_de_3)
else:
    print("Digita un valor correcto")
'''
# Ejercicio 3

'''
lista = []

print("Creemos una lista de numeros :D")
cantidad_de_numeros = int(input("Ingresa cuantos numeros ingresamos a la lista (No mayores a 10): "))

if cantidad_de_numeros > 0 and cantidad_de_numeros < 11:
    for num in range (cantidad_de_numeros):
        numero = int(input(f"Ingresa el numero {num + 1}: "))
        lista.append(numero)
    print(f"La lista que ingresaste es {lista}")

    validación = int(input("Teclea un numero y validemos si esta en la lista: "))
    if validación in lista:
        print(f"El numero {validación} está en la lista")
    else:
        print(f"El numero {validación} no está en la lista")
else:
    print("Digita un valor correcto")
'''
#Ejercicio 4
'''
a = 0
texto = input("Digita una palabra y contemos sus a en ella: ").lower()
vocal  = ["a"]
for letra in texto:
    if letra in vocal:
        a+=1

print(f"La cantidad de vocales a en la palabra o frase es {a}")
'''
#Ejercicio 5

edades = []
edad = 0
contador = 0
cantidad_de_edades = int(input("Ingresa cuentas edades quieres ingresar entre 1 y 5: "))

if  cantidad_de_edades > 0 and cantidad_de_edades < 6:
    for ed in range (cantidad_de_edades):
        edad = int(input(f"Digita le edad {ed + 1}: "))
        while edad > 120 or edad < 0:
            print("Revisa la edad digitada")
            edad = int(input(f"Ingresa la edad {ed+1} nuevamente: "))
        edades.append(edad)
    for ed in edades:
        if ed >= 18:
            contador += 1
    
    print(f"En la lista de edades {edades}, hay {contador} mayores de edad")

else:
    print("Digita un valor entre el rango mencionado")
