import math

# Decision Tree - Problem 3

# Dataset
data = [
    [1, "T", "T", "+"],
    [2, "T", "T", "+"],
    [3, "T", "F", "-"],
    [4, "F", "F", "+"],
    [5, "F", "T", "-"],
    [6, "F", "T", "-"]
]

# Feature names
feature_names = {
    1: "A1",
    2: "A2"
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

    # If all classifications are same
    if len(set(classes)) == 1:
        return classes[0]

    # If no features remain
    if not features:
        return max(set(classes), key=classes.count)

    # Select feature with maximum Information Gain
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


# Features
features = [1, 2]


# Calculate Information Gain
print("Information Gain:")

for feature in features:
    gain = information_gain(data, feature)
    print(feature_names[feature], "=", round(gain, 4))


# Build Decision Tree
decision_tree = build_tree(data, features)


# Display Decision Tree
print("\nDecision Tree:")
print(decision_tree)