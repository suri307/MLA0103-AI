# ================================================================
# INTELLIGENT EMERGENCY MEDICAL DECISION-SUPPORT AGENT
# Using Search, Logic and Expert-System Techniques
#
# Course: MLA01 - Artificial Intelligence and Expert Systems
#
# Educational Prototype Only
# This system is NOT a medical diagnosis or treatment system.
# It is designed only for academic decision-support demonstration.
# ================================================================


from heapq import heappush, heappop


# ================================================================
# 1. PATIENT DATA
# ================================================================

patients = {

    "P1": {
        "symptoms": [
            "chest_pain",
            "sweating",
            "shortness_of_breath"
        ],
        "heart_rate": "high",
        "oxygen": "normal",
        "temperature": "normal",
        "history": ["hypertension"]
    },

    "P2": {
        "symptoms": [
            "high_fever",
            "cough",
            "breathing_difficulty"
        ],
        "heart_rate": "normal",
        "oxygen": "low",
        "temperature": "high",
        "history": []
    },

    "P3": {
        "symptoms": [
            "severe_headache",
            "one_sided_weakness"
        ],
        "heart_rate": "normal",
        "oxygen": "normal",
        "temperature": "normal",
        "blood_pressure": "high",
        "history": ["hypertension"]
    },

    "P4": {
        "symptoms": [
            "abdominal_pain",
            "vomiting",
            "fever"
        ],
        "heart_rate": "normal",
        "oxygen": "normal",
        "temperature": "high",
        "history": []
    }
}


# ================================================================
# 2. PROPOSITIONAL LOGIC KNOWLEDGE BASE
# ================================================================

propositional_rules = [

    # Cardiac rules
    (
        "R1",
        {"chest_pain"},
        "cardiac_risk"
    ),

    (
        "R2",
        {"chest_pain", "sweating"},
        "cardiac_warning"
    ),

    (
        "R3",
        {"cardiac_risk", "shortness_of_breath"},
        "very_high_risk"
    ),

    # Respiratory rules
    (
        "R4",
        {"high_fever", "low_oxygen"},
        "respiratory_risk"
    ),

    (
        "R5",
        {"breathing_difficulty", "low_oxygen"},
        "urgent_respiratory_assessment"
    ),

    # Neurological rules
    (
        "R6",
        {"severe_headache", "one_sided_weakness"},
        "neurological_risk"
    ),

    (
        "R7",
        {"neurological_risk", "high_blood_pressure"},
        "urgent_neurological_assessment"
    ),

    # Abdominal rules
    (
        "R8",
        {"abdominal_pain", "vomiting"},
        "abdominal_risk"
    ),

    (
        "R9",
        {"abdominal_risk", "fever"},
        "infection_risk"
    ),

    (
        "R10",
        {"infection_risk"},
        "medical_assessment_required"
    ),

    # Priority rules
    (
        "R11",
        {"very_high_risk"},
        "immediate_attention"
    ),

    (
        "R12",
        {"urgent_respiratory_assessment"},
        "high_priority"
    ),

    (
        "R13",
        {"urgent_neurological_assessment"},
        "high_priority"
    )
]


# ================================================================
# 3. FIRST-ORDER LOGIC FACTS
# ================================================================

fol_facts = [

    ("has_symptom", "P1", "chest_pain"),
    ("has_symptom", "P1", "sweating"),
    ("has_symptom", "P1", "shortness_of_breath"),
    ("has_history", "P1", "hypertension"),

    ("has_symptom", "P2", "high_fever"),
    ("has_symptom", "P2", "cough"),
    ("has_symptom", "P2", "breathing_difficulty"),
    ("has_measurement", "P2", "low_oxygen"),

    ("has_symptom", "P3", "severe_headache"),
    ("has_symptom", "P3", "one_sided_weakness"),
    ("has_measurement", "P3", "high_blood_pressure"),
    ("has_history", "P3", "hypertension"),

    ("has_symptom", "P4", "abdominal_pain"),
    ("has_symptom", "P4", "vomiting"),
    ("has_symptom", "P4", "fever")
]


