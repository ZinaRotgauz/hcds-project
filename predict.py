import streamlit as st
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import shap


FEATURE_NAME_MAP = {
    "num__age": "Age",
    "num__avg_glucose_level": "Average Glucose Level",
    "num__bmi": "BMI",
    "num__hypertension": "Hypertension",
    "num__heart_disease": "Heart Disease",
    
    "cat__gender_Male": "Gender: Male",
    "cat__gender_Female": "Gender: Female",
    "cat__ever_married_Yes": "Marital Status: Married",
    "cat__ever_married_No": "Marital Status: Not Married",
    "cat__Residence_type_Urban": "Residence: Urban",
    "cat__Residence_type_Rural": "Residence: Rural",
    "cat__smoking_status_formerly smoked": "Smoking Status: Former Smoker",
    "cat__smoking_status_never smoked": "Smoking Status: Never Smoked",
    "cat__smoking_status_smokes": "Smoking Status: Smoker",
    "cat__work_type_Private": "Work Type: Private",
    "cat__work_type_Self-employed": "Work Type: Self-Employed",
    "cat__work_type_Govt_job": "Work Type: Government Job",
    "cat__work_type_Never_worked": "Work Type: Never Worked",
    "cat__work_type_children": "Work Type: Child/Student",
}


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

def classify_risk(prob):
    if prob >= 0.7:
        return "HIGH", "red", "⚠️ Refer to a specialist immediately."
    elif prob >= 0.4:
        return "MEDIUM", "orange", "📋 Recommend lifestyle changes and regular checkups."
    else:
        return "LOW", "green", "✅ No urgent action. Maintain healthy habits."
    
st.title("🔎 Enter Patient Information")

col_right,col_left = st.columns(2)

with col_left:
    age = st.number_input("Age", min_value=1, max_value=100, value=30)
    hypertension = st.selectbox("Hypertension", ("Yes", "No"))
    heart_disease = st.selectbox("Heart Disease", ("Yes", "No"))
    avg_glucose_level = st.number_input("Average Glucose Level", min_value=0.0, value=80.0)
    bmi = st.number_input("BMI", min_value=0.0, value=20.0)


with col_right:
    gender = st.selectbox("Gender", ("Male", "Female"))
    smoking_status = st.selectbox("Smoking Status", ("formerly smoked", "never smoked", "smokes"))
    ever_married = st.selectbox("Ever Married", ("Yes", "No"))
    work_type_display = {
        "Private Company": "Private",
        "Self-employed / Freelancer": "Self-employed",
        "Government Job": "Govt_job",
        "Never Worked": "Never_worked",
        "Underage / Child": "children"
    }
    work_type_label = st.selectbox("Work Type", list(work_type_display.keys()))
    work_type = work_type_display[work_type_label]

    residence_type = st.selectbox("Residence Type", ("Urban", "Rural"))

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

