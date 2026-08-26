% =========================================================
% STUDENT ACADEMIC ADVISORY EXPERT SYSTEM
% =========================================================

:- dynamic student/5.
:- dynamic derived/1.


% =========================================================
% 1. STUDENT FACTS
% =========================================================

student(rahul, low, low, poor, yes).
student(priya, high, high, good, no).
student(arun, low, high, poor, no).
student(meena, high, low, good, yes).

% YOUR TEST STUDENT
student(suri, low, low, poor, yes).


% =========================================================
% 2. PRODUCTION RULES
% =========================================================

% Rule 1: Low attendance and low marks
academic_risk(Name) :-
    student(Name, low, low, _, _).

% Rule 2: Low attendance and poor assignments
academic_risk(Name) :-
    student(Name, low, _, poor, _).

% Rule 3: Low attendance
attendance_improvement(Name) :-
    student(Name, low, _, _, _).

% Rule 4: Learning difficulty
extra_learning_support(Name) :-
    student(Name, _, _, _, yes).

% Rule 5: Poor assignments
assignment_support(Name) :-
    student(Name, _, _, poor, _).

% Rule 6: Academic risk
faculty_counselling(Name) :-
    academic_risk(Name).

% Rule 7: Good performance
overall_good_performance(Name) :-
    student(Name, high, high, good, no).


% =========================================================
% 3. FORWARD CHAINING
% =========================================================

forward_chaining(Name) :-

    retractall(derived(_)),

    nl,
    write('=========================================='), nl,
    write('          FORWARD CHAINING'), nl,
    write('=========================================='), nl,

    student(Name, Attendance, Marks, Assignment, Difficulty),

    write('Initial Facts'), nl,
    write('Student: '),
    write(Name), nl,

    write('Attendance: '),
    write(Attendance), nl,

    write('Internal Marks: '),
    write(Marks), nl,

    write('Assignment Performance: '),
    write(Assignment), nl,

    write('Learning Difficulty: '),
    write(Difficulty), nl,
    nl,

    apply_forward_rules(Name),

    write('------------------------------------------'), nl,
    write('Derived Conclusions'), nl,
    write('------------------------------------------'), nl,

    show_derived.


% =========================================================
% FORWARD RULE PROCESSING
% =========================================================

apply_forward_rules(Name) :-

    student(Name, low, low, _, _),
    \+ derived(academic_risk),

    assertz(derived(academic_risk)),

    write('Rule 1 Fired:'), nl,
    write('Low attendance + Low internal marks'), nl,
    write('=> Academic Risk'), nl,
    nl,

    fail.


apply_forward_rules(Name) :-

    student(Name, low, _, poor, _),
    \+ derived(academic_risk),

    assertz(derived(academic_risk)),

    write('Rule 2 Fired:'), nl,
    write('Low attendance + Poor assignments'), nl,
    write('=> Academic Risk'), nl,
    nl,

    fail.


apply_forward_rules(Name) :-

    student(Name, low, _, _, _),
    \+ derived(attendance_improvement),

    assertz(derived(attendance_improvement)),

    write('Rule 3 Fired:'), nl,
    write('Low attendance'), nl,
    write('=> Improve Attendance'), nl,
    nl,

    fail.


apply_forward_rules(Name) :-

    student(Name, _, _, _, yes),
    \+ derived(extra_learning_support),

    assertz(derived(extra_learning_support)),

    write('Rule 4 Fired:'), nl,
    write('Learning difficulty detected'), nl,
    write('=> Extra Learning Support'), nl,
    nl,

    fail.


apply_forward_rules(Name) :-

    student(Name, _, _, poor, _),
    \+ derived(assignment_support),

    assertz(derived(assignment_support)),

    write('Rule 5 Fired:'), nl,
    write('Poor assignment performance'), nl,
    write('=> Assignment Support'), nl,
    nl,

    fail.


apply_forward_rules(_) :-

    derived(academic_risk),
    \+ derived(faculty_counselling),

    assertz(derived(faculty_counselling)),

    write('Rule 6 Fired:'), nl,
    write('Academic risk detected'), nl,
    write('=> Faculty Counselling'), nl,
    nl,

    fail.


apply_forward_rules(Name) :-

    student(Name, high, high, good, no),
    \+ derived(overall_good_performance),

    assertz(derived(overall_good_performance)),

    write('Rule 7 Fired:'), nl,
    write('High attendance + High marks + Good assignments'), nl,
    write('=> Overall Good Performance'), nl,
    nl,

    fail.