# ================================================================
# 4. FIRST-ORDER LOGIC RULES
# ================================================================

fol_rules = [

    (
        ("has_symptom", "X", "chest_pain"),
        ("possible_condition", "X", "cardiac_risk")
    ),

    (
        ("has_symptom", "X", "one_sided_weakness"),
        ("possible_condition", "X", "neurological_risk")
    ),

    (
        ("has_measurement", "X", "low_oxygen"),
        ("possible_condition", "X", "respiratory_risk")
    ),

    (
        ("has_symptom", "X", "abdominal_pain"),
        ("possible_condition", "X", "abdominal_risk")
    )
]


# ================================================================
# 5. CREATE PATIENT FACTS
# ================================================================

def create_facts(patient):

    data = patients[patient]

    facts = set()

    # Add symptoms
    for symptom in data["symptoms"]:
        facts.add(symptom)

    # Add vital-related facts
    if data.get("heart_rate") == "high":
        facts.add("high_heart_rate")

    if data.get("oxygen") == "low":
        facts.add("low_oxygen")

    if data.get("temperature") == "high":
        facts.add("high_fever")

    if data.get("blood_pressure") == "high":
        facts.add("high_blood_pressure")

    # Add history facts
    if "hypertension" in data.get("history", []):
        facts.add("hypertension_history")

    return facts


# ================================================================
# 6. FORWARD CHAINING
# ================================================================

def forward_chaining(initial_facts):

    facts = set(initial_facts)

    fired_rules = []

    changed = True

    while changed:

        changed = False

        for rule_number, conditions, conclusion in propositional_rules:

            if conditions.issubset(facts):

                if conclusion not in facts:

                    facts.add(conclusion)

                    fired_rules.append(rule_number)

                    changed = True

    return facts, fired_rules


# ================================================================
# 7. BACKWARD CHAINING
# ================================================================

def backward_chaining(goal, facts, visited=None):

    if visited is None:
        visited = set()

    # Goal already known
    if goal in facts:

        return True, [
            "FACT: " + goal
        ]

    # Avoid loops
    if goal in visited:

        return False, []

    visited.add(goal)

    # Search rules whose conclusion matches goal
    for rule_number, conditions, conclusion in propositional_rules:

        if conclusion == goal:

            explanation = [
                "RULE " + rule_number +
                " supports " + goal
            ]

            all_conditions_true = True

            for condition in conditions:

                result, sub_explanation = backward_chaining(
                    condition,
                    facts,
                    visited.copy()
                )

                if not result:

                    all_conditions_true = False
                    break

                explanation.extend(sub_explanation)

            if all_conditions_true:

                return True, explanation

    return False, []


# ================================================================
# 8. UNIFICATION
# ================================================================

def is_variable(value):

    return (
        isinstance(value, str)
        and value.isupper()
    )


def unify(term1, term2, substitution=None):

    if substitution is None:
        substitution = {}

    # Same terms
    if term1 == term2:

        return substitution

    # Variable handling
    if is_variable(term1):

        return unify_variable(
            term1,
            term2,
            substitution
        )

    if is_variable(term2):

        return unify_variable(
            term2,
            term1,
            substitution
        )

    # Tuple/predicate handling
    if isinstance(term1, tuple) and isinstance(term2, tuple):

        if len(term1) != len(term2):

            return None

        for a, b in zip(term1, term2):

            substitution = unify(
                a,
                b,
                substitution
            )

            if substitution is None:

                return None

        return substitution

    return None


def unify_variable(variable, value, substitution):

    if variable in substitution:

        return unify(
            substitution[variable],
            value,
            substitution
        )

    if is_variable(value) and value in substitution:

        return unify(
            variable,
            substitution[value],
            substitution
        )

    substitution[variable] = value

    return substitution


# ================================================================
# 9. UNIFICATION DEMONSTRATION
# ================================================================

