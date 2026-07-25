edge(a,b,4).
edge(a,c,2).
edge(b,d,5).
edge(c,e,3).
edge(e,f,1).

best_first(X,Y,Cost) :-
    edge(X,Y,Cost).