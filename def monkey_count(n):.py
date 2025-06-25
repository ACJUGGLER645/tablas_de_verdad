# retornar listas
def monkey_count(n):
    return list(range(1, n + 1))

print(monkey_count(10))

#cuenta de letras
def count_char_occurrences(string, char):
    return string.count(char)

print(count_char_occurrences("bananaaaaa", "n"))

#capicua
cadena_texto : str = "rcomer"

if cadena_texto != cadena_texto[::-1]:
    print("No es capicua")
else : print ("Es capicua")

print(cadena_texto[::-1])

lista : list = ["Puño magico", "Salto Embolvente"] #, "Beso intrepido", "Doble patada"]
for i in lista [:3]:
    print(i)