def demonstrate_unification():

    print("\n" + "=" * 75)
    print("UNIFICATION EXAMPLES")
    print("=" * 75)

    example1 = unify(
        ("has_symptom", "X", "chest_pain"),
        ("has_symptom", "P1", "chest_pain")
    )

    print("Example 1:")
    print("  has_symptom(X, chest_pain)")
    print("  has_symptom(P1, chest_pain)")
    print("  Substitution:", example1)

    example2 = unify(
        (
            "possible_condition",
            "X",
            "cardiac_risk"
        ),
        (
            "possible_condition",
            "P1",
            "cardiac_risk"
        )
    )

    print("\nExample 2:")
    print("  possible_condition(X, cardiac_risk)")
    print("  possible_condition(P1, cardiac_risk)")
    print("  Substitution:", example2)


# ================================================================
# 10. RESOLUTION
# ================================================================

def negate(literal):

    if literal.startswith("NOT_"):

        return literal[4:]

    return "NOT_" + literal


def resolve(clause1, clause2):

    for literal1 in clause1:

        complementary = negate(literal1)

        if complementary in clause2:

            new_clause = (
                set(clause1) - {literal1}
            ) | (
                set(clause2) - {complementary}
            )

            return frozenset(new_clause)

    return None


def resolution_demo():

    print("\n" + "=" * 75)
    print("RESOLUTION")
    print("=" * 75)

    print("Knowledge Base:")
    print("1. chest_pain")
    print("2. chest_pain -> cardiac_risk")
    print("3. cardiac_risk -> urgent_assessment")

    print("\nQuery: urgent_assessment")

    print("\nClausal form:")
    print("C1 = {chest_pain}")
    print("C2 = {NOT_chest_pain, cardiac_risk}")
    print("C3 = {NOT_cardiac_risk, urgent_assessment}")

    print("Negated Query:")
    print("C4 = {NOT_urgent_assessment}")

    c1 = frozenset(["chest_pain"])

    c2 = frozenset([
        "NOT_chest_pain",
        "cardiac_risk"
    ])

    c3 = frozenset([
        "NOT_cardiac_risk",
        "urgent_assessment"
    ])

    c4 = frozenset([
        "NOT_urgent_assessment"
    ])

    print("\nResolution steps:")

    r1 = resolve(c1, c2)

    print(
        "C1 + C2 ->",
        set(r1)
    )

    r2 = resolve(r1, c3)

    print(
        "R1 + C3 ->",
        set(r2)
    )

    r3 = resolve(r2, c4)

    print(
        "R2 + C4 ->",
        set(r3)
    )

    if r3 == frozenset():

        print(
            "\nConclusion: Empty clause obtained."
        )

        print(
            "Therefore urgent_assessment "
            "is logically supported."
        )


# ================================================================
# 11. RISK SCORE
# ================================================================

def calculate_risk(patient):

    data = patients[patient]

    score = 0

    symptoms = data["symptoms"]

    # Cardiac indicators
    if "chest_pain" in symptoms:
        score += 5

    if "sweating" in symptoms:
        score += 2

    if "shortness_of_breath" in symptoms:
        score += 3

    # Respiratory indicators
    if "breathing_difficulty" in symptoms:
        score += 3

    if data.get("oxygen") == "low":
        score += 5

    # Neurological indicators
    if "severe_headache" in symptoms:
        score += 4

    if "one_sided_weakness" in symptoms:
        score += 5

    if data.get("blood_pressure") == "high":
        score += 3

    # Abdominal indicators
    if "abdominal_pain" in symptoms:
        score += 2

    if "vomiting" in symptoms:
        score += 1

    # Fever
    if data.get("temperature") == "high":
        score += 2

    # Medical history
    if "hypertension" in data.get("history", []):
        score += 1

    return score


# ================================================================
# 12. PRIORITY CLASSIFICATION
# ================================================================

def priority_from_score(score):

    if score >= 10:

        return "CRITICAL"

    elif score >= 7:

        return "HIGH"

    elif score >= 4:

        return "MEDIUM"

    else:

        return "LOW"


# ================================================================
# 13. DETERMINE CORRECT ASSESSMENT
# ================================================================

