# Wine Quality Analysis

## Overview

This project analyses the physicochemical properties of wine to understand the key factors influencing quality. It combines exploratory data analysis (EDA) with a basic machine learning model to evaluate how well wine quality can be predicted from chemical attributes.

---

## Objective

* Identify relationships between chemical properties and wine quality
* Perform exploratory data analysis to uncover patterns and correlations
* Build a simple classification model to assess predictability of wine quality
* Translate findings into practical, business-relevant insights

---

## Tools & Technologies

* Python
* pandas (data manipulation)
* matplotlib & seaborn (data visualisation)
* scikit-learn (machine learning)

---

## Dataset

The dataset contains physicochemical properties of wine samples, including:

* Alcohol
* Volatile acidity
* Citric acid
* Residual sugar
* Chlorides
* Sulphates
* pH
* Density
* Quality (target variable)

Note: The dataset was cleaned by removing non-relevant columns and handling missing values.

---

## Exploratory Data Analysis

### Correlation Analysis

A correlation heatmap was used to identify relationships between features.

**Key observations:**

* Alcohol shows a positive correlation with quality
* Volatile acidity shows a negative correlation with quality
* Several features exhibit interdependence, indicating complex interactions

---

### Quality Distribution

* Most wines fall within mid-range quality scores
* High-quality wines are relatively rare

---

### Feature Relationships

* Higher alcohol content tends to be associated with better quality
* Increased volatile acidity is linked to lower quality

---

## Machine Learning Model

A Random Forest Classifier was used to evaluate how well wine quality can be predicted.

### Steps:

* Feature selection (all variables except target)
* Train-test split
* Model training using Random Forest
* Model evaluation using accuracy

### Outcome:

The model demonstrates that wine quality is reasonably predictable using chemical features, indicating strong underlying relationships in the data.

---

## Key Insights

* Alcohol content is one of the strongest positive indicators of wine quality
* Volatile acidity negatively impacts quality
* Wine quality is influenced by a combination of multiple chemical factors rather than a single variable
* The dataset shows a natural imbalance with fewer high-quality samples

---

## Business Interpretation

* Wine producers can improve quality by optimising alcohol levels and controlling acidity
* Data-driven quality prediction can support:

  * Pricing strategies
  * Product classification
  * Quality control processes
* Predictive modelling can be integrated into production pipelines for consistency

---

## Skills Demonstrated

* Exploratory Data Analysis (EDA)
* Data Cleaning & Preprocessing
* Correlation & Statistical Analysis
* Data Visualisation
* Machine Learning (Classification)
* Translating technical analysis into business insights

---

## Project Structure

```
wine-quality-analysis/
│
├── wine_analysis.py
├── winequality.csv
├── README.md
├── insights.txt
```

---

## Conclusion

This project demonstrates how data analysis and machine learning can be applied to understand product quality and support data-driven decision-making in production and quality control environments.
