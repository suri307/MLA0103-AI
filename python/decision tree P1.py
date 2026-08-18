import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Dataset
data = {
    'Outlook': ['Sunny','Sunny','Overcast','Rain','Rain','Rain',
                'Overcast','Sunny','Sunny','Rain','Sunny','Overcast',
                'Overcast','Rain'],

    'Temp': ['Hot','Hot','Hot','Mild','Cool','Cool',
             'Cool','Mild','Cool','Mild','Mild','Mild',
             'Hot','Mild'],

    'Humidity': ['High','High','High','High','Normal','Normal',
                 'Normal','High','Normal','Normal','Normal','High',
                 'Normal','High'],

    'Wind': ['Weak','Strong','Weak','Weak','Weak','Strong',
             'Strong','Weak','Weak','Weak','Strong','Strong',
             'Weak','Strong'],

    'Play': ['No','No','Yes','Yes','Yes','No',
             'Yes','No','Yes','Yes','Yes','Yes',
             'Yes','No']
}

df = pd.DataFrame(data)

# Convert categorical values into numbers
X = pd.get_dummies(df[['Outlook', 'Temp', 'Humidity', 'Wind']])
y = df['Play']

# Create Decision Tree using Entropy
model = DecisionTreeClassifier(
    criterion='entropy',
    random_state=42
)

# Train the model
model.fit(X, y)

# Display accuracy
print("Training Accuracy:", model.score(X, y))

# Display tree
plt.figure(figsize=(14, 8))
plot_tree(
    model,
    feature_names=X.columns,
    class_names=model.classes_,
    filled=True
)

plt.title("Decision Tree - Play Tennis")
plt.show()