# ============================================================
# SMART LOAN APPROVAL USING DECISION TREE
# AI Model Design Exercise - Q1
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

# ============================================================
# 1. CREATE DATASET
# ============================================================

np.random.seed(42)

n = 100

data = {
    "Income": np.random.randint(20000, 100000, n),

    "CreditScore": np.random.randint(500, 850, n),

    "EmploymentStatus": np.random.choice(
        ["Employed", "Self-Employed", "Unemployed"],
        n,
        p=[0.60, 0.30, 0.10]
    ),

    "LoanAmount": np.random.randint(
        200000, 700000, n
    ),

    "RepaymentHistory": np.random.choice(
        ["Good", "Average", "Poor"],
        n,
        p=[0.40, 0.35, 0.25]
    )
}

# ============================================================
# 2. GENERATE LOAN APPROVAL TARGET
# ============================================================

approval = []

for i in range(n):

    credit_score = data["CreditScore"][i]
    income = data["Income"][i]
    employment = data["EmploymentStatus"][i]
    loan_amount = data["LoanAmount"][i]
    repayment = data["RepaymentHistory"][i]

    score = 0

    # Credit Score
    if credit_score >= 700:
        score += 3
    elif credit_score >= 600:
        score += 1

    # Income
    if income >= 70000:
        score += 2
    elif income >= 40000:
        score += 1

    # Employment Status
    if employment == "Employed":
        score += 2
    elif employment == "Self-Employed":
        score += 1

    # Repayment History
    if repayment == "Good":
        score += 3
    elif repayment == "Average":
        score += 1

    # Loan Amount
    if loan_amount <= 400000:
        score += 2
    elif loan_amount <= 550000:
        score += 1

    # Final decision
    if score >= 6:
        approval.append("Approved")
    else:
        approval.append("Rejected")

data["LoanApproval"] = approval

df = pd.DataFrame(data)

# ============================================================
# 3. DISPLAY DATASET
# ============================================================

print("\n================================================")
print("             SMART LOAN APPROVAL")
print("================================================")

print("\nFirst 10 Records:")
print(df.head(10))

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nDataset Information:")
df.info()

# ============================================================
# 4. CLASS DISTRIBUTION
# ============================================================

print("\n================================================")
print("             CLASS DISTRIBUTION")
print("================================================")

print(df["LoanApproval"].value_counts())

# ============================================================
# 5. MISSING VALUE CHECK
# ============================================================

print("\n================================================")
print("             MISSING VALUE CHECK")
print("================================================")

print(df.isnull().sum())

# ============================================================
# 6. DUPLICATE CHECK
# ============================================================

print("\nDuplicate Records:", df.duplicated().sum())

# ============================================================
# 7. ENCODE CATEGORICAL FEATURES
# ============================================================

employment_encoder = LabelEncoder()
repayment_encoder = LabelEncoder()
target_encoder = LabelEncoder()

df["EmploymentStatus"] = employment_encoder.fit_transform(
    df["EmploymentStatus"]
)

df["RepaymentHistory"] = repayment_encoder.fit_transform(
    df["RepaymentHistory"]
)

df["LoanApproval"] = target_encoder.fit_transform(
    df["LoanApproval"]
)

print("\n================================================")
print("             ENCODED DATA")
print("================================================")

print(df.head())

print("\nEmployment Encoding:")

for label, value in zip(
    employment_encoder.classes_,
    employment_encoder.transform(
        employment_encoder.classes_
    )
):
    print(label, "=", value)

print("\nRepayment History Encoding:")

for label, value in zip(
    repayment_encoder.classes_,
    repayment_encoder.transform(
        repayment_encoder.classes_
    )
):
    print(label, "=", value)

print("\nLoan Approval Encoding:")

for label, value in zip(
    target_encoder.classes_,
    target_encoder.transform(
        target_encoder.classes_
    )
):
    print(label, "=", value)

# ============================================================
# 8. SEPARATE FEATURES AND TARGET
# ============================================================

X = df[
    [
        "Income",
        "CreditScore",
        "EmploymentStatus",
        "LoanAmount",
        "RepaymentHistory"
    ]
]

y = df["LoanApproval"]

print("\n================================================")
print("             FEATURES AND TARGET")
print("================================================")

print("\nFeatures:")
print(X.columns.tolist())

print("\nTarget:")
print("LoanApproval")

# ============================================================
# 9. TRAIN-TEST SPLIT
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\n================================================")
print("             TRAIN TEST SPLIT")
print("================================================")

print("Training samples:", len(X_train))
print("Testing samples :", len(X_test))

# ============================================================
# 10. CREATE DECISION TREE
# ============================================================

model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=5,
    min_samples_split=4,
    min_samples_leaf=2,
    random_state=42
)

print("\n================================================")
print("             DECISION TREE MODEL")
print("================================================")

print("Algorithm        : Decision Tree")
print("Criterion        : Gini Index")
print("Maximum Depth    :", model.max_depth)
print("Min Samples Split:", model.min_samples_split)
print("Min Samples Leaf :", model.min_samples_leaf)
print("Random State     :", model.random_state)

# ============================================================
# 11. TRAIN MODEL
# ============================================================

model.fit(X_train, y_train)

print("\nModel training completed successfully.")

