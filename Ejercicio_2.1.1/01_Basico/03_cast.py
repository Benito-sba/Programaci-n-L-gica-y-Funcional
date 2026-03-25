#03_casting de types
#trasformar un tipo de valor y otro

from os import system

if system("clear") != 0: system("cls")

print("conversion de tipo")

#convertir una cadenas contiene un numero a un entero
print(int("100")+2)

#convierte entero a cadena 
print("100"+ str(2))

#cv un numero decimal a tipo float

print(type(float("3.1416")))

#decinal a entero
print(int(3.1416))

#evaluar valores numericos como booleanos
print(bool(3)) #resultado true
print(bool(0)) #resultado false
print(bool(-1)) #numero negativo tambnien son true resultado true 


#evaluacion de cadena como booleanos 
print(bool("")) #una cadena vacias es false: resultado es false
print(bool(" ")) #una cadena con es espacio es true resultado true
print(bool("Fslse")) #una cadena con texto, auque tenga false resultado es true

#redondear un numero decimal
print(round(2.51)) #reodonde 2.5l al entero mas cercano resultado :3

#
#
