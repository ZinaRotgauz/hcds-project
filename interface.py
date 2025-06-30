import streamlit as st
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import shap

# --- Load Model and Background ---
@st.cache_resource
def load_model():
    with open("logreg_stroke_model.pkl", "rb") as file:
        return pickle.load(file)

@st.cache_resource
def load_background():
    with open("X_background.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()
X_background = load_background()

# --- Risk Classifier ---
def classify_risk(prob):
    if prob >= 0.7:
        return "HIGH", "red", "⚠️ Refer to a specialist immediately."
    elif prob >= 0.4:
        return "MEDIUM", "orange", "📋 Recommend lifestyle changes and regular checkups."
    else:
        return "LOW", "green", "✅ No urgent action. Maintain healthy habits."

# --- App UI ---
st.title("🧠 Stroke Prediction Web App")
st.write("Enter the required information to predict the likelihood of stroke.")

# --- Input Fields ---
age = st.number_input("Age", min_value=1, max_value=100, value=30)
hypertension = st.selectbox("Hypertension", ("Yes", "No"))
heart_disease = st.selectbox("Heart Disease", ("Yes", "No"))
avg_glucose_level = st.number_input("Average Glucose Level", min_value=0.0, value=80.0)
bmi = st.number_input("BMI", min_value=0.0, value=20.0)
gender = st.selectbox("Gender", ("Male", "Female"))
smoking_status = st.selectbox("Smoking Status", ("formerly smoked", "never smoked", "smokes"))
ever_married = st.selectbox("Ever Married", ("Yes", "No"))
work_type = st.selectbox("Work Type", ("Private", "Self-employed", "children", "Govt_job", "Never_worked"))
residence_type = st.selectbox("Residence Type", ("Urban", "Rural"))

# --- Build Input DataFrame ---
input_data = pd.DataFrame([{
    'age': age,
    'avg_glucose_level': avg_glucose_level,
    'bmi': bmi,
    'hypertension': 1 if hypertension == "Yes" else 0,
    'heart_disease': 1 if heart_disease == "Yes" else 0,
    'gender': gender,
    'ever_married': ever_married,
    'work_type': work_type,
    'Residence_type': residence_type,
    'smoking_status': smoking_status
}])

# --- Prediction Block ---
if st.button("🔍 Predict Stroke Risk"):
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    risk_level, risk_color, recommendation = classify_risk(probability)

    st.subheader("🧠 Stroke Risk Evaluation")
    with st.container():
        st.markdown(f"**Risk Level:** <span style='color:{risk_color}; font-weight:bold'>{risk_level}</span>", unsafe_allow_html=True)
        st.markdown(f"**Probability:** {probability:.2%}")
        st.markdown(f"**Recommendation:** {recommendation}")

    # --- SHAP Explanation ---
    shap_explainer = shap.Explainer(model.named_steps['classifier'], model.named_steps['preprocessor'].transform(X_background))
    input_transformed = model.named_steps['preprocessor'].transform(input_data)
    shap_values = shap_explainer(input_transformed)

 
    # --- Patient Profile and Comparison ---
    st.subheader("📋 Patient Profile")
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Name:** John Doe")
        st.write(f"**Age:** {age}")
        st.write(f"**BMI:** {bmi}")
        st.write(f"**Avg. Glucose Level:** {avg_glucose_level}")
        st.write(f"**Heart Disease:** {heart_disease}")
        st.write(f"**Hypertension:** {hypertension}")

    with col2:
        st.write("📊 Clinical Reference Comparison")
        fig, ax = plt.subplots(figsize=(6, 4))
        metrics = ['BMI', 'Glucose']
        values = [bmi, avg_glucose_level]
        colors = [
            "red" if bmi >= 30 else "orange" if bmi > 24.9 else "green",
            "red" if avg_glucose_level >= 126 else "orange" if avg_glucose_level > 99 else "green"
        ]
        bars = ax.bar(metrics, values, color=colors)
        ax.set_ylim(0, max(160, max(values)+20))
        ax.axhline(30, color='red', linestyle='--', linewidth=1, label="BMI ≥ 30")
        ax.axhline(24.9, color='gray', linestyle=':', linewidth=1, label="BMI Normal Upper")
        ax.axhline(126, color='darkred', linestyle='--', linewidth=1, label="Glucose ≥ 126")
        ax.axhline(99, color='gray', linestyle=':', linewidth=1, label="Glucose Normal Upper")
        for i, bar in enumerate(bars):
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2, f"{values[i]:.1f}", ha='center')
        ax.set_title("Health Indicators vs Clinical Thresholds")
        ax.legend(loc='lower right')
        st.pyplot(fig)

    with st.expander("🔍 Why did the AI make this prediction?"):
            st.markdown("Top contributing features for John Doe:")

            top_feats = shap_values[0].values.argsort()[::-1][:5]
            feature_names = model.named_steps['preprocessor'].get_feature_names_out()
            for idx in top_feats:
                feature_name = feature_names[idx]
                shap_val = shap_values[0].values[idx]
                direction = "⬆ increases risk" if shap_val > 0 else "⬇ decreases risk"
                st.write(f"- **{feature_name}** ({direction}) — contribution: {shap_val:.3f}")

            fig, ax = plt.subplots(figsize=(8, 5))
            shap.plots.waterfall(shap.Explanation(values=shap_values[0].values,
                                                base_values=shap_values.base_values[0],
                                                data=input_transformed[0],
                                                feature_names=feature_names),
                                                show=False)
            st.pyplot(fig)
