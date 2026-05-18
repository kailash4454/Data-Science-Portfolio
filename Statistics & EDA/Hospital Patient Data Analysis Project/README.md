# Hospital Patient Data Analysis Project

## Data Cleaning, Billing Analytics, and Hospital Revenue Insights

## Project Overview

This project focuses on performing complete data cleaning, preprocessing, and billing analytics on hospital patient data to improve revenue analysis, doctor performance evaluation, and healthcare decision-making.

The project demonstrates how raw hospital operational data can be transformed into a business-ready dataset using professional Pandas operations such as missing value handling, duplicate removal, groupby aggregation, merge, and concatenation.

This is a strong real-world Data Analytics project involving healthcare analytics, billing optimization, and operational intelligence.

---

## Problem Statement

The objective of this project is to analyze hospital patient and billing datasets and identify:

* department-wise revenue
* billing efficiency
* duplicate patient records
* missing billing values
* doctor performance insights
* healthcare decision-support analytics

using data preprocessing and business-focused analysis techniques.

This project helps answer:

### Which department generates the highest hospital revenue?

### How do missing billing values affect financial reporting?

### How can clean patient data improve hospital decision-making?

---

## Dataset Information

The project uses two datasets:

### 1. Patient Dataset

Contains important patient-related fields such as:

* PatientID
* Department
* Doctor
* BillAmount
* ReceptionistID
* CheckInTime

---

### 2. Billing Dataset

Contains additional billing and financial details such as:

* Payment Mode
* Insurance Information
* Final Billing Details

These datasets help create a complete hospital financial analytics system.

---

## Project Workflow

### 1. Data Loading and Initial Understanding

* Loaded datasets using Pandas
* Checked dataset shape, columns, and structure
* Used `.info()` and `.head()` for initial understanding

---

### 2. Feature Selection

Selected billing-relevant columns such as:

* PatientID
* Department
* Doctor
* BillAmount

This improved analytical focus and reduced unnecessary complexity.

---

### 3. Data Cleaning and Preparation

* Removed unnecessary administrative columns
* Checked data types and consistency
* Prepared datasets for reliable analytics

---

### 4. Duplicate Record Removal

Removed duplicate patient records using:

# PatientID

as the unique identifier

This improved:

* accurate billing
* patient-level reporting
* revenue reliability

---

### 5. Missing Value Handling

Filled missing:

# BillAmount

values using mean imputation

Mean = sum(x) / n

This preserved dataset quality while maintaining billing consistency.

---

### 6. GroupBy Revenue Analysis

Used:

# groupby()

to calculate:

### Total Bill Amount Per Department

This helped identify:

* top-performing departments
* low-performing units
* hospital revenue concentration

---

### 7. Dataset Merging

Merged:

### Patient Dataset + Billing Dataset

using:

# PatientID

This created a stronger relational dataset for financial reporting and analytics.

---

### 8. Row-wise Concatenation

Added:

### New Weekly Patients

using:

# pd.concat(axis=0)

This simulated real-world live hospital updates.

---

### 9. Column-wise Concatenation

Added new billing columns such as:

* InsuranceCovered
* FinalAmount

using:

# pd.concat(axis=1)

This improved billing intelligence and settlement tracking.

---

## Key Insights

### Accurate billing analytics depends heavily on duplicate removal

Repeated patient records can create incorrect revenue calculations and misleading department performance reports.

---

### Missing BillAmount values directly affect hospital financial decisions

Proper imputation improves reporting quality and prevents unreliable business conclusions.

---

### Department-wise revenue analysis helps identify business priorities

High-performing departments can be optimized further, while low-performing units may require operational improvement.

---

### Merging datasets creates stronger business intelligence

Patient + Billing integration improves doctor performance analysis, insurance tracking, and final settlement reporting.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Jupyter Notebook

---

## Skills Demonstrated

* Data Cleaning
* Missing Value Handling
* Duplicate Resolution
* Feature Selection
* GroupBy Aggregation
* Merge and Concatenation
* Billing Analytics
* Healthcare Data Analysis
* Business Intelligence
* Analyst-Level Decision Thinking

---

## Business / Healthcare Impact

This project helps support:

* hospital billing optimization
* department revenue analysis
* doctor performance evaluation
* insurance claim analysis
* patient settlement tracking
* healthcare dashboard reporting

It shows how strong preprocessing improves both healthcare operations and business intelligence.

---

## Future Improvements

* Build hospital revenue forecasting model
* Create patient risk scoring system
* Develop healthcare dashboard using Power BI
* Add doctor performance ranking system
* Deploy hospital billing analytics app using Streamlit

---

## Author

### Kailash Singh Rawat

MCA (Data Science) Student

Aspiring Data Analyst / Data Scientist

---

## Final Note

I strongly believe:

> Clean data is more powerful than complex models.

Because:

Bad Data → Bad Reports

Bad Reports → Bad Decisions

Data preprocessing is where real Data Analysts create value.

---

⭐ If you found this project valuable, feel free to explore and connect.
