#04_variables
#las variables sirven para gurdar datos de memoria


from os import system

if system("clear") != 0: system("cls")

#para asignar una variable 
my_name = "Santiago"
print(my_name)

age =22

print(age)
# reasignar un nuevo valor a una variable

age =68

print(age)

#tipado dinamico el tipo de dato se determina en tiempo real 

my_name = "Santiago"
print(type(my_name))


#_______________

#tipado fuerte porque no es automatico
#genera un error por que no sume un numero con cadena


#f-string : cadena de formato

print(f"hola {my_name} , tengo {age + 5} años")

#forma no recomendada
name, age, city ="benito", 22, "FCP"

#
mi_nombre_de_variable = "ok"

nombre = "ok"

miNombreSeVariable ="no-recomendado" #camelcase
MiNombreDeVariable ="no-recomendado"#Pascalcase
MiNombreDeVariable ="no-recomendado"#todojunto


mi_nombre_de_variable_123 = "ok"

MI_COSTANTE =3.14

#nombre no validos 

#anotaciones de tipo opcional
is_user_logged_in: bool = True
print(is_user_logged_in)

name: str = "benito"
print(name)
