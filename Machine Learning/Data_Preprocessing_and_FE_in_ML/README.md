# Adult Income Dataset — Data Preprocessing & Feature Engineering

> **End-to-end data preprocessing and feature engineering workflow for transforming the Adult Income dataset into a machine-learning-ready dataset.**

---

## 📌 Project Overview

This project focuses on the **systematic preprocessing, transformation, analysis, and feature engineering** of the Adult Income dataset.

The objective is to transform raw demographic, educational, occupational, and financial data into a clean and structured dataset suitable for downstream **machine-learning classification tasks**.

Rather than treating preprocessing as simple data cleaning, this project demonstrates a complete data preparation workflow covering:

- Missing-value handling
- Exploratory data analysis
- Numerical feature analysis
- Feature scaling
- Categorical feature analysis
- One-Hot Encoding
- Ordinal feature representation
- Feature engineering
- Skewness transformation
- Anomaly detection using Isolation Forest
- Predictive Power Score (PPS) analysis
- Final ML dataset validation

The project emphasizes **data quality, feature representation, interpretability, and ML readiness**.

---

## 🎯 Business / Analytical Objective

The Adult Income dataset contains information about individuals including:

- Age
- Work class
- Education
- Occupation
- Relationship
- Marital status
- Race
- Gender
- Working hours
- Capital gain/loss
- Other demographic and financial attributes

The target variable is:

**`income`**

with two income categories:

- `<=50K`
- `>50K`

The analytical objective is to prepare these raw observations for a potential **binary classification problem** that predicts an individual's income category.

> **Note:** This project primarily focuses on data preprocessing and feature engineering rather than final predictive model development.

---

## 🔎 Project Objectives

### Data Quality
- Identify and handle missing values represented by `?`
- Check duplicate records
- Validate data types
- Verify final dataset integrity

### Numerical Data Processing
- Analyze numerical distributions
- Identify skewed variables
- Apply appropriate transformations
- Compare original and transformed distributions
- Standardize numerical features
- Apply Min-Max scaling

### Categorical Data Processing
- Identify categorical variables
- Analyze category cardinality
- Apply One-Hot Encoding
- Understand Label Encoding limitations
- Identify ordinal relationships

### Feature Engineering
Create meaningful domain-driven features such as:

- `work_hours_category`
- `net_capital`

### Advanced Data Analysis
- Detect potentially anomalous observations using Isolation Forest
- Evaluate feature predictive relationships using Predictive Power Score

### Final Validation
Ensure that the resulting dataset:

- Contains no unresolved missing values
- Contains no unintended duplicates
- Contains no unprocessed categorical variables
- Has a properly encoded target
- Is suitable for downstream ML workflows

---

# 🛠️ Tech Stack

| Category | Tools / Libraries |
|---|---|
| Language | Python |
| Data Manipulation | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Preprocessing | Scikit-learn |
| Scaling | StandardScaler, MinMaxScaler |
| Encoding | One-Hot Encoding, Label Encoding, Ordinal Mapping |
| Imputation | SimpleImputer |
| Anomaly Detection | Isolation Forest |
| Predictive Analysis | Predictive Power Score (PPS) |
| Development | Jupyter Notebook |

---

# 📂 Project Structure

```text
Adult-Income-Preprocessing/
│
├── adult.csv
│
├── Adult_Income_Preprocessing.ipynb
│
├── adult_income_ml_ready.csv
│
├── README.md
│
└── requirements.txt
```

> File names can be adjusted to match the actual names in your repository.

---

# 🔄 Data Science Workflow

```text
Raw Dataset
     │
     ▼
Data Loading & Exploration
     │
     ▼
Data Quality Assessment
     │
     ▼
Missing Value Handling
     │
     ▼
Numerical Feature Analysis
     │
     ├───────────────┐
     ▼               ▼
Skewness         Outlier Analysis
Transformation
     │
     ▼
Feature Scaling
     │
     ├───────────────┐
     ▼               ▼
StandardScaler    MinMaxScaler
     │               │
     └───────┬───────┘
             ▼
Categorical Feature Analysis
             │
             ▼
Categorical Encoding
             │
             ▼
Ordinal Feature Handling
             │
             ▼
Feature Engineering
             │
      ┌──────┴──────┐
      ▼             ▼
Isolation       PPS Analysis
Forest
      │             │
      └──────┬──────┘
             ▼
Final Dataset Validation
             │
             ▼
ML-Ready Dataset
```

