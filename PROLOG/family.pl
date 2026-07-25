male(tom).
male(bob).
male(jim).

female(pam).
female(liz).
female(ann).
female(pat).

parent(pam,bob).
parent(tom,bob).
parent(pam,liz).
parent(tom,liz).
parent(bob,ann).
parent(bob,pat).
parent(ann,jim).

mother(X,Y) :-
    parent(X,Y),
    female(X).

father(X,Y) :-
    parent(X,Y),
    male(X).

grandfather(X,Y) :-
    father(X,Z),
    parent(Z,Y).

grandmother(X,Y) :-
    mother(X,Z),
    parent(Z,Y).

sister(X,Y) :-
    female(X),
    parent(P,X),
    parent(P,Y),
    X \= Y.

brother(X,Y) :-
    male(X),
    parent(P,X),
    parent(P,Y),
    X \= Y.