def determine_assessment(patient, inferred_facts):

    # P1 / Cardiac
    if "very_high_risk" in inferred_facts:

        return "send_to_urgent_assessment"

    # P2 / Respiratory
    if "urgent_respiratory_assessment" in inferred_facts:

        return "send_to_respiratory_assessment"

    # P3 / Neurological
    if "urgent_neurological_assessment" in inferred_facts:

        return "send_to_neurological_assessment"

    # P4 / General
    if "medical_assessment_required" in inferred_facts:

        return "send_to_general_assessment"

    return "send_to_general_assessment"


# ================================================================
# 14. STATE SPACE
# ================================================================

states = [

    "Patient_Arrival",

    "Initial_Assessment",

    "Vital_Check",

    "Risk_Assessment",

    "Urgent_Assessment",

    "Respiratory_Assessment",

    "Neurological_Assessment",

    "General_Medical_Assessment",

    "Goal"
]


# ================================================================
# 15. STATE TRANSITIONS
# ================================================================

base_transitions = {

    (
        "Patient_Arrival",
        "perform_initial_assessment"
    ):
        "Initial_Assessment",

    (
        "Initial_Assessment",
        "check_vitals"
    ):
        "Vital_Check",

    (
        "Vital_Check",
        "perform_risk_assessment"
    ):
        "Risk_Assessment"
}


# ================================================================
# 16. A* HEURISTIC
# ================================================================

def heuristic(state, goal):

    # Estimated number of steps remaining
    # from current state to goal.

    estimates = {

        "Patient_Arrival": 5,

        "Initial_Assessment": 4,

        "Vital_Check": 3,

        "Risk_Assessment": 2,

        "Urgent_Assessment": 1,

        "Respiratory_Assessment": 1,

        "Neurological_Assessment": 1,

        "General_Medical_Assessment": 1,

        "Goal": 0
    }

    return estimates.get(state, 0)


# ================================================================
# 17. A* SEARCH
# ================================================================

def astar_search(patient, target_assessment):

    start = "Patient_Arrival"

    goal = "Goal"

    # Patient-specific final transition
    patient_transitions = dict(base_transitions)

    patient_transitions[
        (
            "Risk_Assessment",
            target_assessment
        )
    ] = target_assessment

    # Final assessment -> Goal
    patient_transitions[
        (
            target_assessment,
            "generate_priority_decision"
        )
    ] = goal

    open_list = []

    counter = 0

    start_h = heuristic(start, goal)

    heappush(
        open_list,
        (
            start_h,
            0,
            counter,
            start,
            []
        )
    )

    visited = set()

    while open_list:

        f, g, _, current, path = heappop(open_list)

        if current in visited:

            continue

        visited.add(current)

        # Goal reached
        if current == goal:

            return {
                "path": path + ["Goal"],
                "cost": g,
                "visited": visited
            }

        # Determine available actions
        actions = []

        for (
            state,
            action
        ), next_state in patient_transitions.items():

            if state == current:

                actions.append(
                    (
                        action,
                        next_state
                    )
                )

        for action, next_state in actions:

            new_g = g + 1

            new_h = heuristic(
                next_state,
                goal
            )

            new_f = new_g + new_h

            new_path = path + [

                current +
                " --[" +
                action +
                "]--> " +
                next_state
            ]

            counter += 1

            heappush(
                open_list,
                (
                    new_f,
                    new_g,
                    counter,
                    next_state,
                    new_path
                )
            )

    return None


# ================================================================
# 18. GREEDY BEST-FIRST SEARCH
# ================================================================

