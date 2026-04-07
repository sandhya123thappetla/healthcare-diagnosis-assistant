import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pickle
import os

# ✅ Load dataset
dataset_path = os.path.join(os.path.dirname(__file__), "..", "data", "dataset.csv")
df = pd.read_csv(dataset_path)

# ✅ Features & target
X = df.drop("prognosis", axis=1)
y = df["prognosis"]

# ✅ Train-test split with stratification
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# ✅ XGBoost model
model = XGBClassifier(
    n_estimators=200,
    learning_rate=0.1,
    max_depth=6,
    random_state=42,
    use_label_encoder=False,
    eval_metric='mlogloss'
)

# ✅ Train model
model.fit(X_train, y_train)

# ✅ Predictions
y_pred = model.predict(X_test)

# ✅ Metrics
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Model Accuracy: {accuracy * 100:.2f}%\n")

print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# ✅ Save model
models_dir = os.path.join(os.path.dirname(__file__), "..", "..", "backend", "models")
os.makedirs(models_dir, exist_ok=True)
model_path = os.path.join(models_dir, "model.pkl")

with open(model_path, "wb") as f:
    pickle.dump(model, f)

print(f"✅ Model saved to {model_path}")


from sklearn.metrics import accuracy_score

# Predictions
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Model Accuracy: {accuracy * 100:.2f}%")



