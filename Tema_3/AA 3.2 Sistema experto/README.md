# Sistema Experto de Orientación Vocacional

## Descripción

El Sistema Experto de Orientación Vocacional es una aplicación desarrollada utilizando **Python** y **Prolog** que tiene como objetivo apoyar a los estudiantes en la selección de una carrera profesional de acuerdo con sus intereses, habilidades y preferencias.

El sistema realiza una serie de preguntas relacionadas con áreas de conocimiento, habilidades personales y aptitudes. A partir de las respuestas proporcionadas por el usuario, el motor de inferencia desarrollado en Prolog analiza las coincidencias entre las características del estudiante y los perfiles de diversas carreras ofertadas por el Instituto Tecnológico Superior de Felipe Carrillo Puerto (ITSFCP).

Finalmente, el sistema muestra las tres carreras que mejor se ajustan al perfil del usuario, permitiendo una toma de decisiones más informada sobre su futuro académico y profesional.

---

# Objetivo

Brindar una herramienta de apoyo para estudiantes que presentan dudas sobre qué carrera estudiar, utilizando técnicas de Inteligencia Artificial basadas en Sistemas Expertos.

---

# ¿Cómo funciona?

El sistema está compuesto por dos partes principales:

## Base de conocimientos (Prolog)

La base de conocimientos almacena:

* Carreras disponibles.
* Habilidades asociadas a cada carrera.
* Reglas para calcular coincidencias.
* Motor de inferencia para determinar las mejores recomendaciones.

Ejemplo:

```prolog
habilidad(sistemas,programacion).
habilidad(sistemas,matematicas).

habilidad(datos,analisis_datos).
```

---

## Interfaz de usuario (Python)

Python se encarga de:

* Mostrar las preguntas al usuario.
* Capturar las respuestas.
* Enviar los resultados a Prolog.
* Recibir las recomendaciones generadas.
* Mostrar las tres carreras recomendadas.

La comunicación entre Python y Prolog se realiza mediante la librería `subprocess`, que ejecuta SWI-Prolog desde Python y recupera los resultados generados por el motor experto.

---

# Carreras consideradas

El sistema puede recomendar las siguientes carreras:

* Ingeniería en Sistemas Computacionales
* Ingeniería en Ciencia de Datos
* Ingeniería en Administración
* Ingeniería Industrial
* Ingeniería en Industrias Alimentarias
* Ingeniería en Desarrollo Comunitario
* Ingeniería en Gestión Empresarial

---

# Beneficios para los estudiantes

Este sistema puede ayudar a los estudiantes que:

* Tienen dudas sobre qué carrera elegir.
* Desconocen qué área profesional se adapta mejor a sus habilidades.
* Desean explorar opciones académicas basadas en sus intereses.
* Buscan una orientación inicial antes de tomar una decisión profesional.

Entre sus ventajas se encuentran:

* Evaluación rápida y sencilla.
* Recomendaciones personalizadas.
* Apoyo en el proceso de orientación vocacional.
* Uso de técnicas de Inteligencia Artificial mediante Sistemas Expertos.

---

# Tecnologías utilizadas

* Python 3
* SWI-Prolog
* Sistemas Expertos
* Programación Lógica

---

# Estructura del proyecto

```text
Proyecto/
│
├── orientador.py
├── base_conocimientos.pl
└── README.md
```

---

# Requisitos

Antes de ejecutar el proyecto es necesario instalar:

## Python

Verificar instalación:

```bash
python --version
```

## SWI-Prolog

Descargar desde:

https://www.swi-prolog.org/download/stable

Verificar instalación:

```bash
swipl --version
```

---

# Configuración

Verificar que la ruta de SWI-Prolog sea correcta dentro del archivo `orientador.py`:

```python
SWIPL = r"C:\Program Files\swipl\bin\swipl.exe"
```

Si SWI-Prolog está instalado en otra ubicación, actualizar la ruta correspondiente.

---

# Instrucciones de ejecución

## 1. Abrir una terminal

Ubicarse en la carpeta del proyecto:

```bash
cd ruta_del_proyecto
```

Ejemplo:

```bash
cd C:\Users\Usuario\Documents\OrientadorVocacional
```

---

## 2. Ejecutar el sistema

```bash
python orientador.py
```

---

## 3. Responder las preguntas

Ejemplo:

```text
¿Te gusta programar o desarrollar software? (s/n): s
¿Te gustan las matemáticas? (s/n): s
¿Te interesa analizar datos y estadísticas? (s/n): s
```

---

## 4. Obtener recomendaciones

Ejemplo:

```text
==================================================
      CARRERAS RECOMENDADAS
==================================================

1. Ingenieria en Ciencia de Datos
   Puntaje: 3

2. Ingenieria en Sistemas Computacionales
   Puntaje: 2

3. Ingenieria Industrial
   Puntaje: 1
```

---

## 5. Elegir una opción

```text
==================================================
1. Realizar otro test
2. Salir del sistema
==================================================
Seleccione una opción:
```

* Opción 1: Realizar nuevamente la evaluación.
* Opción 2: Finalizar el programa.

---

# Autor

Benito Santiago Balam Acevedo

Adan Adair Moo Noh

Instituto Tecnológico Superior de Felipe Carrillo Puerto

Ingeniería en Sistemas Computacionales

