import math

# Calculate entropy
def entropy(data):
    labels = [row[-1] for row in data]
    total = len(labels)

    counts = {}
    for label in labels:
        counts[label] = counts.get(label, 0) + 1

    ent = 0
    for count in counts.values():
        p = count / total
        ent -= p * math.log2(p)

    return ent


# Calculate information gain
def information_gain(data, feature_index):
    total_entropy = entropy(data)

    values = set(row[feature_index] for row in data)
    weighted_entropy = 0

    for value in values:
        subset = [
            row for row in data
            if row[feature_index] == value
        ]

        weighted_entropy += (
            len(subset) / len(data)
        ) * entropy(subset)

    return total_entropy - weighted_entropy


# Build Decision Tree using ID3
def build_tree(data, features):
    labels = [row[-1] for row in data]

    # All labels are same
    if len(set(labels)) == 1:
        return labels[0]

    # No features remaining
    if not features:
        return max(set(labels), key=labels.count)

    # Select feature with maximum information gain
    best_feature = max(
        features,
        key=lambda f: information_gain(data, f)
    )

    tree = {best_feature: {}}

    values = set(row[best_feature] for row in data)

    remaining_features = [
        f for f in features
        if f != best_feature
    ]

    for value in values:
        subset = [
            row for row in data
            if row[best_feature] == value
        ]

        tree[best_feature][value] = build_tree(
            subset,
            remaining_features
        )

    return tree


# -----------------------------
# Input Data
# -----------------------------

day = list(map(int, input("Day: ").split(",")))

outlook = input("Outlook: ").lower().split(",")

temp = input("Temp: ").lower().split(",")

humidity = input("Humidity: ").lower().split(",")

wind = input("Wind: ").lower().split(",")

play = input("PlayTennis: ").lower().split(",")


# Remove extra spaces
outlook = [x.strip() for x in outlook]
temp = [x.strip() for x in temp]
humidity = [x.strip() for x in humidity]
wind = [x.strip() for x in wind]
play = [x.strip() for x in play]


# Check all columns have same number of values
lengths = [
    len(day),
    len(outlook),
    len(temp),
    len(humidity),
    len(wind),
    len(play)
]

if len(set(lengths)) != 1:
    print("\nError: All columns must contain the same number of values.")
    print("Number of values:", lengths)
    exit()


# Create dataset
data = []

for i in range(len(day)):
    data.append([
        day[i],
        outlook[i],
        temp[i],
        humidity[i],
        wind[i],
        play[i]
    ])


# Feature indexes
# 0 = Day
# 1 = Outlook
# 2 = Temp
# 3 = Humidity
# 4 = Wind

features = [1, 2, 3, 4]


# Build tree
tree = build_tree(data, features)


# Display information gain
print("\nInformation Gain:")

feature_names = {
    1: "Outlook",
    2: "Temp",
    3: "Humidity",
    4: "Wind"
}

for feature in features:
    gain = information_gain(data, feature)
    print(feature_names[feature], "=", round(gain, 4))


# Display tree
print("\nDecision Tree:")
print(tree)