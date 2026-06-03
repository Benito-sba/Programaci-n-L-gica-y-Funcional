/*AA 3.1 Reporte de Practica Benito Santiago Balam Acevedo*/

% hechos que representan el arbol

mujer(isolina).
hombre(cristian).
hombre(placido).
hombre(benito).

madre(isolina, cristian).
madre(isolina, placido).
madre(isolina, benito).

% Datos sobre empleados
empleado(beto, 45, ingeniero).
empleado(mariana, 38, analista).
empleado(erick, 40, gerente).


%Crear regla para consultar empleados menores a 40 años

joven(Persona):- empleado(Persona, Edad, _), Edad < 40.

%Pregunta y respuesta
saludo_respuesta(Saludo) :-
    member(Saludo, ["Hola", "Como estas?", "Buenos dias", "Que tal?"]),
    responder_saludo(Saludo).

responder_saludo("Hola") :-
    write('Hola! En que puedo ayudarte?'), nl.
responder_saludo("Como estas?") :-
    write('Estoy bien, gracias por preguntar.'), nl.
responder_saludo("Buenos dias") :-
    write('Buenos dias! Como puedo ayudarte hoy?'), nl.
responder_saludo("Que tal?") :-
    write('Todo bien, y tu?'), nl.
responder_saludo(_) :-
    write('Lo siento, no entendi tu saludo.'), nl.