def greedy_search(patient, target_assessment):

    start = "Patient_Arrival"

    goal = "Goal"

    patient_transitions = dict(base_transitions)

    patient_transitions[
        (
            "Risk_Assessment",
            target_assessment
        )
    ] = target_assessment

    patient_transitions[
        (
            target_assessment,
            "generate_priority_decision"
        )
    ] = goal

    queue = []

    counter = 0

    heappush(
        queue,
        (
            heuristic(start, goal),
            counter,
            start,
            []
        )
    )

    visited = set()

    while queue:

        _, _, current, path = heappop(queue)

        if current in visited:

            continue

        visited.add(current)

        if current == goal:

            return {
                "path": path + ["Goal"],
                "cost": len(path),
                "visited": visited
            }

        for (
            state,
            action
        ), next_state in patient_transitions.items():

            if state == current:

                counter += 1

                new_path = path + [

                    current +
                    " --[" +
                    action +
                    "]--> " +
                    next_state
                ]

                heappush(
                    queue,
                    (
                        heuristic(
                            next_state,
                            goal
                        ),
                        counter,
                        next_state,
                        new_path
                    )
                )

    return None


# ================================================================
# 19. RESOURCE ALLOCATION
# ================================================================

def allocate_resource(priority):

    resources = {

        "CRITICAL":
            "Emergency team + continuous monitoring",

        "HIGH":
            "Priority clinical assessment + monitoring",

        "MEDIUM":
            "Standard medical assessment",

        "LOW":
            "Routine assessment"
    }

    return resources.get(
        priority,
        "Standard medical assessment"
    )


# ================================================================
# 20. INTELLIGENT AGENT
# ================================================================

class EmergencyMedicalAgent:

    def __init__(self):

        self.name = (
            "Intelligent Emergency "
            "Medical Decision-Support Agent"
        )

        self.goals = [

            "Prioritize patients",

            "Identify possible risk patterns",

            "Recommend appropriate assessment",

            "Support resource allocation"
        ]

        self.learning_records = []

    # ------------------------------------------------------------
    # Sensor / Perception
    # ------------------------------------------------------------

    def perceive(self, patient):

        print(
            "\n[SENSOR] Receiving patient data:",
            patient
        )

        return patients[patient]

    # ------------------------------------------------------------
    # Reasoning
    # ------------------------------------------------------------

    def reason(self, patient):

        initial_facts = create_facts(patient)

        inferred_facts, fired_rules = forward_chaining(
            initial_facts
        )

        return (
            initial_facts,
            inferred_facts,
            fired_rules
        )

    # ------------------------------------------------------------
    # Decision
    # ------------------------------------------------------------

    def decide(self, patient, inferred_facts):

        score = calculate_risk(patient)

        priority = priority_from_score(score)

        assessment = determine_assessment(
            patient,
            inferred_facts
        )

        resource = allocate_resource(priority)

        return (
            score,
            priority,
            assessment,
            resource
        )

    # ------------------------------------------------------------
    # Learning
    # ------------------------------------------------------------

    def learn(self, patient, priority):

        self.learning_records.append(
            {
                "patient": patient,
                "priority": priority
            }
        )

    # ------------------------------------------------------------
    # Actuator
    # ------------------------------------------------------------

    def act(
        self,
        patient,
        assessment,
        priority
    ):

        print(
            "[ACTUATOR] Patient:",
            patient
        )

        print(
            "[ACTUATOR] Suggested assessment:",
            assessment
        )

        print(
            "[ACTUATOR] Priority:",
            priority
        )


# ================================================================
# 21. HISTORICAL LEARNING COMPONENT
# ================================================================

class HistoricalLearning:

    def __init__(self):

        self.historical_cases = [

            {
                "risk_score": 13,
                "priority": "CRITICAL"
            },

            {
                "risk_score": 11,
                "priority": "CRITICAL"
            },

            {
                "risk_score": 9,
                "priority": "HIGH"
            },

            {
                "risk_score": 6,
                "priority": "MEDIUM"
            },

            {
                "risk_score": 5,
                "priority": "MEDIUM"
            },

            {
                "risk_score": 2,
                "priority": "LOW"
            }
        ]

    def predict_priority(self, score):

        closest_case = min(
            self.historical_cases,
            key=lambda case:
            abs(
                case["risk_score"] -
                score
            )
        )

        return closest_case["priority"]

    def display_learning(self):

        print("\n" + "=" * 75)
        print("LEARNING COMPONENT")
        print("=" * 75)

        for case in self.historical_cases:

            print(
                "Historical risk score:",
                case["risk_score"],
                "->",
                case["priority"]
            )


