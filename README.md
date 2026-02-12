# 🚚 Food Delivery Time Prediction App

A Machine Learning project to predict food delivery time based on order characteristics and operational conditions.  
This project is built using **Python, Scikit-Learn, and Streamlit**.

---

## 📌 Project Overview

In the competitive food delivery industry, accurate delivery time estimation is crucial for improving customer satisfaction and operational efficiency.

This project develops a regression model to predict delivery time (in minutes) using historical delivery data and operational features such as:

- Delivery distance
- Preparation time
- Courier experience
- Weather condition
- Traffic level
- Time of day
- Vehicle type

The final solution is deployed as an interactive Streamlit web application.

---

## ❗ Problem Statement

Companies often struggle with:
- Inaccurate delivery time estimation
- Customer dissatisfaction due to delays
- Lack of data-driven prediction systems

Without predictive analytics, operations may become inefficient and unreliable.

---

## 🎯 Project Objective

- Build a Machine Learning regression model to predict delivery time.
- Identify key factors affecting delivery duration.
- Evaluate model performance using appropriate regression metrics.
- Deploy an interactive prediction app using Streamlit.

---

## 📊 Dataset

- Source: Kaggle – Food Delivery Time Prediction
- Total Records: ~1000+
- Features:
  - Distance_km
  - Preparation_Time_min
  - Courier_Experience_yrs
  - Weather
  - Traffic_Level
  - Time_of_Day
  - Vehicle_Type
  - Delivery_Time_min (Target)

---

## 🔎 Exploratory Data Analysis (EDA)

Key Insights:

- Delivery time distribution is right-skewed.
- Distance and preparation time show strong positive correlation with delivery time.
- High traffic significantly increases delivery duration.
- Vehicle type influences delivery efficiency.

Visualizations included:
- Histogram distribution
- Boxplot (outlier detection)
- Scatter plots
- Categorical bar charts

---

## 🤖 Machine Learning Process

### 1️⃣ Data Preprocessing
- Handling missing values
- Scaling numerical features
- One-hot encoding categorical features
- Pipeline implementation using `ColumnTransformer`

### 2️⃣ Models Compared
- Linear Regression
- Ridge Regression
- Decision Tree Regressor

### 3️⃣ Best Model
✅ **Linear Regression + Scaling**

Selected due to:
- Stable performance
- Low error
- High interpretability
- Generalization capability

---

## 📈 Evaluation Metrics

- **MAE (Mean Absolute Error)**  
  Measures average absolute prediction error.

- **RMSE (Root Mean Squared Error)**  
  Penalizes large errors more heavily.

- **MAPE (Mean Absolute Percentage Error)**  
  Measures percentage error relative to actual values.

---

## 🖥️ Streamlit App Features

- 🏠 Project Overview Page
- 📊 Exploratory Data Analysis Page
- 🤖 Prediction Simulation Page
- 📬 Contact Page (Google Form integration)

---

