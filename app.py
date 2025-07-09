from flask import Flask, request, jsonify, render_template
import joblib
from datetime import datetime, timedelta
import numpy as np

app = Flask(__name__)

# Load the trained model and scaler
model = joblib.load('best_rf_model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # Extract input features
        sleep_start = data['sleep_start']
        sleep_end = data['sleep_end']
        caffeine_intake = float(data['caffeine_intake'])
        stress_level = int(data['stress_level'])
        physical_activity = int(data['physical_activity'])
        mood = int(data['mood'])
        environmental_factors = float(data['environmental_factors'])

        # Calculate sleep duration
        sleep_start_time = datetime.strptime(sleep_start, "%H:%M")
        sleep_end_time = datetime.strptime(sleep_end, "%H:%M")
        if sleep_end_time < sleep_start_time:
            sleep_end_time += timedelta(days=1)

        sleep_duration = (sleep_end_time - sleep_start_time).seconds / 3600

        # Prepare input for prediction
        input_data = [
            sleep_duration,
            caffeine_intake,
            stress_level,
            physical_activity,
            mood,
            environmental_factors
        ]
        input_data_scaled = scaler.transform([input_data])

        prediction = model.predict(input_data_scaled)[0]

        if prediction >= 8:
            category = "Good"
            suggestion = "Great job! Keep up the healthy habits."
        elif 6 < prediction < 8:
            category = "Average"
            suggestion = "You're doing okay! A little effort can make it excellent."
        else:
            category = "Bad"
            suggestion = "Don't worry! Focus on improving your sleep routine."

        return jsonify({
            'prediction': round(prediction, 2),
            'category': category,
            'suggestion': suggestion
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
