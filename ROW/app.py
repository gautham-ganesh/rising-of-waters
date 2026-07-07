from flask import Flask, request, render_template, redirect, url_for, session
import joblib
import pandas as pd
import os
import json
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'flood-prediction-secret'

HISTORY_FILE = 'prediction_history.json'

def load_history():
    """Load prediction history from file."""
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, 'r') as f:
                return json.load(f)
        except:
            return []
    return []

def save_history(history):
    """Save prediction history to file."""
    with open(HISTORY_FILE, 'w') as f:
        json.dump(history, f, indent=2)

def add_to_history(input_data, result):
    """Add a prediction to the history."""
    history = load_history()
    entry = {
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'inputs': input_data,
        'result': result
    }
    history.append(entry)
    save_history(history)

MODEL_PATH = 'models/flood_model.joblib'
SCALER_PATH = 'models/scaler.joblib'

if not os.path.exists(MODEL_PATH) or not os.path.exists(SCALER_PATH):
    print("ERROR: Model or Scaler not found! Please run train.py first.")
    exit(1)

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

FEATURE_COLUMNS = [
    'Temp',
    'Humidity',
    'Cloud Cover',
    'ANNUAL',
    'Jan-Feb',
    'Mar-May',
    'Jun-Sep',
    'Oct-Dec',
    'avgjune',
    'sub'
]


@app.route('/')
def home():
    return render_template('homepage.html')


@app.route('/prediction', methods=['GET'])
def prediction_page():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        if request.is_json:
            data = request.get_json()
        else:
            data = request.form

        input_data = {
            'temp': float(data['temp']),
            'humidity': float(data['humidity']),
            'cloud_cover': float(data['cloud_cover']),
            'annual_rainfall': float(data['annual_rainfall']),
            'jan_feb': float(data['jan_feb']),
            'mar_may': float(data['mar_may']),
            'jun_sep': float(data['jun_sep']),
            'oct_dec': float(data['oct_dec']),
            'avg_june': float(data['avg_june']),
            'sub_index': float(data['sub_index'])
        }

        features_df = pd.DataFrame([
            {
                'Temp': input_data['temp'],
                'Humidity': input_data['humidity'],
                'Cloud Cover': input_data['cloud_cover'],
                'ANNUAL': input_data['annual_rainfall'],
                'Jan-Feb': input_data['jan_feb'],
                'Mar-May': input_data['mar_may'],
                'Jun-Sep': input_data['jun_sep'],
                'Oct-Dec': input_data['oct_dec'],
                'avgjune': input_data['avg_june'],
                'sub': input_data['sub_index']
            }
        ], columns=FEATURE_COLUMNS)

        features_scaled = scaler.transform(features_df)
        prediction = model.predict(features_scaled)[0]
        prediction_proba = model.predict_proba(features_scaled)[0]

        result = {
            'flood': int(prediction) == 1,
            'flood_probability': float(prediction_proba[1]) * 100,
            'no_flood_probability': float(prediction_proba[0]) * 100
        }

        add_to_history(input_data, result)
        session['prediction_result'] = result
        return redirect(url_for('result_page'))
    except Exception as e:
        return render_template('index.html', error=str(e))


@app.route('/result')
def result_page():
    result = session.pop('prediction_result', None)
    if not result:
        return redirect(url_for('prediction_page'))
    return render_template('result.html', result=result)


@app.route('/history')
def history_page():
    history = load_history()
    return render_template('history.html', history=list(reversed(history)))


if __name__ == '__main__':
    app.run(port=5000, debug=True)
