% Facts
man(marcus).
pompeian(marcus).
ruler(caesar).
tried_to_assassinate(marcus, caesar).

% Rules
roman(X) :- pompeian(X).
person(X) :- man(X).

% Marcus is not loyal if he tried to assassinate Caesar
not_loyal(X, Y) :-
    tried_to_assassinate(X, Y).

% Romans who are not loyal hate Caesar
hates(X, caesar) :-
    roman(X),
    not_loyal(X, caesar).

% Loyal people are Romans who do not hate Caesar
loyal_to(X, caesar) :-
    roman(X),
    \+ hates(X, caesar).