# 🩺 Diabetes Prediction using Logistic Regression

# 📌 End-to-End Healthcare Machine Learning Project

## 📖 Project Overview

This project focuses on predicting whether a patient is likely to have diabetes using:

# Logistic Regression

The project demonstrates a complete end-to-end Machine Learning workflow including:

✔ Exploratory Data Analysis (EDA)  
✔ Healthcare Data Preprocessing  
✔ Missing Value Handling  
✔ Logistic Regression Classification  
✔ Model Evaluation  
✔ ROC-AUC Analysis  
✔ Feature Interpretation  
✔ Streamlit Deployment  
✔ Explainable Healthcare AI

This project simulates how Machine Learning can support:

- early disease prediction
- preventive healthcare systems
- medical risk assessment
- healthcare decision support

using patient medical data.

---

# 🎯 Business Problem

Diabetes is one of the most common chronic diseases worldwide.

Early prediction of diabetes can help healthcare systems:

- identify high-risk patients
- improve preventive treatment
- reduce medical complications
- optimize healthcare resources

The objective of this project is to build a Machine Learning model capable of predicting:

# 🧬 Diabetes Risk

using patient medical features such as:

- Glucose
- BMI
- Blood Pressure
- Insulin
- Age
- Pregnancies
- Skin Thickness
- Diabetes Pedigree Function

This project reflects how AI and Machine Learning are increasingly being used in real-world healthcare analytics.

---

# 📊 Dataset Information

The dataset contains patient medical information with the following features:

| Feature | Description |
|---|---|
| Pregnancies | Number of pregnancies |
| Glucose | Glucose level |
| BloodPressure | Blood pressure level |
| SkinThickness | Skin fold thickness |
| Insulin | Insulin level |
| BMI | Body Mass Index |
| DiabetesPedigreeFunction | Hereditary diabetes risk |
| Age | Patient age |
| Outcome | Target Variable (0 = No Diabetes, 1 = Diabetes) |

---

# 🧠 Machine Learning Workflow

---

# 1️⃣ Exploratory Data Analysis (EDA)

Performed detailed healthcare EDA to understand:

- feature distributions
- medical relationships
- outliers
- class balance
- diabetes-related patterns

## 📈 Visualizations Used

- Histograms
- Boxplots
- Pairplots
- Correlation Heatmaps
- Outcome-wise Analysis
- ROC Curve

---

## 🔍 Key EDA Insights

✔ Patients with higher glucose levels showed higher diabetes probability  
✔ BMI positively influenced diabetes risk  
✔ Older patients showed increased diabetes likelihood  
✔ Some medical variables contained invalid zero values representing missing data

---

# 2️⃣ Data Preprocessing

Performed healthcare-specific preprocessing including:

✔ Replacing medically invalid zero values  
✔ Missing Value Handling using Median Imputation  
✔ Duplicate Record Removal  
✔ Feature Scaling using StandardScaler  
✔ Feature & Target Separation

---

## ⚠️ Important Healthcare Observation

Features such as:

- Glucose
- BloodPressure
- BMI
- Insulin

cannot realistically be zero.

These values were treated as:

# Missing Values

and handled using:

# Median Imputation

Very important healthcare preprocessing step.

---

# 3️⃣ Train-Test Split

The dataset was divided into:

- 80% Training Data
- 20% Testing Data

Used:

# Stratified Sampling

to preserve class balance in both datasets.

---

# 4️⃣ Logistic Regression Model

Built a:

# Binary Classification Model

using Logistic Regression to predict:

- Diabetes (1)
- No Diabetes (0)

---

# 📐 Logistic Regression Formula

```math
P(Y=1) = 1 / 1 + e^(β0 + β1x1 + ... + βnxn)
```

Where:

- **P(Y=1)** = Probability of Diabetes
- **X** = Medical Features
- **β** = Coefficients

---

# 5️⃣ Model Evaluation

