import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

from src.evaluation import evaluate_model
from src.feature_importance import plot_feature_importance

# Load dataset
df = pd.read_csv("data/raw/employees.csv")

# ---------------- FIX: USE ONLY 5 FEATURES ----------------
features = ["age", "experience", "salary", "training_hours", "attendance"]

X = df[features]
y = df["performance"]

# Encode target
le = LabelEncoder()
y = le.fit_transform(y)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Accuracy
print("Accuracy:", model.score(X_test, y_test))

# Evaluation
evaluate_model(model, X_test, y_test)

# Feature importance
plot_feature_importance(model, X)

# Save model
import os
os.makedirs("models", exist_ok=True)

with open("models/performance_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved successfully!")