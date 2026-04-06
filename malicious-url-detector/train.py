import pandas as pd
from src.features import extract_features
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import pickle

# Load dataset
df = pd.read_csv("data/urls.csv")

# Take small data first
df = df[:5000]

# Extract features
feature_list = []
for url in df['url']:
    feature_list.append(extract_features(url))

X = pd.DataFrame(feature_list)
y = df['isMalicious']

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(n_estimators=100, n_jobs=-1)
model.fit(X_train, y_train)

print("Model trained!")

# Evaluate
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Save model
with open("models/rf_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved!")
