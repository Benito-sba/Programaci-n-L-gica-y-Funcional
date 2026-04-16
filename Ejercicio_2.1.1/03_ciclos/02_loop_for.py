# iterrar una lista



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
