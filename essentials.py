import streamlit as st

st.set_page_config(page_title="Learn Essentials", layout="wide")

st.title("📘 Learn the Essentials")

st.warning("This tool is intended as a decision-support assistant. It does not replace medical diagnosis or judgment.")

st.header("🩺 What is the Purpose of this App?")
st.write("This app is designed to support healthcare professionals in quickly assessing a patient's risk of experiencing a stroke.")
st.write("By collecting a few routine clinical indicators, the app uses an AI-powered model to estimate stroke risk and offers insights into contributing risk factors.")
st.write("Its goal is not to replace clinical judgment, but to provide an easy-to-use, explainable second opinion, that supports early prevention and personalized patient guidance.")


st.header("🧠 What is Behind the Scenes?")
st.subheader("📊 The Dataset")
st.write("""
The model was trained on the **Stroke Prediction Dataset from Kaggle**, a publicly available health dataset 
that includes over 40,000 patient records with the following features:

- Age, BMI, Glucose levels
- Presence of hypertension or heart disease
- Lifestyle indicators (smoking status, physical activity)
- Work type, marital status, gender, etc.
- Target label: whether the patient has had a stroke

Some preprocessing was done to clean missing values (e.g., imputing BMI), and unknown categories were filtered out.
""")

st.subheader("🧪 The Model")
st.write("""
After evaluating several models such as Random Forests and Neural Networks, 
**Logistic Regression** was chosen for the final app because:

- It is **highly interpretable**, making it easy to understand the influence of each feature.
- It performed competitively in terms of **accuracy and fairness**.
- It allows **explanation via SHAP values**, which highlight how each input contributes to the prediction.

We trained the model using stratified 80/20 train-test split, applied feature scaling and one-hot encoding,
and ensured class balancing due to the low frequency of positive stroke cases.
""")

st.subheader("🔬 What Analysis Was Performed?")
st.write("""
- **Exploratory Data Analysis (EDA)** to understand feature distributions and missing values.
- **Fairness Assessment** on key demographic attributes (e.g., gender).
- **Model Evaluation** using metrics like ROC-AUC, precision-recall, and confusion matrix.
- **SHAP Analysis** to understand individual predictions and global feature importance.

This ensures the model is not only accurate, but also **transparent and ethically grounded**.
""")


st.header("🔍 Interpreting the Results")
st.write("""
When you use the prediction tool, the results page is divided into sections:
""")
st.markdown("""
- **🧠 Stroke Risk Evaluation**: 
  - Indicates **Low**, **Medium**, or **High** risk.
  - Displays the **probability** score.
  - Suggests a recommended **clinical action**.

- **🔍 Why the AI Made This Prediction**:
  - Uses SHAP values to highlight the **top contributing features**.
  - Helps explain **what factors increased or decreased the risk**.

- **📋 Patient Profile**:
  - Lists the patient's entered data for quick reference.
  - Includes a chart comparing **BMI** and **Glucose** values against clinical thresholds.
""")

st.subheader("💡 What to Recommend at Each Risk Level?")
st.markdown("""
- **LOW Risk** ✅  
  - Reassure the patient.  
  - Promote healthy habits and regular check-ups.  

- **MEDIUM Risk** 🟠  
  - Recommend lifestyle adjustments: diet, physical activity.  
  - Consider further testing if clinical suspicion exists.  

- **HIGH Risk** ⚠️  
  - Consider urgent referral for diagnostics.  
  - Monitor or intervene depending on history and comorbidities.
""")

st.subheader("📌 What to Watch For: Risk Factors Explained")
st.markdown("""
| Risk Factor        | Interpretation                        | Clinical Tip                                          |
|--------------------|----------------------------------------|--------------------------------------------------------|
| **High BMI**        | Obesity is a known stroke risk.        | Encourage weight management, dietary counseling.       |
| **High Glucose**    | May signal prediabetes or diabetes.    | Recommend blood sugar control, diabetes screening.     |
| **Heart Disease**   | Increases cardioembolic stroke risk.   | Review medications, consider cardiology follow-up.     |
| **Hypertension**    | Major modifiable stroke risk.          | Review BP control, lifestyle counseling.               |
""")

