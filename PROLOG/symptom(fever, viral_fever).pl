symptom(fever, viral_fever).
symptom(cough, cold).
symptom(headache, migraine).
symptom(chest_pain, heart_disease).
symptom(stomach_pain, gastritis).

diagnosis(Symptom, Disease) :-
    symptom(Symptom, Disease).