# ================================================================
# 22. AGENT ARCHITECTURE DISPLAY
# ================================================================

def display_architecture():

    print("\n" + "=" * 75)
    print("INTELLIGENT AGENT ARCHITECTURE")
    print("=" * 75)

    print("""
                         ENVIRONMENT
                              |
                              v
                       +--------------+
                       |    SENSORS   |
                       | Patient Data |
                       +--------------+
                              |
                              v
                       +--------------+
                       |  KNOWLEDGE   |
                       |     BASE     |
                       +--------------+
                              |
                              v
                 +---------------------------+
                 |     REASONING ENGINE      |
                 |                           |
                 |  Forward Chaining         |
                 |  Backward Chaining        |
                 |  A* Search                |
                 |  FOL / Unification       |
                 |  Resolution               |
                 +---------------------------+
                              |
                              v
                       +--------------+
                       |   DECISION   |
                       |    MODULE    |
                       +--------------+
                              |
                              v
                       +--------------+
                       |  ACTUATORS   |
                       | Recommendation|
                       +--------------+
                              |
                              v
                         ENVIRONMENT


             Historical Cases
                    |
                    v
             +--------------+
             |   LEARNING   |
             |   COMPONENT  |
             +--------------+
                    |
                    v
             Updated Knowledge
    """)


# ================================================================
# 23. PROCESS ONE PATIENT
# ================================================================

def process_patient(
    agent,
    learner,
    patient
):

    print("\n")

    print("=" * 75)
    print(
        "PROCESSING PATIENT:",
        patient
    )
    print("=" * 75)

    # ------------------------------------------------------------
    # SENSOR
    # ------------------------------------------------------------

    data = agent.perceive(patient)

    print("\nPatient Information:")

    print(
        "Symptoms:",
        ", ".join(data["symptoms"])
    )

    print(
        "Heart Rate:",
        data.get("heart_rate")
    )

    print(
        "Oxygen:",
        data.get("oxygen")
    )

    print(
        "Temperature:",
        data.get("temperature")
    )

    print(
        "Blood Pressure:",
        data.get(
            "blood_pressure",
            "not recorded"
        )
    )

    print(
        "History:",
        data.get("history")
    )

    # ------------------------------------------------------------
    # PROPOSITIONAL FACTS
    # ------------------------------------------------------------

    initial_facts = create_facts(patient)

    print("\nPropositional Facts:")

    print(
        sorted(initial_facts)
    )

    # ------------------------------------------------------------
    # FORWARD CHAINING
    # ------------------------------------------------------------

    (
        initial_facts,
        inferred_facts,
        fired_rules
    ) = agent.reason(patient)

    print("\nForward Chaining:")

    print(
        "Initial Facts:",
        sorted(initial_facts)
    )

    print(
        "Fired Rules:",
        fired_rules
    )

    print(
        "Inferred Facts:",
        sorted(inferred_facts)
    )

    # ------------------------------------------------------------
    # BACKWARD CHAINING
    # ------------------------------------------------------------

    score = calculate_risk(patient)

    # Determine correct backward goal
    if "very_high_risk" in inferred_facts:

        backward_goal = "immediate_attention"

    elif (
        "urgent_respiratory_assessment"
        in inferred_facts
    ):

        backward_goal = "high_priority"

    elif (
        "urgent_neurological_assessment"
        in inferred_facts
    ):

        backward_goal = "high_priority"

    else:

        backward_goal = (
            "medical_assessment_required"
        )

    (
        backward_result,
        backward_explanation
    ) = backward_chaining(
        backward_goal,
        inferred_facts
    )

    print("\nBackward Chaining:")

    print(
        "Goal:",
        backward_goal
    )

    print(
        "Result:",
        backward_result
    )

    if backward_result:

        for item in backward_explanation:

            print(
                " ",
                item
            )

    # ------------------------------------------------------------
    # DETERMINE ASSESSMENT
    # ------------------------------------------------------------

    assessment = determine_assessment(
        patient,
        inferred_facts
    )

    # ------------------------------------------------------------
    # A* SEARCH
    # ------------------------------------------------------------

    astar_result = astar_search(
        patient,
        assessment
    )

    print("\nA* SEARCH")
    print("-" * 45)

    print(
        "Target Assessment:",
        assessment
    )

    if astar_result:

        print("Path:")

        for step in astar_result["path"]:

            print(
                " ",
                step
            )

        print(
            "Path Cost:",
            astar_result["cost"]
        )

        print(
            "States Explored:",
            len(
                astar_result["visited"]
            )
        )

    # ------------------------------------------------------------
    # GREEDY BEST-FIRST SEARCH
    # ------------------------------------------------------------

    greedy_result = greedy_search(
        patient,
        assessment
    )

    print("\nGREEDY BEST-FIRST SEARCH")
    print("-" * 45)

    if greedy_result:

        print(
            "Target Assessment:",
            assessment
        )

        print(
            "Path Cost:",
            greedy_result["cost"]
        )

        print(
            "States Explored:",
            len(
                greedy_result["visited"]
            )
        )

    # ------------------------------------------------------------
    # AGENT DECISION
    # ------------------------------------------------------------

    (
        score,
        priority,
        assessment,
        resource
    ) = agent.decide(
        patient,
        inferred_facts
    )

    learned_priority = learner.predict_priority(
        score
    )

    print("\nAGENT DECISION")
    print("-" * 45)

    print(
        "Risk Score:",
        score
    )

    print(
        "Rule-Based Priority:",
        priority
    )

    print(
        "Learning-Based Priority:",
        learned_priority
    )

    print(
        "Recommended Assessment:",
        assessment
    )

    print(
        "Resource Allocation:",
        resource
    )

    # ------------------------------------------------------------
    # ACTUATOR
    # ------------------------------------------------------------

    agent.act(
        patient,
        assessment,
        priority
    )

    # ------------------------------------------------------------
    # LEARNING
    # ------------------------------------------------------------

    agent.learn(
        patient,
        priority
    )

    return {

        "patient": patient,

        "score": score,

        "priority": priority,

        "learned_priority":
            learned_priority,

        "assessment":
            assessment,

        "resource":
            resource,

        "astar_cost":
            astar_result["cost"]
            if astar_result
            else None,

        "greedy_cost":
            greedy_result["cost"]
            if greedy_result
            else None
    }


