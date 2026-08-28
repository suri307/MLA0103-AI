% ============================================================
%       BANKING LOAN ELIGIBILITY EXPERT SYSTEM
%       Prolog-Based Decision Support System
% ============================================================

% ------------------------------------------------------------
% KNOWLEDGE BASE
% ------------------------------------------------------------

% customer(Name, Income, CreditScore, Employment, ExistingLoan, RepaymentHistory).

customer(suri, high, excellent, stable, no, good).
customer(ravi, medium, good, stable, no, good).
customer(rahul, low, poor, unstable, yes, poor).
customer(priya, high, good, stable, yes, good).
customer(anu, medium, poor, stable, no, average).

% ------------------------------------------------------------
% PRODUCTION RULES
% ------------------------------------------------------------

% Rule 1: Good credit
credit_ok(C) :-
    customer(C, _, excellent, _, _, _).

credit_ok(C) :-
    customer(C, _, good, _, _, _).

% Rule 2: Stable employment
employment_ok(C) :-
    customer(C, _, _, stable, _, _).

% Rule 3: Good repayment history
repayment_ok(C) :-
    customer(C, _, _, _, _, good).

% Rule 4: No existing loan
loan_status_ok(C) :-
    customer(C, _, _, _, no, _).

% Rule 5: High income
income_ok(C) :-
    customer(C, high, _, _, _, _).

% ------------------------------------------------------------
% FORWARD CHAINING
% ------------------------------------------------------------

forward_loan_decision(C) :-
    customer(C, Income, Credit, Employment, ExistingLoan, Repayment),

    nl,
    write('=========================================='), nl,
    write('        FORWARD CHAINING'), nl,
    write('=========================================='), nl,
    write('Customer: '), write(C), nl,
    nl,

    write('Initial Facts:'), nl,
    write('Income = '), write(Income), nl,
    write('Credit Score = '), write(Credit), nl,
    write('Employment = '), write(Employment), nl,
    write('Existing Loan = '), write(ExistingLoan), nl,
    write('Repayment History = '), write(Repayment), nl,
    nl,

    forward_rules(C).

forward_rules(C) :-
    income_ok(C),
    write('[RULE 1] Income condition satisfied.'), nl,

    credit_ok(C),
    write('[RULE 2] Credit score condition satisfied.'), nl,

    employment_ok(C),
    write('[RULE 3] Employment condition satisfied.'), nl,

    repayment_ok(C),
    write('[RULE 4] Repayment history condition satisfied.'), nl,

    loan_status_ok(C),
    write('[RULE 5] Existing loan condition satisfied.'), nl,

    write('------------------------------------------'), nl,
    write('FINAL DECISION: LOAN ELIGIBLE'), nl,
    write('------------------------------------------'), nl.

forward_rules(C) :-
    \+ income_ok(C),
    write('[RULE FAILED] Income condition not satisfied.'), nl,
    write('------------------------------------------'), nl,
    write('FINAL DECISION: LOAN NOT ELIGIBLE'), nl,
    write('------------------------------------------'), nl.

forward_rules(C) :-
    income_ok(C),
    \+ credit_ok(C),
    write('[RULE FAILED] Credit score condition not satisfied.'), nl,
    write('------------------------------------------'), nl,
    write('FINAL DECISION: LOAN NOT ELIGIBLE'), nl,
    write('------------------------------------------'), nl.

forward_rules(C) :-
    income_ok(C),
    credit_ok(C),
    \+ employment_ok(C),
    write('[RULE FAILED] Employment condition not satisfied.'), nl,
    write('------------------------------------------'), nl,
    write('FINAL DECISION: LOAN NOT ELIGIBLE'), nl,
    write('------------------------------------------'), nl.

forward_rules(C) :-
    income_ok(C),
    credit_ok(C),
    employment_ok(C),
    \+ repayment_ok(C),
    write('[RULE FAILED] Repayment history not satisfactory.'), nl,
    write('------------------------------------------'), nl,
    write('FINAL DECISION: LOAN NOT ELIGIBLE'), nl,
    write('------------------------------------------'), nl.

forward_rules(C) :-
    income_ok(C),
    credit_ok(C),
    employment_ok(C),
    repayment_ok(C),
    \+ loan_status_ok(C),
    write('[RULE FAILED] Existing loan condition not satisfied.'), nl,
    write('------------------------------------------'), nl,
    write('FINAL DECISION: LOAN NOT ELIGIBLE'), nl,
    write('------------------------------------------'), nl.

