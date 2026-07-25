disease(diabetes, sugar_free_diet).
disease(bp, low_salt_diet).
disease(obesity, low_fat_diet).
disease(fever, liquid_diet).
disease(anemia, iron_rich_diet).

diet(X,Y) :-
    disease(X,Y).