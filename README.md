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

# Stakeholder Analysis
## ML expert (us) 
| **Goal**      | Understand how the model works | Build trust in the model |
|--------------|-------------------------------|---------------------------|
| **Objectives** | - Debug or improve the model<br>- Ensure compliance with standards or regulations | - Justify or explain actions influenced by the model’s output<br>- Understand how one’s data is being used |
| **Tasks**      | - Assess reliability of predictions<br>- Understand the extent of the information the model is using | - Understand the influence of different factors on the model’s output<br>- Understand model strengths and limitations |

## Public Health Policy Makers
| **Goal**      | Improve population health | Optimize resource allocation |
|--------------|-------------------------------|---------------------------|
| **Objectives** | - Understand how to incorporate model’s output into downstream actions<br>- How should public health programs or resource allocations change based on the model’s risk predictions | - Ensure compliance with standards or regulations<br>- non-discrimination standards / Medical data privacy laws |
| **Tasks**      | - Understand influence of different factors<br>- Which factors are most influential? How do they interact? | - Understand model strengths and limitations<br>- Where is the model reliable? Where is it weak? |

# Prototyping
## Defining Target Audience
Primary Stakeholder: Doctor<br>
Doctos use the application during routine health checkups to identify patients at elevated risk of stroke. This decision-support system segments patients into risk profiles based on their demographic and health data, aiding doctors in tailoring preventive care.
- What prior knowledge to the stakeholders need to use your application?<br>
  Doctors need to understand general health risk factors (age, hypertension, glucose, BMI, etc.). No specific ML knowledge is needed, but a basic understanding of how features contribute to clustering or classification helps.
- What explanations might the stakeholder need?<br>
  Doctors must be able to explain why a patient is classified into a particular risk group. They need visual and textual explanations of key contributing features (e.g., "High glucose and smoking history place this patient in a high-risk cluster").
- What prior knowledge in Data Science is needed to understand the decision?<br>
  Minimal. Explanations should avoid technical jargon and focus on feature importance, trend patterns, and medically relevant insights. Model outputs must be interpretable, perhaps supported by SHAP values or decision trees, with emphasis on medically validated factors.
## Individual Paper Prototypes
![WhatsApp Image 2025-06-10 at 15 31 44](https://github.com/user-attachments/assets/762d3128-092b-4ee5-88c7-c78501b45088)


## Group Paper Prototypes
![photo_2025-06-17_13-58-30](https://github.com/user-attachments/assets/572a4cc5-9b0a-4122-be14-dc9513a9be38)

## Scenario Walkthrough
![WechatIMG464](https://github.com/user-attachments/assets/cc452704-d79d-421a-86bb-1068fe8df867)
![WechatIMG465](https://github.com/user-attachments/assets/178cbe04-a74d-464d-86db-7947dda65e20)
![WechatIMG466](https://github.com/user-attachments/assets/224c6066-3e62-4ab1-8756-0e2d5c386e49)
![WechatIMG467](https://github.com/user-attachments/assets/d274cefc-1018-4950-86e5-420883e73942)
![WechatIMG468](https://github.com/user-attachments/assets/f8c07985-0f24-4e24-b8ab-aa2941a1b548)




# Technical details
For our research we are going to consider Logical Regression and Random Forest models and evaluate their accuracy for answering our research questions. This is because Logical Regression is highly interpretable and works well with binary targets, and it also explains which features contributes most to stroke risks. Random Forest also has high interpretability. It handles missing values well and ranks feature importance.
