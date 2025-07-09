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
![Main_page](https://github.com/user-attachments/assets/96c7b92f-bd4b-4bbe-9cb9-b5cf25b3c7c2)
![1](https://github.com/user-attachments/assets/c99eff77-8b30-4ebc-8317-2409706fea65)
![2](https://github.com/user-attachments/assets/287c0061-096d-424e-8670-6e75a5d41bc0)
![3](https://github.com/user-attachments/assets/f7d07553-c430-4667-80b1-3354daf54f52)
![4](https://github.com/user-attachments/assets/f6129da8-26f8-4883-aed4-9d699cc936b3)


## EDA & main insights

Dataset has 5110 rows.
There are missing values in bmi column.
There is 2 more numeric Column than text columns.
Due to the imbalance in the dataset, with only 249 individuals having had a stroke, we will apply over-sampling (SMOTE) to increase the number of stroke cases and balance the dataset.
![image](https://github.com/user-attachments/assets/b05b0a16-862b-4db6-a749-fae32b1570d4)

As we can see the stroke cases are pretty imbalanced, although the gender groups are represented equally.
But let's see the representation of other features:
![image](https://github.com/user-attachments/assets/eccc0dbe-ca16-45e2-b951-aa0a69be0512)


We have a good age distribution. I think we have disparities in BMI. The average glucose distribution is acceptable, as the normal average blood sugar level is less than 140, which may not be good; this feature will not be useful for determining the correlation between diabetes and strokes.

![image](https://github.com/user-attachments/assets/d1489ffe-e86a-4656-a563-7aa4011e8085)

![image](https://github.com/user-attachments/assets/8bc6a638-7235-4bc6-96e7-f6683957d9b8)

- The average glucose level is high in elderly people.
- BMI >40 has a low average glucose level.

### The correlation matrix will show us if the data about BMI could be effective in decision making
We can see that BMI doesn"t really influence the Stroke, however age is one of the most deciding points, followed by previous heart deseases and glucose level.
With the further analysis we saw, that the high BMI (over 49.9) feature doesnt reallyinfluence the stroke feature: high BMI - 79 entries, but with stroke - only 1
![image](https://github.com/user-attachments/assets/3d59232d-3d9c-4790-9d13-053aa27cecaa)

# Interview Guide
## Consent Question
Before we begin, do I have your permission to use your answers from this interview for our project’s research and final presentation? Your identity will not be disclosed.

## Project Introduction
We’re designing a decision-support tool for doctors during routine checkups. It helps assess stroke risk using patient data (like age, glucose, BMI, and medical history). Rather than just saying ‘high’ or ‘low’ risk, it groups patients into profiles and explains why — so doctors can give personalized guidance.
We’d like your input on how this might work in your practice, and whether it provides value.

## Starting questions
1. Do you use many digital tools or apps in your practice?
2. Would you be open to using AI-based support tools in checkups?
3. How do you currently assess stroke risk?

## Task-related questions
Task1: Imagine you’re seeing a new patient during a routine checkup. Could you walk me through how you’d use this tool to input their information?<br>
Question: Is anything unclear while entering the data? Would you expect anything to happen at this stage?

Task2: You’ve now entered the data and pressed ‘Predict Stroke Risk’. What do you expect to see next? How would you use this information in your conversation with the patient?<br>
Question: What would you tell the patient based on the output? Would you want more context around the prediction — such as confidence or comparison to averages?

Task3:Imagine the system now groups the patient into a certain risk profile, and you can click on that profile to see common features of people in the same group. What do you expect to see?<br>
Questions: Would this kind of profile grouping help your decision-making? How would you explain it to a patient?

Task4: Imagine you want to show your patient how their stroke risk changes if they reduce their glucose level or quit smoking. How would you do this using the tool?<br>
Questions: Would this motivate behavior change for the patient? Would a side-by-side comparison help?

Task5: You’ve completed the checkup and want to record the result or share it with another specialist. What would you do?<br>
Question: Would you want to add notes or see documentation of how the result was calculated? Would you prefer export, print, or integration with an EHR system?

## Open-ended questions
1. What do you like about this interface or system?

2. What part is most confusing or unhelpful?

3. What information would you like to see that is currently missing?

4. How would you integrate this tool into your routine?

5. Would this change how you explain risk to patients?

6. Is there any risk in relying on this prediction? What would you need to feel confident?

# Technical details
For our research we are going to consider Logical Regression and Random Forest models and evaluate their accuracy for answering our research questions. This is because Logical Regression is highly interpretable and works well with binary targets, and it also explains which features contributes most to stroke risks. Random Forest also has high interpretability. It handles missing values well and ranks feature importance.

# User Study Feedback

## 1. **Summary of Feedback from User Study**

**Interview 1:**
- **Part 1 – Input Form:**
  - Add “diverse” option to gender field.
  - “Ever Married?” label unclear—needs better wording.
  - Work type categories are ambiguous or confusing.

- **Part 2 – Stroke Risk Prediction:**
  - Only low-risk result shown—users want to see what a high-risk case looks like.
  - Desire for follow-up recommendations from the AI in case of high risk (e.g., medication, further checks).
  - BMI and glucose are hard to interpret on the same scale—users suggest using different scales.
  - Add reasoning for why BMI and glucose are emphasized.

- **Part 3 – AI Explanation (SHAP plot):**
  - Combine textual and graphical explanation for clarity.
  - Variable names are not intuitive for non-technical users.
  - Remove grey values (less useful) on SHAP bar chart.
  - Keep arrows and make top variables more visually prominent.
  - Add explanation for color meaning (blue/red) and value interpretation.

**Interview 2:**
- **Part 1 – Input UI:**
  - Input fields take too much vertical space; split into two columns to fit one screen.

- **Part 2 – Risk Result Display:**
  - Positive visual feedback: colors of risk levels are clear and intuitive.
  - Threshold line in the risk plot is not prominent.
  - Users want more context on why certain features contribute the most.
  - Suggestion: show similar patient comparisons to explain risk better.

- **Part 3 – AI Explanation:**
  - Variable names lack contrast—need clearer visual emphasis.
  - “Top contributing features” list is hard to scan—should be paired with mini graphs and a clearer layout with a right-aligned variable name column.

---

## 2. **Design Implications Discussed**

- **Inclusivity & Clarity in Inputs:**
  - Rethink form labels (e.g., “Ever Married?”) for clarity.
  - Update gender options to reflect diversity.
  - Replace ambiguous terms in dropdowns with user-friendly labels.

- **Interpretability & Actionability of Results:**
  - Visualize both low and high-risk cases for contrast.
  - Add recommendations or clinical follow-up suggestions when risk is high.
  - Separate BMI and glucose in visual comparisons to avoid confusion.
  - Explain why certain features matter using comparisons or short notes.

- **Improved SHAP Explanation:**
  - Merge text + visual explanation.
  - Clarify the color coding (red = increase risk, blue = decrease).
  - Remove non-informative elements like grey bars.
  - Use layout and color to emphasize the most important variables.

- **Better Layout & Usability:**
  - Redesign form layout to reduce scrolling (two-column format).
  - Ensure each part fits within one screen for smoother navigation.
  - Use cleaner, more structured layout in feature explanations.

---

## 3. **Planned Changes Based on Feedback**

- ✅ Add “diverse” to gender options and relabel “Ever Married?”  
- ✅ Refactor input UI to 2-column layout to reduce screen space  
- ✅ Show example of high-risk prediction, not just low-risk  
- ✅ Add clinical recommendation note if risk is high  
- ✅ Plot BMI and glucose on separate axes with brief explanation  
- ✅ Update SHAP plot: remove grey bars, keep arrows, highlight top variables  
- ✅ Add visual legend for SHAP plot color meaning  
- ✅ Improve variable name clarity and contrast in feature lists  
- ✅ Add comparison to similar patients in explanation section  

