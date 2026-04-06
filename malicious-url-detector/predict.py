import pickle
import pandas as pd
from src.features import extract_features

model = pickle.load(open("models/rf_model.pkl", "rb"))

def predict_url(url):
    features = extract_features(url)
    df = pd.DataFrame([features])

    pred = model.predict(df)[0]
    proba = model.predict_proba(df)[0]

    return pred, max(proba)

# Test
url = input("Enter URL: ")
pred, conf = predict_url(url)

print("\nResult:", "Malicious" if pred == 1 else "Safe")
print("Confidence:", conf)
