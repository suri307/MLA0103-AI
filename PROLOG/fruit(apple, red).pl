fruit(apple, red).
fruit(banana, yellow).
fruit(grapes, green).
fruit(orange, orange).
fruit(mango, yellow).

color(Fruit, Color) :-
    fruit(Fruit, Color).