# ============================================================
# 12. MAKE PREDICTIONS
# ============================================================

y_pred = model.predict(X_test)

# ============================================================
# 13. PERFORMANCE EVALUATION
# ============================================================

accuracy = accuracy_score(y_test, y_pred)

precision = precision_score(
    y_test,
    y_pred,
    zero_division=0
)

recall = recall_score(
    y_test,
    y_pred,
    zero_division=0
)

f1 = f1_score(
    y_test,
    y_pred,
    zero_division=0
)

print("\n================================================")
print("             MODEL PERFORMANCE")
print("================================================")

print(f"Accuracy  : {accuracy * 100:.2f}%")
print(f"Precision : {precision * 100:.2f}%")
print(f"Recall    : {recall * 100:.2f}%")
print(f"F1-Score  : {f1 * 100:.2f}%")

# ============================================================
# 14. CLASSIFICATION REPORT
# ============================================================

print("\n================================================")
print("             CLASSIFICATION REPORT")
print("================================================")

print(
    classification_report(
        y_test,
        y_pred,
        target_names=target_encoder.classes_,
        zero_division=0
    )
)

# ============================================================
# 15. CONFUSION MATRIX
# ============================================================

cm = confusion_matrix(y_test, y_pred)

print("\n================================================")
print("             CONFUSION MATRIX")
print("================================================")

print(cm)

plt.figure(figsize=(7, 5))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=target_encoder.classes_,
    yticklabels=target_encoder.classes_
)

plt.title("Confusion Matrix - Smart Loan Approval")
plt.xlabel("Predicted Class")
plt.ylabel("Actual Class")

plt.tight_layout()

plt.savefig(
    "confusion_matrix.png",
    dpi=300
)

# IMPORTANT:
# Close the figure instead of plt.show()
plt.close()

print("\nConfusion matrix saved as: confusion_matrix.png")

# ============================================================
# 16. FEATURE IMPORTANCE
# ============================================================

importance = model.feature_importances_

feature_importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": importance
})

feature_importance = feature_importance.sort_values(
    by="Importance",
    ascending=False
)

print("\n================================================")
print("             FEATURE IMPORTANCE")
print("================================================")

print(feature_importance)

plt.figure(figsize=(8, 5))

plt.bar(
    feature_importance["Feature"],
    feature_importance["Importance"]
)

plt.title("Feature Importance - Decision Tree")
plt.xlabel("Features")
plt.ylabel("Importance")

plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig(
    "feature_importance.png",
    dpi=300
)

# IMPORTANT:
# Close the figure instead of plt.show()
plt.close()

print("\nFeature importance graph saved as: feature_importance.png")

# ============================================================
# 17. DECISION TREE VISUALIZATION
# ============================================================

plt.figure(figsize=(22, 12))

plot_tree(
    model,
    feature_names=X.columns,
    class_names=target_encoder.classes_,
    filled=True,
    rounded=True,
    fontsize=9
)

plt.title(
    "Decision Tree for Smart Loan Approval"
)

plt.tight_layout()

plt.savefig(
    "decision_tree.png",
    dpi=300
)

# IMPORTANT:
# Close the figure instead of plt.show()
plt.close()

print("\nDecision tree saved as: decision_tree.png")

# ============================================================
# 18. TEST NEW CUSTOMER
# ============================================================

print("\n================================================")
print("             NEW CUSTOMER PREDICTION")
print("================================================")

# Example customer
new_customer = pd.DataFrame({
    "Income": [65000],

    "CreditScore": [750],

    "EmploymentStatus": [
        employment_encoder.transform(
            ["Employed"]
        )[0]
    ],

    "LoanAmount": [400000],

    "RepaymentHistory": [
        repayment_encoder.transform(
            ["Good"]
        )[0]
    ]
})

print("\nNew Customer Input:")
print(new_customer)

prediction = model.predict(new_customer)

prediction_probability = model.predict_proba(
    new_customer
)

prediction_label = target_encoder.inverse_transform(
    prediction
)

print("\nLoan Approval Prediction:")
print(prediction_label[0])

print("\nPrediction Probability:")

for class_name, probability in zip(
    target_encoder.classes_,
    prediction_probability[0]
):
    print(
        f"{class_name}: {probability * 100:.2f}%"
    )

# ============================================================
# 19. SAVE TEST PREDICTIONS
# ============================================================

results = X_test.copy()

results["Actual"] = target_encoder.inverse_transform(
    y_test
)

results["Predicted"] = target_encoder.inverse_transform(
    y_pred
)

results.to_csv(
    "prediction_results.csv",
    index=False
)

print("\nTest predictions saved as: prediction_results.csv")

# ============================================================
# 20. SAVE FEATURE IMPORTANCE
# ============================================================

feature_importance.to_csv(
    "feature_importance.csv",
    index=False
)

print(
    "Feature importance data saved as: "
    "feature_importance.csv"
)

# ============================================================
# 21. FINAL OUTPUT
# ============================================================

print("\n================================================")
print("             FILES GENERATED")
print("================================================")

print("1. decision_tree.png")
print("2. confusion_matrix.png")
print("3. feature_importance.png")
print("4. prediction_results.csv")
print("5. feature_importance.csv")

print("\n================================================")
print("       SMART LOAN APPROVAL COMPLETED")
print("================================================")