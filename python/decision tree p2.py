import math

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
    [10,"false", "cool", "high",   "yes"]
]

feature_names = {
    1: "A1",
    2: "A2",
    3: "A3"
}

# Entropy
def entropy(dataset):
    total = len(dataset)
    labels = [row[-1] for row in dataset]

    counts = {}
    for label in labels:
        counts[label] = counts.get(label, 0) + 1

    ent = 0
    for count in counts.values():
        p = count / total
        ent -= p * math.log2(p)

    return ent


# Information Gain
def information_gain(dataset, feature):
    total_entropy = entropy(dataset)

    values = set(row[feature] for row in dataset)

    weighted_entropy = 0

    for value in values:
        subset = [row for row in dataset if row[feature] == value]
        weighted_entropy += (len(subset) / len(dataset)) * entropy(subset)

    return total_entropy - weighted_entropy


# Build Decision Tree
def build_tree(dataset, features):

    labels = [row[-1] for row in dataset]

    if len(set(labels)) == 1:
        return labels[0]

    if len(features) == 0:
        return max(set(labels), key=labels.count)

    best = max(features, key=lambda f: information_gain(dataset, f))

    tree = {feature_names[best]: {}}

    values = set(row[best] for row in dataset)

    remaining = [f for f in features if f != best]

    for value in values:
        subset = [row for row in dataset if row[best] == value]

        tree[feature_names[best]][value] = build_tree(subset, remaining)

    return tree


features = [1, 2, 3]

print("Information Gain")
for f in features:
    print(feature_names[f], "=", round(information_gain(data, f), 4))

tree = build_tree(data, features)

print("\nDecision Tree")
print(tree)