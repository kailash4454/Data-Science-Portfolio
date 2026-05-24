# 🚗 Toyota Corolla Price Prediction using Multiple Linear Regression

# 📌 End-to-End Machine Learning Regression Project

## 📖 Project Overview

This project focuses on predicting **Toyota Corolla car prices** using **Multiple Linear Regression (MLR)** and advanced regularization techniques such as:

- Ridge Regression
- Lasso Regression

The project demonstrates a complete Machine Learning workflow including:

✔ Exploratory Data Analysis (EDA)  
✔ Data Preprocessing  
✔ Feature Engineering  
✔ Multiple Linear Regression Modeling  
✔ Model Evaluation  
✔ Ridge & Lasso Regularization  
✔ Multicollinearity Handling  
✔ Business Interpretation of ML Models

This project simulates a real-world automobile pricing system where businesses estimate vehicle resale prices using historical vehicle data and machine learning techniques.

---

# 🎯 Business Problem

Used car pricing is one of the biggest challenges in the automobile industry.

Car prices depend on multiple factors such as:

- Vehicle Age
- Kilometers Driven
- Fuel Type
- Horsepower
- Engine Capacity
- Weight
- Transmission Type

The objective of this project is to build a Machine Learning model that can accurately predict:

# 💰 Toyota Corolla Resale Prices

using multiple vehicle attributes.

This helps businesses with:

- Used Car Valuation
- Dealership Pricing
- Inventory Management
- Pricing Recommendation Systems
- Customer Negotiation Support

---

# 📊 Dataset Information

The dataset contains Toyota Corolla vehicle details with the following features:

| Feature | Description |
|---|---|
| Age | Age of the car |
| KM | Kilometers driven |
| FuelType | Petrol / Diesel / CNG |
| HP | Horse Power |
| Automatic | Automatic or Manual Transmission |
| CC | Engine Capacity |
| Doors | Number of doors |
| Weight | Vehicle weight |
| Quarterly_Tax | Road tax |
| Price | Target Variable (Car Price) |

---

# 🧠 Machine Learning Workflow

---

# 1️⃣ Exploratory Data Analysis (EDA)

Performed detailed EDA to understand:

- feature distributions
- outliers
- correlations
- categorical variable frequency
- business patterns

## 📈 Visualizations Used

- Histograms
- Boxplots
- Scatter Plots
- Correlation Heatmap
- Bar Charts
- Pie Charts

## 🔍 Key EDA Insights

✔ Older cars generally had lower prices  
✔ Higher kilometers reduced resale value  
✔ Weight and Horsepower positively influenced price  
✔ Fuel type impacted market pricing behavior

---

# 2️⃣ Data Preprocessing

Performed:

✔ Missing Value Handling  
✔ Duplicate Removal  
✔ One-Hot Encoding  
✔ Feature Selection  
✔ Train-Test Split

## 🔄 Encoding Technique

Used:

# One-Hot Encoding

for categorical variables like:

```python
Fuel_Type
```

to prepare the dataset for regression modeling.

---

# 3️⃣ Train-Test Split

The dataset was divided into:

- 80% Training Data
- 20% Testing Data

This helps evaluate model performance on unseen data and prevents overfitting.

---

# 4️⃣ Multiple Linear Regression Models

Built multiple regression models:

## 🔹 Model 1 — Using All Features

## 🔹 Model 2 — Using Selected Important Features

## 🔹 Model 3 — Using Highly Correlated Features

This helped compare:

- prediction accuracy
- feature importance
- model complexity
- business interpretability

---

# 📐 Multiple Linear Regression Formula

```math
Y = β₀ + β₁X₁ + β₂X₂ + ... + βₙXₙ + ε
```

Where:

- **Y** = Car Price
- **X** = Independent Variables
- **β** = Regression Coefficients
- **ε** = Error Term

---

# 5️⃣ Model Evaluation

Models were evaluated using industry-standard regression metrics:

| Metric | Purpose |
|---|---|
| MAE | Average prediction error |
| MSE | Squared prediction error |
| RMSE | Error in original target units |
| R² Score | Model explanatory power |

## 🎯 Evaluation Goal

✔ Lower MAE  
✔ Lower RMSE  
✔ Higher R² Score

indicate better model performance.

---

# 6️⃣ Ridge & Lasso Regression

Applied:

# 🔹 Ridge Regression (L2 Regularization)

and

# 🔹 Lasso Regression (L1 Regularization)

to improve model stability and reduce overfitting.

---

## 📌 Ridge Regression

Ridge Regression helped:

- reduce coefficient magnitude
- stabilize predictions
- handle multicollinearity

without removing features.

---

## 📌 Lasso Regression

Lasso Regression helped:

- perform automatic feature selection
- shrink less important coefficients to zero
- simplify the regression model

This improves model interpretability and deployment efficiency.

---

# 🔥 Key Insights

## ✅ 1. Age and KM strongly reduce resale price

Older cars and heavily driven vehicles generally had lower market value.

---

## ✅ 2. Weight and Horsepower positively impact price

Higher-performance and heavier vehicles showed stronger resale value.

---

## ✅ 3. Fuel Type affects pricing behavior

Fuel efficiency and operating cost influence vehicle demand and pricing.

---

## ✅ 4. Regularization improves model stability

Ridge and Lasso helped reduce overfitting and improved model generalization.

---

## ✅ 5. Simpler models can still perform effectively

Selected-feature models achieved competitive performance while remaining easier to interpret.

---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

---

# 💡 Skills Demonstrated

✔ Multiple Linear Regression  
✔ Exploratory Data Analysis (EDA)  
✔ Data Preprocessing  
✔ Feature Engineering  
✔ Regression Modeling  
✔ Model Evaluation  
✔ Ridge Regression  
✔ Lasso Regression  
✔ Regularization Techniques  
✔ Multicollinearity Handling  
✔ Predictive Analytics  
✔ Business Interpretation of ML Models

---

# 📈 Business Impact

This project demonstrates how Machine Learning can support:

- automobile resale pricing
- dealership inventory valuation
- predictive pricing systems
- pricing optimization
- automotive market intelligence

The project reflects how data-driven decision-making improves pricing accuracy and business efficiency in real-world automotive analytics.

---

# 🚀 Future Improvements

- Hyperparameter Tuning using GridSearchCV
- Cross-Validation for robust evaluation
- Advanced Models (Random Forest, XGBoost)
- Deployment using Flask/FastAPI
- Interactive Dashboard using Power BI or Streamlit

---

# 🎯 Interview Questions Covered

## ❓ What is Normalization & Standardization?

Covered:
- feature scaling
- transformation techniques
- importance in regularization models

---

## ❓ How can multicollinearity be handled?

Covered:
- feature selection
- correlation analysis
- Ridge Regression
- Lasso Regression
- PCA concepts

---

# 👨‍💻 Author

# Kailash Singh Rawat

🎓 MCA (Data Science) Student  
📊 Aspiring Data Analyst / Data Scientist

---

# ⭐ Final Note

I strongly believe:

> Machine Learning is not only about building models.  
> It is about solving business problems using data intelligently.

Because:

Bad Features → Bad Models  
Bad Models → Bad Decisions

Strong analytics begins with understanding data before training algorithms.

---

# ⭐ If you found this project valuable, feel free to explore and connect.