#Benito Santiago Balam Acevedo
#Adan Adair Moo NOH
#AA 3.2 Sistema experto


import subprocess
import os


PROLOG_FILE = "base_conocimientos.pl"
SWIPL = r"C:\Program Files\swipl\bin\swipl.exe"


preguntas = [
    ("programacion", "¿Te gusta programar o desarrollar software?"),
    ("matematicas", "¿Te gustan las matemáticas?"),
    ("analisis_datos", "¿Te interesa analizar datos y estadísticas?"),
    ("liderazgo", "¿Te gusta dirigir equipos?"),
    ("comunicacion", "¿Se te facilita comunicar ideas?"),
    ("organizacion", "¿Eres organizado y planificado?"),
    ("ciencias_naturales", "¿Te gustan temas de química y biología?"),
    ("vocacion_social", "¿Te gusta ayudar a las comunidades?"),
    ("optimizacion", "¿Te gusta mejorar procesos?"),
    ("creatividad", "¿Te consideras creativo?")
]

def consultar_prolog(atributos):

    lista = "[" + ",".join(atributos) + "]"
    consulta = f"consulta_sistema({lista},3),halt."

    resultado = subprocess.run(
        [
            SWIPL,
            "-q",
            "-f",
            PROLOG_FILE,
            "-g",
            consulta
        ],
        capture_output=True,
        text=True,
        encoding="utf-8"
    )

    carreras = []

    for linea in resultado.stdout.splitlines():

        if "|" in linea:
            nombre, puntos = linea.split("|")
            carreras.append((nombre.strip(), int(puntos)))

    return carreras


while True:

    print("\n" + "=" * 50)
    print("      ORIENTADOR VOCACIONAL ITSFCP")
    print("=" * 50)

    respuestas = []

    for atributo, pregunta in preguntas:

        while True:

            respuesta = input(f"\n{pregunta} (s/n): ").lower()

            if respuesta in ["s", "n"]:
                break

            print("Opción no válida. Escriba 's' o 'n'.")

        if respuesta == "s":
            respuestas.append(atributo)

    print("\nAnalizando respuestas...\n")

    carreras = consultar_prolog(respuestas)

    print("=" * 50)
    print("      CARRERAS RECOMENDADAS")
    print("=" * 50)

    for posicion, (nombre, puntos) in enumerate(carreras, start=1):

        print(f"\n{posicion}. {nombre}")
        print(f"   Puntaje: {puntos}")

    print("\n" + "=" * 50)
    print("1. Realizar otro test")
    print("2. Salir del sistema")
    print("=" * 50)

    opcion = input("Seleccione una opción: ")

    if opcion == "2":
        print("\nGracias por utilizar el Orientador Vocacional.")
        break