if st.button("Predict Stroke"):
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]
    risk_level, risk_color, recommendation = classify_risk(probability)

    st.subheader("🧠 Stroke Risk Evaluation")
    with st.container():
        st.markdown(f"**Risk Level:** <span style='color:{risk_color}; font-weight:bold'>{risk_level}</span>", unsafe_allow_html=True)
        st.markdown(f"**Probability:** {probability:.2%}")
        st.markdown(f"**Recommendation:** {recommendation}")

    shap_explainer = shap.Explainer(model.named_steps['classifier'], model.named_steps['preprocessor'].transform(X_background))
    input_transformed = model.named_steps['preprocessor'].transform(input_data)
    shap_values = shap_explainer(input_transformed)
    feature_names = model.named_steps['preprocessor'].get_feature_names_out()


    st.subheader("📋 Patient Profile")
    col1, col2 = st.columns(2)
    with col1:
        col1_1,col1_2 = st.columns(2)
        with col1_1:
            st.write(f"**Age:** {age}")
            st.write(f"**BMI:** {bmi}")
            st.write(f"**Avg. Glucose Level:** {avg_glucose_level}")
            st.write(f"**Heart Disease:** {heart_disease}")
            st.write(f"**Hypertension:** {hypertension}")
        with col1_2:
            st.write(f"**Gender:** {gender}")
            st.write(f"**Family status** {ever_married}")
            st.write(f"**Occupation:** {work_type}")
            st.write(f"**Smoking Status:** {smoking_status}")
            st.write(f"**Resindence type:** {residence_type}")


    with col2:
        st.write("📊 Clinical Reference Comparison")

        col_bmi, col_glucose = st.columns(2)

        with col_bmi:
            fig_bmi, ax_bmi = plt.subplots(figsize=(4, 3))
            bmi_color = "green" if bmi <= 24.9 else "orange" if bmi < 30 else "red"
            ax_bmi.bar(["BMI"], [bmi], color=bmi_color)
            ax_bmi.axhline(30, color='red', linestyle='--', linewidth=1, label="BMI ≥ 30")
            ax_bmi.axhline(24.9, color='gray', linestyle=':', linewidth=1, label="BMI Normal Upper")
            ax_bmi.set_ylim(0, max(bmi + 10, 50))
            ax_bmi.set_title("BMI vs Clinical Thresholds")
            ax_bmi.text(0, bmi + 1, f"{bmi:.1f}", ha='center')
            ax_bmi.legend(loc='upper right')
            st.pyplot(fig_bmi)

        with col_glucose:
            fig_glucose, ax_glucose = plt.subplots(figsize=(4, 3))
            glucose_color = "green" if avg_glucose_level <= 99 else "orange" if avg_glucose_level < 126 else "red"
            ax_glucose.bar(["Glucose"], [avg_glucose_level], color=glucose_color)
            ax_glucose.axhline(126, color='darkred', linestyle='--', linewidth=1, label="Glucose ≥ 126")
            ax_glucose.axhline(99, color='gray', linestyle=':', linewidth=1, label="Glucose Normal Upper")
            ax_glucose.set_ylim(0, max(avg_glucose_level+50, 180))
            ax_glucose.set_title("Glucose vs Clinical Thresholds")
            ax_glucose.text(0, avg_glucose_level + 2, f"{avg_glucose_level:.1f}", ha='center')
            ax_glucose.legend(loc='upper right')
            st.pyplot(fig_glucose)



    st.subheader("🔍 Why did the AI make this prediction?")
    with st.expander("See Details"):
        

        st.subheader("Top contributing features:")
        with st.container(border=True):
            top_feats = shap_values[0].values.argsort()[::-1][:5]
            for idx in top_feats:
                raw_name = feature_names[idx]
                shap_val = shap_values[0].values[idx]
                direction = "⬆ increases risk" if shap_val > 0 else "⬇ decreases risk"
                readable_name = FEATURE_NAME_MAP.get(raw_name, raw_name.replace("num__", "").replace("cat__", "").replace("_", " ").title())
                st.write(f"- **{readable_name}** ({direction}) — contribution: {shap_val:.3f}")

        st.markdown("""
        > **ℹ️ What does “contribution” mean in the SHAP graph?**  
        > A contribution represents how much a specific feature influenced the prediction.  
        > - 🟥 A **positive contribution** (red) increases the stroke risk  
        > - 🟦 A **negative contribution** (blue) decreases the stroke risk  
        >  
        > The SHAP waterfall chart shows how the model moves from the average prediction  
        > (shown as *E[f(x)]*) to the final stroke risk for this individual, based on their personal data.
        """)

        fig, ax = plt.subplots(figsize=(8, 5))
        readable_feature_names = [
            FEATURE_NAME_MAP.get(name, name.replace("num__", "").replace("cat__", "").replace("_", " ").title())
            for name in feature_names
        ]
        shap.plots.waterfall(shap.Explanation(values=shap_values[0].values,
                                            base_values=shap_values.base_values[0],
                                            data=input_transformed[0],
                                            feature_names=readable_feature_names),
                            show=False)
                            
        st.pyplot(fig)
