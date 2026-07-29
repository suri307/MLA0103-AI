fact(rain).
fact(cloudy).
fact(wet_ground).

rule([rain], umbrella).
rule([cloudy], rain).
rule([wet_ground], slippery).

forward_chain :-
    write('Starting Forward Chaining...'), nl,
    fc_loop([]).

fc_loop(DerivedFacts) :-
    ( apply_rules(DerivedFacts, NewFacts),
      NewFacts \= [] ->
        append(DerivedFacts, NewFacts, UpdatedFacts),
        write('Derived: '), write(NewFacts), nl,
        fc_loop(UpdatedFacts)
    ; write('No more new facts.'), nl,
      write('Final derived facts: '), write(DerivedFacts), nl
    ).

apply_rules(DerivedFacts, NewFacts) :-
    findall(Conclusion,
        ( rule(Conditions, Conclusion),
          all_true(Conditions, DerivedFacts),
          \+ member(Conclusion, DerivedFacts),
          \+ fact(Conclusion)
        ),
        NewFacts).

all_true([], _).
all_true([Cond|Rest], Facts) :-
    ( fact(Cond) ; member(Cond, Facts) ),
    all_true(Rest, Facts).
