bird(parrot).
bird(pigeon).
bird(sparrow).
bird(peacock).
bird(penguin).
bird(ostrich).

can_fly(X) :-
    bird(X),
    X \= penguin,
    X \= ostrich.