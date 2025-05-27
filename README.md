# Dataset documentation

- The dataset was uploaded by Kaggle user fedesoriano. It's a confidential source, available for educational or research purposes, provided that an acknowledgment is given to the original author
- No additional info about how the data was collected, funding or sponsorship for the dataset’s creation.
- The dataset was uploaded to Kaggle approximately four years ago.

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

That is why we consider several direction for our research:

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

# Techncal details
For our research we are going to consider, **RandomForest, LogicalRegression** and ... models and evaluate their accuracy for answering our research questions. Later on you will see the attribute comparison of their abilities. 
