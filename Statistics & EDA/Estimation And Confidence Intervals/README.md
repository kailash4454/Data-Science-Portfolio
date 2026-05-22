# Estimation And Confidence Intervals using Statistical Inference

## Manufacturing Reliability Analysis using Confidence Intervals

## Project Overview

This project focuses on statistical estimation and confidence interval analysis for print-head durability testing in a manufacturing environment.

The project demonstrates how businesses estimate unknown population characteristics using sample data under uncertainty, especially when large-scale testing is expensive or destructive.

Using statistical inference techniques, the project estimates the true average durability of print-heads and compares confidence intervals constructed using both:

* t-Distribution
* z-Distribution

This is a strong real-world Data Analytics and Statistics project involving estimation theory, uncertainty quantification, and manufacturing quality control.

---

# Problem Statement

A manufacturer produces print-heads for personal computers and wants to estimate the average durability of the print-heads before failure.

Durability is measured in:

# Millions of Characters Printed

before the print-head stops working.

Since testing is destructive and expensive, only a small sample of print-heads can be tested.

The objective of this project is to estimate the true population mean durability using:

* sample statistics
* confidence intervals
* statistical inference techniques

This project helps answer:

### What is the estimated average durability of the product?

### How much uncertainty exists in the estimate?

### How does known vs unknown population variability affect estimation?

---

# Dataset Information

The dataset contains durability measurements of:

n = 15

print-heads tested until failure.

Each value represents:

# millions of characters printed before failure

Sample observations include:

```python id="rci1"
1.13, 1.55, 1.43, 0.92, 1.25,
1.36, 1.32, 0.85, 1.07, 1.48,
1.20, 1.33, 1.18, 1.22, 1.29
```

---

# Project Workflow

## 1. Business Understanding

* Understood destructive testing constraints
* Identified need for estimation instead of full population testing
* Applied statistical inference concepts for reliability analysis

---

## 2. Data Preparation

* Organized sample data using Pandas DataFrame
* Calculated sample size
* Prepared data for statistical calculations

---

## 3. Statistical Calculations

Calculated:

* Sample Mean
* Sample Standard Deviation

using professional statistical methods.

Sample mean formula:

xˉ = ∑x / n

Sample standard deviation formula:

s = sqrt(square(xi - xˉ) / (n -1))

---

## 4. Confidence Interval using t-Distribution

Constructed:

# 99% Confidence Interval

using:

* sample standard deviation
* small sample inference
* t-distribution

Confidence interval formula:

xˉ ± tα/2 (s / sqrt(n))

This approach was used because:

* sample size was small
* population standard deviation was unknown

---

## 5. Confidence Interval using z-Distribution

Constructed:

# 99% Confidence Interval

using:

* known population standard deviation
* z-distribution

Confidence interval formula:

xˉ ± zα/2 (σ / sqrt(n))

This helped compare estimation precision under different uncertainty assumptions.

---

## 6. Comparative Analysis

Compared:

* t-interval width
* z-interval width
* critical values
* uncertainty levels

to understand how estimation reliability changes when population variability is known vs unknown.

---

# Key Insights

## t-Confidence Interval was wider than z-Confidence Interval

This occurred because estimating population variability from a small sample introduces additional uncertainty.

The t-distribution accounts for this uncertainty using:

* larger critical values
* heavier tails
* wider intervals

---

## Known population standard deviation reduces uncertainty

When the population standard deviation was known:

σ = 0.2

the resulting z-confidence interval became narrower and more precise.

---

## Confidence intervals provide better business insight than single-point estimates

Instead of relying only on the sample mean, confidence intervals help businesses understand:

* reliability range
* estimation uncertainty
* manufacturing consistency
* operational risk

---

# Technologies Used

* Python
* NumPy
* Pandas
* SciPy
* Jupyter Notebook

---

# Skills Demonstrated

* Statistical Inference
* Confidence Interval Estimation
* t-Distribution vs z-Distribution
* Margin of Error Analysis
* Sample Statistics
* Manufacturing Quality Analytics
* Reliability Estimation
* Uncertainty Quantification
* Analyst-Level Statistical Thinking

---

# Business / Manufacturing Impact

This project helps support:

* product reliability estimation
* manufacturing quality control
* warranty planning
* production consistency analysis
* operational risk management
* evidence-based manufacturing decisions

It demonstrates how statistical estimation helps businesses make reliable decisions even when only limited sample data is available.

---

# Future Improvements

* Build predictive product reliability models
* Apply Bayesian estimation techniques
* Perform hypothesis testing for manufacturing consistency
* Develop manufacturing quality dashboards using Power BI
* Integrate automated statistical quality control systems

---

# Author

## Kailash Singh Rawat

MCA (Data Science) Student

Aspiring Data Analyst / Data Scientist

---

# Final Note

I strongly believe:

> Strong Data Analysts do not only calculate numbers.
> They quantify uncertainty and help businesses make reliable decisions.

Because:

Bad Estimation → Bad Decisions

Bad Decisions → Business Risk

Statistical inference is where real analytical thinking begins.

---

⭐ If you found this project valuable, feel free to explore and connect.