---

# 🧹 1. Missing Value Handling

The dataset uses `?` as a representation of missing information.

The preprocessing workflow identifies these values and converts them into proper missing-value representations.

Example:

```python
df = df.replace('?', np.nan)
```

Numerical variables are handled using **median-based imputation**, while categorical variables are handled using the **most frequent value**.

### Why?

Median imputation is less sensitive to extreme values than mean imputation, while mode-based imputation preserves the most frequently observed categorical value.

---

# 📊 2. Numerical Feature Analysis

Numerical variables were analyzed using:

- Descriptive statistics
- Distribution analysis
- Histograms
- Boxplots
- Skewness
- IQR-based outlier analysis

This analysis helped identify variables requiring additional transformation or investigation.

---

# 📈 3. Skewness Transformation

The `capital-gain` feature was identified as strongly right-skewed.

A logarithmic transformation was applied:

```python
df['capital-gain_log'] = np.log1p(df['capital-gain'])
```

### Why `log1p()`?

`log1p(x)` calculates:

```text
log(1 + x)
```

and is particularly useful when the feature contains zero values.

The transformation reduces the influence of extremely large values and produces a more compact representation of the feature.

---

# ⚖️ 4. Feature Scaling

Two scaling approaches were explored.

## StandardScaler

Standardization transforms numerical features so that they are approximately centered around:

```text
Mean ≈ 0
Standard Deviation ≈ 1
```

Example:

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

df_standard_scaled[numerical_columns] = scaler.fit_transform(
    df[numerical_columns]
)
```

---

## MinMaxScaler

Min-Max scaling transforms numerical values to a bounded range, generally:

```text
0 → 1
```

Example:

```python
from sklearn.preprocessing import MinMaxScaler

minmax_scaler = MinMaxScaler()

df_minmax_scaled[numerical_columns] = (
    minmax_scaler.fit_transform(
        df[numerical_columns]
    )
)
```

### Comparison

| Characteristic | StandardScaler | MinMaxScaler |
|---|---|---|
| Typical output | Centered around 0 | 0 to 1 |
| Uses mean/std | Yes | No |
| Bounded range | No | Yes |
| Outlier sensitivity | Sensitive | Highly sensitive |
| Main purpose | Standardization | Range normalization |

---

# 🏷️ 5. Categorical Feature Analysis

Categorical variables were analyzed based on:

- Number of unique categories
- Frequency distribution
- Category percentages
- Cardinality

This analysis was used to determine appropriate encoding strategies.

---

# 🔢 6. Categorical Encoding

## One-Hot Encoding

One-Hot Encoding was used to represent categorical variables as binary features.

Example:

```python
X_encoded = pd.get_dummies(
    X,
    columns=categorical_features,
    drop_first=False,
    dtype=int
)
```

A categorical variable such as:

```text
sex
```

can become:

```text
sex_Female
sex_Male
```

This avoids imposing an artificial numerical ordering on nominal categories.

---

## Label Encoding

Label Encoding was also explored to demonstrate compact numerical representation of categorical values.

However, numerical labels can unintentionally imply an ordering between categories.

Therefore:

> **Encoding strategy should be determined by the nature of the variable, not simply by the number of categories.**

For nominal variables, One-Hot Encoding is generally more interpretable.

---

# 🎓 7. Ordinal Feature Representation

The `education` variable contains an inherent educational progression.

An explicit ordinal mapping was demonstrated to represent this ordering.

However, the dataset already contains:

```text
education-num
```

which provides an ordered numerical representation.

Therefore, the additional demonstration feature:

```text
education_ordinal
```

was removed to avoid redundant information.

This demonstrates an important feature-engineering principle:

> **Do not retain multiple representations of the same underlying information without a clear modeling purpose.**

---

# 🧠 8. Feature Engineering

Two meaningful domain-driven features were created.

## `work_hours_category`

The continuous:

```text
hours-per-week
```

feature was converted into interpretable groups:

```text
< 30   → Part-Time
30–39  → Near Full-Time
40     → Full-Time
> 40   → Overtime
```

Example:

```python
def categorize_work_hours(hours):
    if hours < 30:
        return 'Part-Time'
    elif hours < 40:
        return 'Near Full-Time'
    elif hours == 40:
        return 'Full-Time'
    else:
        return 'Overtime'

