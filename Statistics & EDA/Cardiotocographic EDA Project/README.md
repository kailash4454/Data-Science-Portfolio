# Cardiotocographic EDA Project

## Exploratory Data Analysis on Cardiotocographic Dataset

## Project Overview

This project focuses on performing a complete Exploratory Data Analysis (EDA) on the Cardiotocographic dataset to understand fetal heart monitoring patterns, identify medical risk indicators, and generate meaningful healthcare insights using statistical analysis and advanced visualizations.

The project demonstrates how raw medical data can be cleaned, analyzed, and transformed into decision-support insights for healthcare professionals.

This is a strong real-world Data Analytics project involving data cleaning, preprocessing, visualization, correlation analysis, and insight generation.

---

## Problem Statement

The objective of this project is to explore the Cardiotocographic dataset and identify:

* hidden patterns
* abnormal fetal monitoring conditions
* variable relationships
* potential fetal distress indicators
* healthcare decision-support insights

using statistical summaries and advanced EDA techniques.

This project helps answer:

### Which fetal patterns indicate possible medical concern?

### Which variables strongly relate to fetal health?

### How can EDA support pregnancy monitoring and risk detection?

---

## Dataset Information

The dataset contains important fetal monitoring variables such as:

* **LB** → Baseline Fetal Heart Rate (FHR)
* **AC** → Accelerations
* **FM** → Fetal Movements
* **UC** → Uterine Contractions
* **DL** → Decelerations Late
* **DS** → Decelerations Short
* **DP** → Decelerations Prolonged
* **ASTV** → Abnormal Short-Term Variability
* **MSTV** → Mean Short-Term Variability
* **ALTV** → Abnormal Long-Term Variability
* **MLTV** → Mean Long-Term Variability

These features are used to assess fetal well-being and detect abnormal pregnancy conditions.

---

## Project Workflow

### 1. Data Loading and Initial Understanding

* Loaded dataset using Pandas
* Checked shape, columns, and structure
* Used `.info()` and `.head()` for initial understanding

---

### 2. Data Cleaning and Preparation

* Missing value detection and treatment
* Median imputation for numerical columns
* Data type consistency checks
* Safe numeric conversion where required

---

### 3. Outlier Detection and Treatment

* Used IQR (Interquartile Range) method for outlier detection

IQR = Q3 - Q1

* Identified clinically important extreme values
* Applied business-aware interpretation instead of blind deletion

---

### 4. Statistical Summary

Performed descriptive analysis using:

* Mean
* Median
* Standard Deviation
* Interquartile Range (IQR)

This helped identify:

* skewness
* spread
* variability
* abnormal value patterns

---

### 5. Data Visualization

Created:

* Histograms
* Boxplots
* Bar Charts
* Pie Charts
* Scatter Plots
* Correlation Heatmaps
* Pair Plots
* Violin Plots

for deeper analytical understanding.

---

### 6. Categorical Analysis

Created:

### FHR Category

from Baseline Fetal Heart Rate (LB):

* Low
* Normal
* High

This improved medical interpretation and categorical analysis.

---

### 7. Correlation Analysis

Explored relationships between variables using:

* Correlation Heatmap
* Scatter Plots

This helped identify important medical relationships such as:

* Uterine Contractions vs Late Decelerations
* Variability Measures Relationships

---

### 8. Pattern Recognition and Insights

Converted statistical findings into:

# actionable healthcare insights

which support:

* fetal distress detection
* high-risk pregnancy identification
* better monitoring decisions

---

## Key Insights

### Most fetal heart rate observations fall within the Normal range

This suggests overall fetal well-being for the majority of patients.

---

### Strong positive relationship between uterine contractions and late decelerations

This may indicate contraction-related fetal stress and requires closer medical monitoring.

---

### Several variables showed right-skewed distributions

This indicates that while most patients fall within healthy ranges, a smaller number of cases may represent high-risk pregnancies.

---

### Outliers in Baseline FHR may represent clinically significant cases

These should be investigated carefully rather than removed blindly.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Jupyter Notebook

---

## Skills Demonstrated

* Exploratory Data Analysis (EDA)
* Data Cleaning
* Missing Value Handling
* Outlier Detection
* Statistical Analysis
* Data Visualization
* Correlation Analysis
* Medical Data Interpretation
* Healthcare Analytics
* Analyst-Level Business Thinking

---

## Business / Healthcare Impact

This project helps support:

* early fetal distress detection
* pregnancy risk monitoring
* doctor decision support
* high-risk case prioritization
* healthcare analytics dashboards
* future predictive healthcare systems

It shows how strong EDA improves both business intelligence and clinical decision-making.

---

## Future Improvements

* Build fetal risk classification model
* Predict abnormal fetal conditions using Machine Learning
* Develop healthcare monitoring dashboard in Power BI
* Deploy predictive system using Streamlit / FastAPI
* Add explainable AI for clinical transparency

---

## Author

### Kailash Singh Rawat

MCA (Data Science) Student

Aspiring Data Analyst / Data Scientist

---

## Final Note

I strongly believe:

> Good Machine Learning starts with good Data Understanding.

Because:

Bad Data → Bad Analysis
Bad Analysis → Bad Decisions

EDA is where real Data Analysts create value.

---

⭐ If you found this project valuable, feel free to explore and connect.
