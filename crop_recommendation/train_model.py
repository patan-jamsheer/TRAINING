import os
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

DATA_PATH = "crop_recommendation.csv"
MODEL_DIR = "model"
MODEL_PATH = os.path.join(MODEL_DIR, "random_forest_model.pkl")

FEATURES = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]
TARGET = "label"

df = pd.read_csv(DATA_PATH)

# Basic validation
required = FEATURES + [TARGET]
missing = [col for col in required if col not in df.columns]
if missing:
    raise ValueError(f"Missing columns in CSV: {missing}")

df = df.dropna(subset=required)

X = df[FEATURES]
y = df[TARGET]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

model = RandomForestClassifier(
    n_estimators=300,
    random_state=42,
    n_jobs=-1,
    class_weight=None
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print(f"Test Accuracy: {accuracy * 100:.2f}%")
print("\nClassification Report:")
print(classification_report(y_test, predictions))

os.makedirs(MODEL_DIR, exist_ok=True)
joblib.dump(model, MODEL_PATH)

print(f"\nModel saved to: {MODEL_PATH}")
