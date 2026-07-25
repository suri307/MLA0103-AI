% 1. John likes all kinds of food.
likes(john, X) :- food(X).

% 2. Apple and vegetables are food.
food(apple).
food(vegetable).

% 3. Anything that someone eats and is not killed by is food.
food(X) :-
    eats(Y, X),
    alive(Y).

% 4. Anil eats peanuts and is still alive.
eats(anil, peanuts).
alive(anil).

% 5. Harry eats everything that Anil eats.
eats(harry, X) :-
    eats(anil, X).

% 6. John likes peanuts.
likes(john, peanuts).