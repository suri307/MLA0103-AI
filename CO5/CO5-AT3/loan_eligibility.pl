% =========================================================
%        BANKING LOAN ELIGIBILITY EXPERT SYSTEM
% =========================================================

% =========================================================
% 1. FACTS
% =========================================================

% customer(Name, Income, CreditScore, Employment,
%          ExistingLoan, RepaymentHistory).

customer(suri,  high,   excellent, employed,   no,  good).
customer(rahul, medium, good,      employed,   no,  good).
customer(priya, high,   good,      employed,   yes, good).
customer(arun,  medium, poor,      employed,   no,  poor).
customer(raj,   low,    poor,      unemployed, yes, poor).


% =========================================================
% 2. SUPPORTING PREDICATES
% =========================================================

suitable_income(high).
suitable_income(medium).

suitable_credit(excellent).
suitable_credit(good).

suitable_employment(employed).

suitable_existing_loan(no).

suitable_repayment(good).


% =========================================================
% 3. LOAN ELIGIBILITY RULE
% =========================================================

loan_eligible(Name) :-
    customer(Name, Income, Credit, Employment, Loan, Repayment),
    suitable_income(Income),
    suitable_credit(Credit),
    suitable_employment(Employment),
    suitable_existing_loan(Loan),
    suitable_repayment(Repayment).


% =========================================================
% 4. LOAN NOT ELIGIBLE RULE
% =========================================================

loan_not_eligible(Name) :-
    customer(Name, _, _, _, _, _),
    \+ loan_eligible(Name).


% =========================================================
% 5. LOAN STATUS
% =========================================================

loan_status(Name) :-
    loan_eligible(Name),
    write('===================================='), nl,
    write('       BANKING LOAN DECISION'), nl,
    write('===================================='), nl,
    write('Applicant: '), write(Name), nl,
    write('Loan Status: ELIGIBLE'), nl,
    write('Reason: All eligibility conditions are satisfied.'), nl,
    write('===================================='), nl.

loan_status(Name) :-
    loan_not_eligible(Name),
    write('===================================='), nl,
    write('       BANKING LOAN DECISION'), nl,
    write('===================================='), nl,
    write('Applicant: '), write(Name), nl,
    write('Loan Status: NOT ELIGIBLE'), nl,
    write('Reason: One or more eligibility conditions are not satisfied.'), nl,
    write('===================================='), nl.


% =========================================================
% 6. FORWARD CHAINING DEMONSTRATION
% =========================================================

forward_chaining(Name) :-
    customer(Name, Income, Credit, Employment, Loan, Repayment),

    write('=========================================='), nl,
    write('       FORWARD CHAINING DEMONSTRATION'), nl,
    write('=========================================='), nl,

    write('Initial Facts:'), nl,
    write('1. Income = '), write(Income), nl,
    write('2. Credit Score = '), write(Credit), nl,
    write('3. Employment = '), write(Employment), nl,
    write('4. Existing Loan = '), write(Loan), nl,
    write('5. Repayment History = '), write(Repayment), nl,
    nl,

    write('Inference Steps:'), nl,

    suitable_income(Income),
    write('Step 1: Suitable income confirmed.'), nl,

    suitable_credit(Credit),
    write('Step 2: Suitable credit score confirmed.'), nl,

    suitable_employment(Employment),
    write('Step 3: Employment condition confirmed.'), nl,

    suitable_existing_loan(Loan),
    write('Step 4: No existing loan confirmed.'), nl,

    suitable_repayment(Repayment),
    write('Step 5: Good repayment history confirmed.'), nl,

    nl,
    write('Conclusion: Loan is ELIGIBLE.'), nl,
    write('=========================================='), nl.


% =========================================================
% 7. BACKWARD CHAINING DEMONSTRATION
% =========================================================

backward_chaining(Name) :-
    write('=========================================='), nl,
    write('       BACKWARD CHAINING DEMONSTRATION'), nl,
    write('=========================================='), nl,

    write('Goal: Determine whether '),
    write(Name),
    write(' is eligible for a loan.'), nl,
    nl,

    write('Checking required conditions:'), nl,

    customer(Name, Income, Credit, Employment, Loan, Repayment),

    write('1. Checking income... '),
    suitable_income(Income),
    write('Satisfied ('), write(Income), write(').'), nl,

    write('2. Checking credit score... '),
    suitable_credit(Credit),
    write('Satisfied ('), write(Credit), write(').'), nl,

    write('3. Checking employment... '),
    suitable_employment(Employment),
    write('Satisfied ('), write(Employment), write(').'), nl,

    write('4. Checking existing loan... '),
    suitable_existing_loan(Loan),
    write('Satisfied ('), write(Loan), write(').'), nl,

    write('5. Checking repayment history... '),
    suitable_repayment(Repayment),
    write('Satisfied ('), write(Repayment), write(').'), nl,

    nl,
    write('All required conditions are satisfied.'), nl,
    write('Conclusion: Loan is ELIGIBLE.'), nl,
    write('=========================================='), nl.