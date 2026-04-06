import streamlit as st
import pandas as pd
from predict import predict_url
from src.features import extract_features

st.set_page_config(page_title="URL Threat Analyzer", page_icon="🔍", layout="wide")

st.title("🔍 URL Threat Analyzer")

url = st.text_input("Enter URL")

if st.button("Analyze"):
    features = extract_features(url)
    pred, conf = predict_url(url)

    col1, col2 = st.columns(2)

    with col1:
        if pred == 1:
            st.error(f"⚠️ Malicious ({conf*100:.2f}%)")
        else:
            st.success(f"✅ Safe ({conf*100:.2f}%)")

    with col2:
        st.metric("URL Length", features['url_length'])
        st.metric("Dots", features['dot_count'])
        st.metric("Suspicious Words", features['suspicious_keywords'])

    st.subheader("🔍 Feature Breakdown")
    st.dataframe(pd.DataFrame([features]).T.rename(columns={0: 'Value'}))