# ================================================================
# 24. SEARCH ALGORITHM COMPARISON
# ================================================================

def compare_search(results):

    print("\n" + "=" * 75)
    print("SEARCH ALGORITHM COMPARISON")
    print("=" * 75)

    print(
        "{:<10} {:<20} {:<20}".format(
            "Patient",
            "A* Path Cost",
            "Greedy Path Cost"
        )
    )

    print("-" * 55)

    for result in results:

        print(
            "{:<10} {:<20} {:<20}".format(
                result["patient"],
                result["astar_cost"],
                result["greedy_cost"]
            )
        )

    print("\nA* Evaluation Function:")

    print(
        "f(n) = g(n) + h(n)"
    )

    print("\ng(n): Cost from the initial state")

    print(
        "h(n): Estimated cost from current state to goal"
    )

    print(
        "f(n): Total estimated path cost"
    )

    print("\nGreedy Best-First Search uses:")

    print(
        "f(n) = h(n)"
    )


# ================================================================
# 25. FINAL VALIDATION TABLE
# ================================================================

def validation_table(results):

    print("\n" + "=" * 110)
    print("FINAL VALIDATION / TESTING RESULTS")
    print("=" * 110)

    print(
        "{:<10} {:<12} {:<18} {:<35} {:<15}".format(
            "Patient",
            "Risk Score",
            "Search",
            "Inference Decision",
            "Priority"
        )
    )

    print("-" * 110)

    for result in results:

        print(
            "{:<10} {:<12} {:<18} {:<35} {:<15}".format(
                result["patient"],
                result["score"],
                "A*",
                result["assessment"],
                result["priority"]
            )
        )


