fact(fever).
fact(cough).

disease(flu) :-
    fact(fever),
    fact(cough).

disease(viral_fever) :-
    fact(fever).

forward :-
    disease(D),
    write('Disease is: '),
    write(D), nl.