% ------------------------------------------------------------
% BACKWARD CHAINING
% ------------------------------------------------------------

backward_loan_decision(C) :-
    nl,
    write('=========================================='), nl,
    write('        BACKWARD CHAINING'), nl,
    write('=========================================='), nl,
    write('Customer: '), write(C), nl,
    nl,

    write('Goal: loan_eligible('),
    write(C),
    write(')'), nl,
    nl,

    (   loan_eligible(C)
    ->  write('Goal satisfied.'), nl,
        write('------------------------------------------'), nl,
        write('FINAL DECISION: LOAN ELIGIBLE'), nl,
        write('------------------------------------------'), nl
    ;   write('Goal cannot be satisfied.'), nl,
        write('------------------------------------------'), nl,
        write('FINAL DECISION: LOAN NOT ELIGIBLE'), nl,
        write('------------------------------------------'), nl
    ).

% Main backward-chaining rule
loan_eligible(C) :-
    income_ok(C),
    credit_ok(C),
    employment_ok(C),
    repayment_ok(C),
    loan_status_ok(C).

% ------------------------------------------------------------
% EXPLANATION
% ------------------------------------------------------------

explain(C) :-
    customer(C, Income, Credit, Employment, ExistingLoan, Repayment),

    nl,
    write('=========================================='), nl,
    write('          LOAN DECISION EXPLANATION'), nl,
    write('=========================================='), nl,
    write('Customer: '), write(C), nl,
    nl,

    write('Income: '), write(Income), nl,
    write('Credit Score: '), write(Credit), nl,
    write('Employment: '), write(Employment), nl,
    write('Existing Loan: '), write(ExistingLoan), nl,
    write('Repayment History: '), write(Repayment), nl,
    nl,

    write('Reasoning:'), nl,

    explain_income(C),
    explain_credit(C),
    explain_employment(C),
    explain_repayment(C),
    explain_existing_loan(C),

    nl,
    ( loan_eligible(C)
    -> write('Conclusion: Customer is ELIGIBLE for the loan.')
    ;  write('Conclusion: Customer is NOT ELIGIBLE for the loan.')
    ),
    nl.

explain_income(C) :-
    income_ok(C),
    write('- Income requirement satisfied.'), nl.

explain_income(C) :-
    \+ income_ok(C),
    write('- Income requirement NOT satisfied.'), nl.

explain_credit(C) :-
    credit_ok(C),
    write('- Credit score requirement satisfied.'), nl.

explain_credit(C) :-
    \+ credit_ok(C),
    write('- Credit score requirement NOT satisfied.'), nl.

explain_employment(C) :-
    employment_ok(C),
    write('- Employment requirement satisfied.'), nl.

explain_employment(C) :-
    \+ employment_ok(C),
    write('- Employment requirement NOT satisfied.'), nl.

explain_repayment(C) :-
    repayment_ok(C),
    write('- Repayment history is satisfactory.'), nl.

explain_repayment(C) :-
    \+ repayment_ok(C),
    write('- Repayment history is NOT satisfactory.'), nl.

explain_existing_loan(C) :-
    loan_status_ok(C),
    write('- No existing loan condition satisfied.'), nl.

explain_existing_loan(C) :-
    \+ loan_status_ok(C),
    write('- Existing loan condition NOT satisfied.'), nl.

% ------------------------------------------------------------
% TEST CASES
% ------------------------------------------------------------

test1 :-
    forward_loan_decision(suri).

test2 :-
    forward_loan_decision(ravi).

test3 :-
    forward_loan_decision(rahul).

test4 :-
    forward_loan_decision(priya).

test5 :-
    forward_loan_decision(anu).

% ------------------------------------------------------------
% SHOW ALL CUSTOMERS
% ------------------------------------------------------------

show_customers :-
    nl,
    write('=========================================='), nl,
    write('          CUSTOMER DATABASE'), nl,
    write('=========================================='), nl,
    customer(Name, Income, Credit, Employment, Loan, Repayment),
    write(Name), write(' -> '),
    write(Income), write(', '),
    write(Credit), write(', '),
    write(Employment), write(', '),
    write(Loan), write(', '),
    write(Repayment), nl,
    fail.

show_customers.