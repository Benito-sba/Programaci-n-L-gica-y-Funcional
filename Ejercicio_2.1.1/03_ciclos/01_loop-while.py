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



###
# EJERCICIOS (while)
###

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.

contador = 10
while contador >= 1:
    print(contador)
    contador -= 1


# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.

suma = 0
numero = 1
while numero <= 20:
    if numero % 2 == 0:
        suma += numero
    numero += 1
print(f"El resultado de la suma de los números pares entre 1 y 20 es: {suma}")


# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número


n = int(input("Ingresa un número entero que sea positivo: "))
facto = 1
temp = n
while temp > 1:
    facto *= temp
    temp -= 1
print(f"El factorial de {n} es: {facto}")


# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".

password = input("Ingresa una contraseña de tu agrado: ")
while len(password) < 8:
    print("Error: La contraseña no cumple con 8 caracteres.")
    password = input("Ingresa una contraseña: ")
print("Contraseña correcta")



# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
num_tab = int(input("Ingresa un número: "))
i = 1
while i <= 10:
    print(f"{num_tab} x {i} = {num_tab * i}")
    i = i + 1 


# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.

n_limite = int(input("Ingresa un número entero positivo: "))
num = 2
print(f"Números primos hasta {n_limite}:")
while num <= n_limite:
    es_primo = True
    divisor = 2
    while divisor * divisor <= num:
        if num % divisor == 0:
            es_primo = False
            break
        divisor += 1
    if es_primo:
        print(num, end=" ")
    num += 1