Evaluated the model using industry-standard classification metrics:

| Metric | Purpose |
|---|---|
| Accuracy | Overall prediction correctness |
| Precision | Correctness of positive predictions |
| Recall | Ability to identify diabetic patients |
| F1-Score | Balance between Precision & Recall |
| ROC-AUC | Classification quality |

---

# 🚨 Why Recall Was Important

In healthcare systems:

# Missing actual diabetic patients can be dangerous.

Therefore:

# Recall

became one of the most important evaluation metrics in this project.

---

# 6️⃣ Confusion Matrix Analysis

Used confusion matrix to analyze:

- True Positives
- True Negatives
- False Positives
- False Negatives

This helped understand prediction behavior and healthcare risk implications.

---

# 7️⃣ ROC-AUC Analysis

Performed:

# ROC Curve Visualization

to evaluate:

- classification threshold behavior
- class separation quality
- overall prediction reliability

---

## 📈 ROC-AUC Interpretation

| ROC-AUC Score | Meaning |
|---|---|
| 1.0 | Perfect Classifier |
| 0.5 | Random Guessing |
| Higher | Better Model |

---

# 8️⃣ Feature Interpretation & Explainability

Interpreted Logistic Regression coefficients to understand:

✔ feature importance  
✔ medical significance  
✔ diabetes risk factors

---

## 🔬 Most Important Predictors

### Glucose

Strongest indicator of diabetes risk.

---

### BMI

Higher BMI increased diabetes probability.

---

### Age

Older patients generally showed higher diabetes likelihood.

---

### DiabetesPedigreeFunction

Captured hereditary diabetes risk.

---

# 9️⃣ Streamlit Deployment

Built an interactive:

# 🖥️ Diabetes Prediction Web Application

using:

# Streamlit

Users can:

✔ enter patient medical information  
✔ click Predict  
✔ receive real-time diabetes risk predictions

This converts the ML model into a usable healthcare AI application.

---

# 📂 Project Structure

```text
Diabetes Prediction using Logistic Regression/
│
├── diabetes.csv
├── Diabetes_Prediction_Logistic_Regression.ipynb
├── app.py
├── diabetes_model.pkl
├── scaler.pkl
├── requirements.txt
└── README.md
```
## Run app.py By :-
python -m streamlit run app.py

---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Pickle
- Jupyter Notebook

---

# 💡 Skills Demonstrated

✔ Logistic Regression  
✔ Binary Classification  
✔ Healthcare Analytics  
✔ Exploratory Data Analysis (EDA)  
✔ Medical Data Preprocessing  
✔ Feature Scaling  
✔ ROC-AUC Analysis  
✔ Confusion Matrix Analysis  
✔ Explainable AI  
✔ Streamlit Deployment  
✔ Production-Oriented Machine Learning

---

# 📈 Business & Healthcare Impact

This project demonstrates how Machine Learning can support:

- early disease prediction
- preventive healthcare systems
- medical decision support
- healthcare risk assessment
- AI-powered patient screening

The project reflects how data-driven healthcare analytics can improve patient outcomes and operational efficiency.

---

# 🚀 Future Improvements

- Hyperparameter Tuning
- Cross-Validation
- Advanced Classification Models
- Cloud Deployment
- Real-Time Healthcare API Integration
- Deep Learning-Based Medical Prediction

---

# 👨‍💻 Author

# Kailash Singh Rawat

🎓 MCA (Data Science) Student  
📊 Aspiring Data Analyst / Data Scientist

---

# ⭐ Final Note

I strongly believe:

> Machine Learning in healthcare should not only be accurate.  
> It should also be interpretable, reliable, and clinically meaningful.

Because:

Bad Healthcare Data → Bad Predictions  
Bad Predictions → Dangerous Decisions

Strong healthcare AI begins with understanding medical data deeply before building models.

---

# ⭐ If you found this project valuable, feel free to explore and connect.