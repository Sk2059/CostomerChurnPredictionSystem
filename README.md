Customer Churn Prediction using Machine Learning 📊

A complete end-to-end Machine Learning project focused on predicting telecom customer churn using multiple classification algorithms, advanced preprocessing techniques, feature engineering, hyperparameter tuning, and deployment with Streamlit.

This project demonstrates a full professional ML workflow from raw data preprocessing to deployment-ready prediction systems.

🚀 Project Overview

Customer churn prediction helps businesses identify customers who are likely to leave a service. In this project, different machine learning algorithms were trained and evaluated to predict customer churn behavior.

The project includes:

Data Cleaning
Missing Value Handling
Feature Engineering
Feature Encoding
Feature Scaling
Feature Selection
Model Training
Hyperparameter Tuning
Model Evaluation
Streamlit Deployment
🎯 Objectives
Predict whether a customer will churn or not
Compare multiple ML algorithms
Optimize model performance
Build a production-ready ML pipeline
Deploy an interactive prediction app
🧠 Machine Learning Workflow
📌 Phase 1 — Project Setup
Customer-Churn-Prediction/
│
├── app/
│   └── app.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   └── churn_prediction.ipynb
│
├── src/
│   ├── model.pkl
│   ├── scaler.pkl
│   └── columns.pkl
│
├── requirements.txt
├── README.md
└── .gitignore
📊 Dataset Features

The dataset contains telecom customer information such as:

Gender
Senior Citizen
Partner
Dependents
Contract Type
Internet Service
Monthly Charges
Total Charges
Tenure
Payment Method
Online Security
Tech Support
Streaming Services
Churn Status
🔥 Complete ML Pipeline
✅ 1. Data Collection
Telecom customer churn dataset
Structured business dataset
✅ 2. Data Understanding

Performed:

shape analysis
datatype inspection
statistical summary
target distribution analysis
✅ 3. Data Cleaning

Handled:

inconsistent values
incorrect datatypes
unwanted columns
✅ 4. Missing Value Handling

Techniques used:

median imputation
mode imputation
categorical handling
✅ 5. Duplicate Handling
removed duplicate records
validated dataset integrity
✅ 6. Data Transformation

Performed:

datatype conversion
categorical normalization
feature restructuring
✅ 7. Exploratory Data Analysis (EDA)

Visualizations used:

countplots
histograms
heatmaps
boxplots
correlation matrix
churn distribution analysis
✅ 8. Outlier Treatment

Handled using:

IQR method
distribution analysis
✅ 9. Feature Engineering

Created meaningful features using:

customer behavior patterns
service combinations
tenure insights
✅ 10. Feature Encoding

Applied:

One Hot Encoding
categorical transformation
✅ 11. Feature Scaling

Used:

StandardScaler

to normalize numerical features.

✅ 12. Feature Selection

Methods used:

correlation analysis
feature importance
model-based selection
✅ 13. Train-Test Split

Dataset split into:

training set
testing set

for proper model evaluation.

🤖 Models Trained

The following algorithms were trained and compared:

Model	Accuracy
Logistic Regression	81.83% ✅
Gradient Boosting	81.41%
Random Forest	81.12%
XGBoost	81.05%
Decision Tree	79.49%
🏆 Best Model
✅ Logistic Regression

Why?

Best overall accuracy
Better generalization
Balanced precision and recall
Less overfitting
Simpler and interpretable model
⚡ Hyperparameter Tuning

Performed using:

GridSearchCV

Optimized:

regularization
solver selection
model parameters
cross-validation performance
📈 Evaluation Metrics

Models were evaluated using:

Accuracy
Precision
Recall
F1-Score
Confusion Matrix
ROC Curve
AUC Score
📉 Visualizations Included
Confusion Matrix
Feature Importance
ROC Curve
Correlation Heatmap
Distribution Analysis
Model Comparison Charts
🌐 Streamlit Deployment

An interactive Streamlit app was developed for real-time churn prediction.

Features include:

✅ Customer input form
✅ Churn prediction
✅ Churn probability score
✅ Business insights
✅ Professional UI

🛠️ Tech Stack
Languages & Libraries
Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
XGBoost
Streamlit
Joblib
▶️ Installation

Clone repository:

git clone https://github.com/Sk2059/Customer-Churn-Prediction.git

Move into project:

cd Customer-Churn-Prediction

Install dependencies:

pip install -r requirements.txt
▶️ Run Streamlit App
streamlit run app/app.py
📌 Future Improvements
Deep Learning implementation
Advanced feature engineering
SHAP explainability
Docker deployment
CI/CD integration
Cloud deployment
Real-time API integration
💡 Key Learnings

Through this project, the following skills were developed:

✅ Data preprocessing
✅ Feature engineering
✅ Classification algorithms
✅ Hyperparameter tuning
✅ Model evaluation
✅ Explainable AI
✅ Streamlit deployment
✅ End-to-end ML workflow

🚀 Project Status

✅ Completed
✅ Deployment Ready
✅ Portfolio Ready
✅ Interview Ready

👨‍💻 Author
Sk Singh

Aspiring Machine Learning Engineer focused on:

Machine Learning
Data Science
Backend Development
AI Applications
Real-world ML Projects

GitHub:

Sk2059 GitHub Profile
⭐ If you like this project

Give this repository a ⭐ on GitHub and connect for more ML projects and AI applications.