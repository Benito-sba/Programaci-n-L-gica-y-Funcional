
#AA 2.1 Reporte práctico/Ejercicios_2.1/02_flujo_control
#Benito Santiago Balam Acevedo


# Q1 - Sentencias condicionales (if, elif, else)
# Permiten ejecutar bloques de código solo si se cumplen ciertas condiciones.

from os import system
if system("clear") != 0: system("cls")

print("\n Sentencia simple condicional")
# Podemos usar la palabra clave "if" para ejecutar un bloque de código
# solo si se cumple una condición.

edad = 18
if edad >= 18:
    print("Eres mayor de edad")
    print("¡Felicidades!")

# Si no se cumple la condición, no se ejecuta el bloque de código

edad = 15
if edad >= 18:
    print("Eres mayor de edad")
    print("¡Felicidades!")

# Podemos usar el comando “else” para ejecutar un bloque de código
# si no se cumple la condición anterior del if

print("\n Sentencia condicional con else")
edad = 15
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

print("\n Sentencia condicional con elif")

# Además de usar "if" y "else", podemos usar "elif" para determinar
# múltiples condiciones, ten en cuenta que sólo se ejecutará el primer bloque
# de código que cumpla la condición (o la del else, si esta presente)

nota = 5
if nota >= 9:
    print("¡Sobresaliente!")
elif nota >= 7:
    print("Notable!")
elif nota >= 5:
    print("¡Aprobado!")
else:
    print("¡No esta calificado!")

print("\n Condiciones multiples")
edad = 16
tiene_carnet = True

# Los operadores lógicos en Python son:
# and: True si ambos operandos son verdaderos
# or: True si al menos uno de los operandos es verdadero
# En javaScript:
# && seria and
# !! seria or
# En el caso que seas mayor de edad y tengas carnet...
# entonces podras conducir

if edad >= 18 and tiene_carnet:
    print("Puedes conducir 🚗🚗 ")
else:
    print("POLICIA 🚗🚗 !!!!!")

# En un pueblo de Isla Holbox son mas relajados y
# te dejan conducir si eres mayor de edad o tienes carnet

if edad >= 18 or tiene_carnet:
    print("Puedes conducir en la Isla Holbox")
else:
    print("Paga al policia y te dejará conducir!!!")

# También tenemos el operador lógico "not"
# que nos permite negar una condición

es_fin_de_semana = False

# javaScript > !

if not es_fin_de_semana:
    print("¡ISC, anda que hay que ir al Tec!")

# Podemos anidar condicionales

print("\n Anidar condicionales")

edad = 20
tiene_dinero = True

if edad >= 18:
    if tiene_dinero:
        print("Puedes ir a la discoteca")
    else:
        print("Quédate en casa")
else:
    print("No puedes entrar a la disco")

# Ten en cuenta que hay valores que al usarlos como condiciones
# en Python son evaluados como verdaderos o falsos
numero = 5
if numero:
    print("El número no es cero")

numero = 0
if numero:
    print("Aqui no entrara nunca")

nombre = ""
if nombre:
    print("El nombre no es vacio")

# ¡Ten cuidado con no confundir la asignación = con la comparación ==!
numero = 3
es_el_tres = numero == 3

if es_el_tres:
    print("El numero es 3")

# Condición ternaria
print("\nLa condición ternaria:")

edad = 17
mensaje = "Es mayor de edad" if edad >= 18 else "Es menor de edad"
print(mensaje)




# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
if num1 > num2:
    print(f"{num1} es mayor.")
elif num2 > num1:
    print(f"{num2} es mayor.")
else:
    print("Son iguales.")



# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))
op = input("Operación (+, -, *, /): ")
if op == "+": print(n1 + n2)
elif op == "-": print(n1 - n2)
elif op == "*": print(n1 * n2)
elif op == "/":
    print(n1 / n2 if n2 != 0 else "Error: División por cero")



# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

anio = int(input("Año: "))
if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print("Es bisiesto")
else:
    print("No es bisiesto")


# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

e = int(input("Edad: "))
if 0 <= e <= 2: print("Bebé")
elif 3 <= e <= 12: print("Niño")
elif 13 <= e <= 17: print("Adolescente")
elif 18 <= e <= 64: print("Adulto")
else: print("Adulto mayor")
