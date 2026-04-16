#Benito Santiago Balam Acevedo

from os import system
if system("clear") != 0: system("cls")

print("\n blucle while:")

contador = 0

while contador <= 5:
    print(contador)
    contador += 1

# con la palabra break

print("\n blucle while con beark")

contador = 0

while True:
    print(contador)
    contador += 1
    if contador == 5:
        break


# con bluqie

print("\n blucle continue")

contador = 0

while contador < 10:
    contador+= 1
    if contador == 5:
        break


# else 

print("\n blucle continue")

contador = 0

while contador < 5:
    print(contador)
    contador+= 1
else :
    print("el bucle ha terminado")


#pedimos al usuario

numero = -1
while numero < 0:
    numero = int(input("Escribe el numero: "))
    if numero < 0:
        print("El numnero es psitivo")

print(f"El numnero que pusistes es {numero}")


numero = -1
while numero < 0:
    try:
        numero = int (input("escribe el numero"))
        if numero < 0:
            print("el numero debe ser positivo")
    except:
        print("lo que pusistes no es numero")

print(f"El numero que has ponido es {numero} ")