df['work_hours_category'] = (
    df['hours-per-week']
    .apply(categorize_work_hours)
)
```

This converts a continuous variable into an interpretable employment-intensity feature.

---

## `net_capital`

A financial feature was created:

```python
df['net_capital'] = (
    df['capital-gain'] -
    df['capital-loss']
)
```

This combines capital gain and capital loss into a single measure of net capital activity.

---

# 🚨 9. Anomaly Detection — Isolation Forest

Isolation Forest was used to identify potentially unusual observations.

```python
from sklearn.ensemble import IsolationForest

iso_forest = IsolationForest(
    n_estimators=200,
    contamination=0.05,
    random_state=42
)

df['anomaly_prediction'] = (
    iso_forest.fit_predict(X_anomaly)
)
```

The algorithm produces:

```text
 1 → Normal observation
-1 → Potential anomaly
```

### Important Analytical Decision

Potential anomalies were **not automatically deleted**.

An unusual observation may still represent a valid real-world record.

Therefore, the workflow follows:

```text
Detect
  ↓
Flag
  ↓
Investigate
  ↓
Decide
```

rather than:

```text
Detect → Delete
```

---

# 🎯 10. Predictive Power Score

Predictive Power Score (PPS) was used to investigate the predictive relationship between features and the `income` target.

```python
import ppscore as pps

pps_matrix = pps.matrix(df)

income_pps = (
    pps_matrix[
        pps_matrix['y'] == 'income'
    ][['x', 'y', 'ppscore']]
    .sort_values(
        'ppscore',
        ascending=False
    )
)
```

PPS provides a directional predictive measure and can capture relationships that may not be represented by simple linear correlation.

### Important

A high PPS score does not automatically mean that a feature should be included in a final ML model.

Feature selection should also consider:

- Data leakage
- Redundant information
- Model performance
- Domain relevance
- Interpretability
- Train/test separation

---

# ✅ 11. Final ML Dataset Validation

The final dataset was validated using multiple quality checks.

```python
print("Shape:", df_ml.shape)

print(
    "Missing values:",
    df_ml.isnull().sum().sum()
)

print(
    "Duplicate rows:",
    df_ml.duplicated().sum()
)

print(
    "Non-numeric columns:",
    len(
        df_ml.select_dtypes(
            exclude=np.number
        ).columns
    )
)
```

Final validation ensures:

```text
Missing Values       → 0
Duplicate Rows       → 0
Non-Numeric Columns  → 0
Target Missing       → 0
```

---

# 📊 Key Analytical Findings

### Missing Data
Missing-value indicators represented by `?` were identified and handled through appropriate preprocessing techniques.

### Numerical Variables
Numerical features were examined through descriptive statistics, distributions, skewness and outlier analysis.

### Skewness
`capital-gain` was identified as a highly right-skewed feature and transformed using `log1p()`.

### Scaling
StandardScaler and MinMaxScaler were implemented and compared to understand their effects on numerical feature ranges.

### Categorical Variables
Categorical variables were analyzed based on their cardinality and nature before selecting appropriate encoding strategies.

### Feature Engineering
`work_hours_category` and `net_capital` were created as interpretable, domain-driven features.

### Anomaly Detection
Isolation Forest was applied to identify potentially unusual observations without automatically treating them as invalid records.

### Predictive Power
PPS analysis was performed to investigate feature-level predictive relationships with the income target.

### Final Data Quality
The resulting dataset was validated for missing values, duplicates, target completeness and numerical compatibility.

---

# 💡 Key Data Science Concepts Demonstrated

This project demonstrates practical understanding of:

- Data cleaning
- Missing-value treatment
- Exploratory Data Analysis
- Statistical distributions
- Skewness
- Log transformations
- Feature scaling
- One-Hot Encoding
- Label Encoding
- Ordinal Encoding
- Feature engineering
- Cardinality analysis
- Anomaly detection
- Predictive Power Score
- Feature selection considerations
- Data leakage awareness
- ML dataset validation

---

# ⚠️ Production ML Considerations

The notebook focuses on preprocessing and analytical understanding.

For a production machine-learning pipeline, preprocessing operations that **learn parameters from data** should be fitted only on the training data.

For example:

```python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

