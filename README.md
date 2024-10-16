# Salary Prediction App
The Salary Prediction App is a web application designed to estimate employee salaries based on their years of experience and job performance rating. Built using Streamlit, this app provides an intuitive interface for users to input data and receive instant salary predictions.


  ![project ss1](https://github.com/user-attachments/assets/aabee711-e07c-44b9-b16d-3b8be615fbfc)


# Features

**User-Friendly Interface:**    Easy-to-use input fields for entering years at the company and job performance rating.

**Real-Time Predictions:**    Instant salary estimation using a pre-trained linear regression model.

**ractive Elements:**    Includes visual feedback (balloons) upon successful prediction.


# How to Use
1.  Enter the number of years the employee has been with the company.

2. Provide a job performance rating (on a scale).

3. Click the "Press the button for salary prediction" button to receive an estimated salary.

# Requirements

Python

Streamlit

NumPy

joblib

Scikit-learn

Pandas


# Salary Prediction Model Analysis
The Salary Prediction App employs a linear regression model to predict employee salaries based on specific features. This section details the analysis process, including data handling, model training, and evaluation.

# Libraries Used
**Pandas:** For data manipulation and analysis.
**NumPy:** For numerical operations and handling arrays.
**Matplotlib:** For data visualization and plotting (if used).
**Scikit-Learn:** For machine learning tasks, including model training and evaluation.
**Joblib:** For saving and loading the trained model.

# Analysis Steps
**Data Preparation:**
Import necessary libraries and load the dataset using Pandas for analysis and preparation.

**Feature Selection:**
Identify relevant features for predicting salaries, such as:

    Years of experience
    Job performance ratings
    
**Data Splitting:**
Use train_test_split from Scikit-Learn to split the dataset into training and testing sets. This step ensures the model's effectiveness and helps avoid overfitting.

**Model Training:**
Train a Linear Regression model using the training dataset to establish relationships between the features and target salary values.

**Model Evaluation:**
Evaluate the model's performance using metrics such as Mean Absolute Error (MAE) to assess prediction accuracy.

**Model Saving:**
Save the trained model using Joblib for later use in the Salary Prediction App.

![project ss2](https://github.com/user-attachments/assets/bd7efb4c-1990-4ec3-89e1-a8097b1621c2)
![project ss3](https://github.com/user-attachments/assets/7fbfccf2-711b-4e0d-b7c4-9941e66095c5)
