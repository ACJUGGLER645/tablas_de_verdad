notas = []
notas_aprobadas = []
cant_aprobadas = 0

cantidad_de_notas = int(input("Por favor ingresa la cantidad de notas a digitar (no mayor a 7): "))

if cantidad_de_notas > 0:
    for i in range (cantidad_de_notas):
        ing_notas = float(input(f"Ingresa la nota {i + 1}: "))
        if ing_notas > 5:
            print("Digita una nota menor a 5")
        elif ing_notas < 0:
            print("Digita una nota mayor a 0")
        else:
            notas.append(ing_notas)

elif cantidad_de_notas < 0:
    print("Digita un valor correcto")
else:
    print("Digita un valor correcto")

for nota in notas:
        if nota >= 3.0:
            cant_aprobadas += 1
            notas_aprobadas.append(nota)

print(f"La cantidad de notas aprobadas fueron: {len(notas_aprobadas)}")

    

'''for i, nota in enumerate(notas):
    print(f"La nota {nota + 1} es: {nota}")

promedio = sum(notas) / len (notas)
print(f"El promedio es {promedio}")'''


