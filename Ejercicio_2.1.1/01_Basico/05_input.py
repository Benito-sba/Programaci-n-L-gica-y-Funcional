#05_entrada de usuario

from os import system

if system("clear") != 0: system("cls")

nombre = input("hola, ¿como tellamas?\n")
print(f"hola {nombre}, encantado")

age = input("¿cuantos años tienes?")
age = int(age)
print(f"tienes {age} años")

print("obtener multiples valores en una")
country, city = input("en que pasi u ciudad vives\n").split()

print(f"vive en {country, {city}}")

