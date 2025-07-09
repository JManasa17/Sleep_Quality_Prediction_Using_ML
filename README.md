
Sleep Quality Prediction
========================

A machine learning-powered web application to help users monitor and improve their sleep quality based on daily lifestyle factors.

Overview
--------

Sleep Quality Prediction is a personalized health-tech solution designed to provide insights into how factors such as stress levels, caffeine intake, physical activity, and environmental conditions affect a person’s sleep quality. The system analyzes user-provided data and generates meaningful predictions and tailored recommendations using a trained machine learning model.

Problem Statement
-----------------

Modern lifestyles have disrupted natural sleep cycles, contributing to sleep deprivation and health problems such as anxiety, obesity, and cardiovascular issues. Most individuals lack tools to assess or understand how their habits impact their sleep. This project bridges that gap by using a data-driven approach to:

- Predict sleep quality (Good, Average, Bad)
- Provide suggestion/comment
- Increase awareness of lifestyle impacts

Machine Learning Model
----------------------

- Algorithm: Random Forest Regressor
- Input Features:
  - Sleep Duration
  - Caffeine Intake (cups)
  - Stress Level (1–10)
  - Physical Activity (steps)
  - Mood (1–10)
  - Environmental Temperature (°C)
- Output: Predicted Sleep Quality Score (1–10), Category & Suggestion

Tech Stack
----------

Layer         | Technology
------------- | ---------------------------
Frontend      | HTML, CSS, JavaScript
Backend       | Python, Flask
ML Libraries  | scikit-learn, pandas, joblib
Deployment    | Localhost / Cloud-ready

Project Structure
-----------------
<pre>
sleep-quality-prediction/
├── app.py                  # Flask backend for prediction
├── training.py             # Model training script
├── best_rf_model.pkl       # Trained ML model (generated)
├── scaler.pkl              # Feature scaler (generated)
├── sleep_quality_data.csv  # Dataset
├── templates/
│ └── index.html            # Web interface
└── README.md               # Project description
</pre>

Features
--------

- Predicts sleep quality from lifestyle inputs
- Interactive, responsive web UI
- Provides feedback to users
- Fast, local inference via Flask API
- Easily extendable to accept real-time data from wearable devices

Sample Inputs
-------------

Sleep Start | Sleep End | Caffeine | Stress | Steps  | Mood  | Temp
----------- | ----------|----------|--------|--------|------|------
22:30       | 06:30     | 2        | 5      | 7000   | 7    | 22°C

Example Output
--------------
Prediction: 8.3 , 
Category: Good , 
Suggestion: Great job! Keep up the healthy habits.

