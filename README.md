# Dataset documentation

**Dataset Name**: Stroke Prediction

**Source / Link**:[Kaggle - Stroke Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset/data)

**Domain / Context**: Public health and preventive medicine — cerebrovascular event risk assessment

**Number of Instances**:  5,110

**Number of Features**:  11 features + 1 target

**Possible Target Variable(s)**:  stroke (0 = No, 1 = Yes)

**Data Access & License**:  Publicly available for research and educational purposes via Kaggle

The dataset provides demographic, lifestyle, and medical information for individuals with the goal of predicting whether a person is likely to suffer a stroke. It includes features such as age, gender, hypertension, heart disease, average glucose level, BMI, work type, and smoking status. The dataset is imbalanced, with only about 5% of the entries indicating a stroke event.

- The dataset was uploaded by Kaggle user fedesoriano. It's a confidential source, available for educational or research purposes, provided that an acknowledgment is given to the original author
- No additional info about how the data was collected, funding or sponsorship for the dataset’s creation.
- was uploaded to Kaggle approximately four years ago.

# Attribute description

- id: unique identifier for each patient
- gender: gender of the patient, "Male", "Female" or "Other"
- age: age of the patient 
- hypertension: 0 if no hypertension, 1 if the patient has hypertension
- heart_disease: 0 if no heart disease, 1 if the patient has heart disease
- ever_married: "Yes" or "No" 
- work_type: type of occupation, "children", "Govt_jov", "Never_worked", "Private" or "Self-employed"
- Residence_type: "Urban" or "Rural"
- avg_glucose_level: average glucose level in blood
- bmi: Body Mass Index
- smoking_status: "formerly smoked", "never smoked", "smokes" or "Unknown" (if the information is unavailable for one patient)
- stroke: 0 if no stroke, 1 if the patient had a stroke. Target variable

# Decision scenario


## Real-world application

Stroke is considered one of the most popular reasons of human death, responsible for approximately 11% of total deaths. 
This dataset is used to predict whether a patient is likely to get stroke based on the input parameters like gender, age, various diseases, and smoking status. Each row in the data provides relavant information about the patient.

Our idea is to explore and analyze the data and get the key insights that will help to form important policies and educational models to prevent the spreading of the disease.


**A hospital implements a decision-support system aimed at preventive health profiling to help general practitioners segment patients into stroke risk groups during routine checkups. Rather than offering a binary risk outcome, the ML model assigns patients to different risk clusters based on features such as age, BMI, glucose level, smoking status, and medical history.**

The model supports physicians by offering an interpretable profile of a patient's risk group and suggesting personalized preventive interventions such as lifestyle changes, diagnostic referrals, or follow-up schedules. This clustering approach helps doctors proactively manage high-risk individuals before stroke symptoms occur.

* **Use Case:** A general practitioner uses the system during preventive checkups to categorize patients into risk profiles and offer targeted health guidance.

* **Type of ML Task:** Unsupervised clustering with follow-up profiling (and optional classification for stroke occurrence prediction)

**Constraints & Requirements:**

* Interpretability: Physicians must be able to understand and explain risk group assignments.

* Actionability: Each risk profile must correspond to meaningful and distinct health advice.

* Data Imbalance: Few stroke cases limit traditional classification reliability.

* Clinical Validity: Risk clusters must align with medically known stroke risk factors.

* Privacy: All patient data must remain confidential under applicable health data protection laws (e.g., GDPR).

What’s at Stake: 
 * Missed opportunities for early intervention, or overburdening low-risk individuals with unnecessary procedures. The goal is to allocate preventive resources effectively and ethically.


# Stakeholder Analysis
## Public Health Policy Makers
### Goals: 
Improve population health, reduce incidence of strokes through effective early interventions. Optimize resource allocation, save time and money for the public health system
### Objectives: 
Understand how to incorporate model’s output into downstream actions: How should public health programs or resource allocations change based on the model’s risk predictions?
Ensure compliance with standards or regulations – non-discrimination standards / Medical data privacy laws
### Tasks:
Understand influence of different factors: Which factors are most influential? How do they interact?
Understand model strengths and limitations: Where is the model reliable? Where is it weak? Helps avoid misuse of the model.







## Health Profiling
### Segment the population into health risk groups to support personalized intervention strategies.

 Can we cluster patients based on features (e.g., age, BMI, glucose) into distinct risk profiles?

 What are the characteristics of high-risk clusters?

How do health outcomes (stroke occurrence) differ between these clusters?

 Which lifestyle modifications are most associated with low-risk groups?


## Health Policy Analysis
### Use data to inform policies for stroke prevention and education.

What occupational or lifestyle factors are strongly associated with stroke?

Are people in private-sector jobs at greater risk than government or children?

How does stroke risk vary across glucose level or smoking status categories?

What interventions (e.g., glucose monitoring, smoking cessation) might reduce stroke incidence most effectively?

## Constraints and Requirements

- Ethical: cannot discriminate on the basis of gender, age or place of residence.
- Medical: the model must be interpretable for physicians.
- Technical: high accuracy requirements (especially recall - to avoid missing stroke cases).
- Legal: protection of personal medical data (GDPR, HIPAA).

## Stakes

- Financial: if strokes are not prevented early, high medical costs would incur for hospitals and insurance providers
- 

# Techncal details
For our research we are going to consider Logical Regression and Random Forest models and evaluate their accuracy for answering our research questions. This is because Logical Regression is highly interpretable and works well with binary targets, and it also explains which features contributes most to stroke risks. Random Forest also has high interpretability. It handles missing values well and ranks feature importance.
