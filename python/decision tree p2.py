import math

# Decision Tree - Problem 2

# Dataset
data = [
    [1, "true",  "hot",  "high",   "no"],
    [2, "true",  "hot",  "high",   "no"],
    [3, "false", "hot",  "high",   "yes"],
    [4, "false", "cool", "normal", "yes"],
    [5, "false", "cool", "normal", "yes"],
    [6, "true",  "cool", "high",   "no"],
    [7, "true",  "hot",  "high",   "no"],
    [8, "true",  "hot",  "normal", "yes"],
    [9, "false", "cool", "normal", "yes"],
    [10, "false", "cool", "high",  "yes"]
]

# Feature names
feature_names = {
    1: "A1",
    2: "A2",
    3: "A3"
}


# Calculate Entropy
def entropy(dataset):
    total = len(dataset)
    counts = {}

    for row in dataset:
        label = row[-1]
        counts[label] = counts.get(label, 0) + 1

    result = 0

    for count in counts.values():
        probability = count / total
        result -= probability * math.log2(probability)

    return result


# Calculate Information Gain
def information_gain(dataset, feature):
    total_entropy = entropy(dataset)

    values = set(row[feature] for row in dataset)

    weighted_entropy = 0

    for value in values:
        subset = [
            row for row in dataset
            if row[feature] == value
        ]

        weighted_entropy += (
            len(subset) / len(dataset)
        ) * entropy(subset)

    return total_entropy - weighted_entropy


# Build Decision Tree
def build_tree(dataset, features):

    classes = [row[-1] for row in dataset]

    # All classes are the same
    if len(set(classes)) == 1:
        return classes[0]

    # No features remaining
    if not features:
        return max(set(classes), key=classes.count)

    # Find feature with maximum Information Gain
    best_feature = max(
        features,
        key=lambda f: information_gain(dataset, f)
    )

    tree = {
        feature_names[best_feature]: {}
    }

    values = set(row[best_feature] for row in dataset)

    remaining_features = [
        f for f in features
        if f != best_feature
    ]

    for value in values:

        subset = [
            row for row in dataset
            if row[best_feature] == value
        ]

        tree[feature_names[best_feature]][value] = build_tree(
            subset,
            remaining_features
        )

    return tree


# Features: A1, A2, A3
features = [1, 2, 3]

# Build the Decision Tree
decision_tree = build_tree(data, features)