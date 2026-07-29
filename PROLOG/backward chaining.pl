% Facts
male(john).
female(mary).
parent(john, mary).
parent(mary, alice).

% Rules
mother(X, Y) :-
    female(X),
    parent(X, Y).

father(X, Y) :-
    male(X),
    parent(X, Y).

grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).