% Stop processing when no more rules can fire
apply_forward_rules(_).


% =========================================================
% DISPLAY FORWARD CONCLUSIONS
% =========================================================

show_derived :-

    derived(Fact),

    write('-> '),
    write(Fact),
    nl,

    fail.

show_derived.


% =========================================================
% 4. BACKWARD CHAINING
% =========================================================

backward_chaining(Name) :-

    nl,
    write('=========================================='), nl,
    write('          BACKWARD CHAINING'), nl,
    write('=========================================='), nl,

    write('Goal-driven reasoning:'), nl,
    nl,

    check_goal(Name, academic_risk),
    check_goal(Name, attendance_improvement),
    check_goal(Name, extra_learning_support),
    check_goal(Name, assignment_support),
    check_goal(Name, faculty_counselling),
    check_goal(Name, overall_good_performance),

    nl,
    write('Backward chaining completed.'), nl.


% =========================================================
% CHECK GOALS
% =========================================================

check_goal(Name, Goal) :-

    call(Goal, Name),

    write('Goal: '),
    write(Goal),
    write(' -> TRUE'),
    nl,

    !.


check_goal(_, Goal) :-

    write('Goal: '),
    write(Goal),
    write(' -> FALSE'),
    nl.


% =========================================================
% 5. COMPLETE ADVISOR
% =========================================================

advisor(Name) :-

    student(Name, _, _, _, _),

    nl,
    write('=========================================='), nl,
    write('      STUDENT ACADEMIC ADVISOR'), nl,
    write('=========================================='), nl,

    write('Student: '),
    write(Name),
    nl,

    forward_chaining(Name),

    backward_chaining(Name),

    nl,
    write('=========================================='), nl,
    write('          FINAL ADVISORY REPORT'), nl,
    write('=========================================='), nl,

    show_recommendations(Name).


% =========================================================
% UNKNOWN STUDENT HANDLING
% =========================================================

advisor(Name) :-

    \+ student(Name, _, _, _, _),

    nl,
    write('=========================================='), nl,
    write('           STUDENT NOT FOUND'), nl,
    write('=========================================='), nl,

    write('No academic information found for: '),
    write(Name),
    nl,

    write('Please enter a student available in the knowledge base.'), nl.


% =========================================================
% 6. RECOMMENDATIONS
% =========================================================

show_recommendations(Name) :-

    nl,
    write('Recommendations:'), nl,
    nl,

    show_attendance(Name),
    show_learning(Name),
    show_assignment(Name),
    show_counselling(Name),
    show_risk(Name),
    show_good_performance(Name).


show_attendance(Name) :-

    attendance_improvement(Name),

    write('[1] Improve Attendance'),
    nl,

    !.

show_attendance(_).


show_learning(Name) :-

    extra_learning_support(Name),

    write('[2] Provide Extra Learning Support'),
    nl,

    !.

show_learning(_).


show_assignment(Name) :-

    assignment_support(Name),

    write('[3] Improve Assignment Performance'),
    nl,

    !.

show_assignment(_).


show_counselling(Name) :-

    faculty_counselling(Name),

    write('[4] Faculty Counselling Recommended'),
    nl,

    !.

show_counselling(_).


show_risk(Name) :-

    academic_risk(Name),

    write('[5] Student Requires Academic Attention'),
    nl,

    !.

show_risk(_).


show_good_performance(Name) :-

    overall_good_performance(Name),

    write('[6] Student is Performing Well'),
    nl,

    !.

show_good_performance(_).


% =========================================================
% 7. TEST CASES
% =========================================================

test :-

    nl,
    write('=========================================='), nl,
    write('             TEST CASES'), nl,
    write('=========================================='), nl,

    nl,
    write('========== TEST CASE 1: RAHUL =========='), nl,
    advisor(rahul),

    nl,
    write('========== TEST CASE 2: PRIYA =========='), nl,
    advisor(priya),

    nl,
    write('========== TEST CASE 3: ARUN =========='), nl,
    advisor(arun),

    nl,
    write('========== TEST CASE 4: MEENA =========='), nl,
    advisor(meena),

    nl,
    write('========== TEST CASE 5: SURI =========='), nl,
    advisor(suri).