# ================================================================
# 26. KNOWLEDGE BASE SUMMARY
# ================================================================

def display_knowledge_summary():

    print("\n" + "=" * 75)
    print("KNOWLEDGE BASE SUMMARY")
    print("=" * 75)

    print(
        "Production Rules:",
        len(propositional_rules)
    )

    print(
        "FOL Facts:",
        len(fol_facts)
    )

    print(
        "FOL Rules:",
        len(fol_rules)
    )

    print(
        "Patients Tested:",
        len(patients)
    )

    print("\nProduction Rules:")

    for number, conditions, conclusion in propositional_rules:

        condition_text = " AND ".join(
            sorted(conditions)
        )

        print(
            f"{number}: "
            f"{condition_text} -> "
            f"{conclusion}"
        )


# ================================================================
# 27. MAIN PROGRAM
# ================================================================

def main():

    print("\n")

    print("=" * 75)

    print(
        " INTELLIGENT EMERGENCY MEDICAL "
        "DECISION-SUPPORT AGENT"
    )

    print("=" * 75)

    print(
        "\nEducational AI Prototype"
    )

    print(
        "Purpose: Emergency prioritization "
        "and decision support"
    )

    print(
        "Techniques: A*, Logic, Expert System, "
        "Intelligent Agent and Learning"
    )

    print(
        "Warning: This prototype does not "
        "replace medical professionals."
    )

    # ------------------------------------------------------------
    # Agent Architecture
    # ------------------------------------------------------------

    display_architecture()

    # ------------------------------------------------------------
    # Knowledge Base
    # ------------------------------------------------------------

    display_knowledge_summary()

    # ------------------------------------------------------------
    # Unification
    # ------------------------------------------------------------

    demonstrate_unification()

    # ------------------------------------------------------------
    # Resolution
    # ------------------------------------------------------------

    resolution_demo()

    # ------------------------------------------------------------
    # Learning
    # ------------------------------------------------------------

    learner = HistoricalLearning()

    learner.display_learning()

    # ------------------------------------------------------------
    # Create Agent
    # ------------------------------------------------------------

    agent = EmergencyMedicalAgent()

    results = []

    # ------------------------------------------------------------
    # Process all patients
    # ------------------------------------------------------------

    for patient in patients:

        result = process_patient(
            agent,
            learner,
            patient
        )

        results.append(result)

    # ------------------------------------------------------------
    # Search Comparison
    # ------------------------------------------------------------

    compare_search(results)

    # ------------------------------------------------------------
    # Validation
    # ------------------------------------------------------------

    validation_table(results)

    # ------------------------------------------------------------
    # Learning Record
    # ------------------------------------------------------------

    print("\n" + "=" * 75)
    print("LEARNING RECORD")
    print("=" * 75)

    for record in agent.learning_records:

        print(
            "Patient:",
            record["patient"],
            "-> Learned Priority:",
            record["priority"]
        )

    # ------------------------------------------------------------
    # Final Summary
    # ------------------------------------------------------------

    print("\n" + "=" * 75)
    print("FINAL SYSTEM SUMMARY")
    print("=" * 75)

    print(
        "Patients processed:",
        len(results)
    )

    print(
        "A* Search: Completed"
    )

    print(
        "Greedy Best-First Search: Completed"
    )

    print(
        "Forward Chaining: Completed"
    )

    print(
        "Backward Chaining: Completed"
    )

    print(
        "FOL Representation: Completed"
    )

    print(
        "Unification: Completed"
    )

    print(
        "Resolution: Completed"
    )

    print(
        "Expert System: Completed"
    )

    print(
        "Intelligent Agent: Completed"
    )

    print(
        "Learning Component: Completed"
    )

    print(
        "Validation Testing: Completed"
    )

    print("\n" + "=" * 75)

    print(
        "PROGRAM EXECUTION COMPLETED"
    )

    print("=" * 75)


# ================================================================
# PROGRAM ENTRY POINT
# ================================================================

if __name__ == "__main__":

    main()