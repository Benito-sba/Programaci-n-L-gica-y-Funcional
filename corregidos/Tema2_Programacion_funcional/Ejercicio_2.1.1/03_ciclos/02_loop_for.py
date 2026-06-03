# iterrar una lista
#Benito Santiago Balam Acevedo


from os import system
if system("clear") != 0: system("cls")

frutas = {"manzana", "platano", "pera" }
for d in frutas:
    print(frutas)


#cadena
cadena = "estudiante"
for caracter in cadena:
    print(caracter)


#enuimerate

frutas = {"manzana", "platano", "pera" }
for idx, value  in enumerate(frutas):
    print(f"el indice es {idx} y la fruta es {value}")


#bluce anilado

letras = ["A", "B", "C"]
numeros = [1, 2, 3]

for letra in letras:
    for numero in numeros:
        print(f"{letra}{numero}")
        
#break

print("\n break:")

animales = {"perro", "gato", "raton"}
for idx, animal in enumerate(animales):
    print(animal)
    if animal == "loro":
        print(f"el loro es escondido {idx}")
        break


# continue

print("\ncontinue:")

animales = {"perro", "gato", "raton"}
for idx, animal in enumerate(animales):
    if animal == "loro": continue
 
print(animal)


# com_lista

animales = {"perro", "gato", "raton"}
animales_mayus = {animales.upper() for animales in animales}
print(animales_mayus)

# muesta nume4ro

pares = {num for num in {1,2,3,4,5,6} if num % 2 == 0}
print(pares)


###
# EJERCICIOS (for)
###

# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.

numeros_pares = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
for i in numeros_pares:
    print(i)

# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.

numeros = [10, 20, 30, 40, 50]
suma_total = 0
for n in numeros:
    suma_total += n
media = suma_total / len(numeros)
print(f"La media es: {media}")

# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.

numeros = [15, 5, 25, 10, 20]
maximo = numeros[0]
for n in numeros:
    if n > maximo:
        maximo = n
print(f"El maximo es: {maximo}")

# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
# palabras = ["cerro", "carros", "miel", "abejorro", "cantarito"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.

palabras = ["cerro", "carros", "miel", "abejorro", "cantarito"]
filtradas = [p for p in palabras if len(p) > 5]
print(f"Palabras con más de 5 letras: {filtradas}")


# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# palabras = ["cerro", "carros", "miel", "abejorro", "cantarito"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).

palabras = ["cerro", "carros", "miel", "abejorro", "cantarito"]
letra_usuario = input("Ingresa una letra: ").lower()
contador_palabras = 0

for p in palabras:
    if p.lower().startswith(letra_usuario):
        contador_palabras += 1

print(f"si hay {contador_palabras} palabras con '{letra_usuario}'")# iterrar una lista