scaler.fit(X_train)

X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

This prevents information from the test set from influencing preprocessing.

The same principle should be considered for:

- Imputation
- Scaling
- Feature selection
- Encoding strategies
- Other learned transformations

---

# 🚀 Potential Next Steps

The processed dataset can be extended into a complete machine-learning project.

Potential next steps include:

1. Train/test split
2. Class imbalance analysis
3. Baseline classification model
4. Logistic Regression
5. Decision Tree
6. Random Forest
7. Gradient Boosting
8. Hyperparameter tuning
9. Cross-validation
10. Precision, Recall and F1-score evaluation
11. ROC-AUC analysis
12. Confusion matrix
13. Feature importance
14. SHAP-based explainability
15. Model deployment

This creates a natural progression from:

```text
Data Preparation
       ↓
Feature Engineering
       ↓
Machine Learning
       ↓
Model Evaluation
       ↓
Explainability
       ↓
Deployment
```

---

# 📁 Dataset Output

The processed machine-learning-ready dataset can be saved using:

```python
df_ml.to_csv(
    'adult_income_ml_ready.csv',
    index=False
)
```

---

# 🧪 Reproducibility

The project uses fixed random seeds where applicable:

```python
random_state=42
```

This helps ensure that stochastic operations produce reproducible results.

The notebook is structured sequentially so that the preprocessing workflow can be reproduced from dataset loading through final validation.

---

# 👨‍💻 Skills Demonstrated

### Programming
- Python
- Pandas
- NumPy

### Data Analysis
- Exploratory Data Analysis
- Descriptive Statistics
- Distribution Analysis
- Skewness Analysis
- Outlier Analysis

### Data Preprocessing
- Missing Value Handling
- Feature Scaling
- One-Hot Encoding
- Label Encoding
- Ordinal Encoding
- Feature Transformation

### Advanced Analytics
- Isolation Forest
- Predictive Power Score
- Feature Selection Concepts

### Data Science Practices
- Feature Engineering
- Data Leakage Awareness
- Reproducible Analysis
- Data Quality Validation
- ML-ready Dataset Preparation

---

# 📌 Project Highlights

- **End-to-end preprocessing workflow**
- **Multiple numerical scaling techniques compared**
- **Categorical encoding strategies evaluated**
- **Domain-driven feature engineering**
- **Skewness transformation using logarithmic transformation**
- **Unsupervised anomaly detection**
- **Predictive Power Score analysis**
- **Final ML-ready dataset validation**
- **Production-oriented data leakage considerations**

---

# ⭐ Project Value

This project demonstrates that effective machine learning begins **before model training**.

The primary focus is on building a reliable foundation where:

```text
Better Data
   +
Better Features
   +
Better Representation
   +
Better Validation
   =
Better ML Pipeline
```

The project therefore serves as a practical demonstration of **data preprocessing, feature engineering, and analytical reasoning required in real-world Data Science workflows**.

---

## 📬 Connect

If you are interested in discussing this project, data science, machine learning, analytics, or collaboration opportunities, feel free to connect with me.

**GitHub:** `https://github.com/kailash4454`

**Portfolio:** `https://github.com/kailash4454/Data-Science-Portfolio`

---

## 📜 License

This project is intended for educational and portfolio purposes.