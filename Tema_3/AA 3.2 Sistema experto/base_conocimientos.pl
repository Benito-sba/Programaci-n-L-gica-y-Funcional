%Benito Santiago Balam Acevedo
%Adan Adair Moo NOH
%AA 3.2 Sistema experto


carrera(sistemas).
carrera(datos).
carrera(administracion).
carrera(industrial).
carrera(alimentarias).
carrera(comunitario).
carrera(empresarial).


nombre(sistemas,'Ingenieria en Sistemas Computacionales').
nombre(datos,'Ingenieria en Ciencia de Datos').
nombre(administracion,'Ingenieria en Administracion').
nombre(industrial,'Ingenieria Industrial').
nombre(alimentarias,'Ingenieria en Industrias Alimentarias').
nombre(comunitario,'Ingenieria en Desarrollo Comunitario').
nombre(empresarial,'Ingenieria en Gestion Empresarial').

habilidad(sistemas,programacion).
habilidad(sistemas,matematicas).

habilidad(sistemas,tecnologia).
habilidad(sistemas,resolucion_problemas).

habilidad(datos,programacion).
habilidad(datos,matematicas).
habilidad(datos,analisis_datos).

habilidad(administracion,liderazgo).
habilidad(administracion,comunicacion).
habilidad(administracion,organizacion).

habilidad(industrial,matematicas).
habilidad(industrial,organizacion).
habilidad(industrial,optimizacion).

habilidad(alimentarias,ciencias_naturales).

habilidad(comunitario,vocacion_social).
habilidad(comunitario,comunicacion).
habilidad(comunitario,creatividad).

habilidad(empresarial,liderazgo).
habilidad(empresarial,organizacion).
habilidad(empresarial,comunicacion).


puntaje(Carrera, Atributos, Puntos) :-
    findall(
        1,
        (
            member(A, Atributos),
            habilidad(Carrera, A)
        ),
        Lista
    ),
    length(Lista, Puntos).


resultado(Atributos, Carrera, Puntos) :-
    carrera(Carrera),
    puntaje(Carrera, Atributos, Puntos),
    Puntos > 0. % Solo tomamos en cuenta carreras con al menos 1 coincidencia


consulta_sistema(Atributos, N) :-
    findall(
        P-C,
        resultado(Atributos, C, P),
        Lista
    ),
    msort(Lista, Ordenada),
    reverse(Ordenada, Final),
    
    obtener_top(N, Final, Top),

    forall(
        member(P-C, Top),
        (
            nombre(C, Nombre),
            format("~w|~w~n", [Nombre, P])
        )
    ).

obtener_top(0, _, []) :- !.
obtener_top(_, [], []) :- !.
obtener_top(N, [X|Xs], [X|Ys]) :-
    N > 0,
    N1 is N - 1,
    obtener_top(N1, Xs, Ys).