at(monkey, door).
at(box, window).
at(banana, middle).

move(monkey, door, window).
push(box, window, middle).
climb(box).
get(banana).

can_get_banana :-
    move(monkey, door, window),
    write('Monkey moves from door to window'), nl,
    push(box, window, middle),
    write('Monkey pushes box to middle'), nl,
    climb(box),
    write('Monkey climbs onto the box'), nl,
    get(banana),
    write('Monkey gets the banana'), nl.