# 🌊 Flood Prediction System using Machine Learning

An intelligent, ML-powered early-warning system that predicts flood risk from historical and real-time meteorological data — helping authorities and disaster management teams act *before* disaster strikes, not after.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20App-black?logo=flask)
![scikit--learn](https://img.shields.io/badge/scikit--learn-ML-orange?logo=scikitlearn)
![XGBoost](https://img.shields.io/badge/XGBoost-Best%20Model-green)
![IBM Cloud](https://img.shields.io/badge/Deployment-IBM%20Cloud-054ADA?logo=ibmcloud)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📖 Overview

Floods are among the most devastating natural disasters, claiming thousands of lives and displacing millions every year. Despite their recurring nature, the lack of timely and accurate early-warning systems continues to amplify their destructive impact. Conventional forecasting methods often fall short in predicting floods at the right time, leaving authorities and communities with insufficient opportunity to respond.

This project closes that gap by building a **machine learning–powered flood prediction system** trained on historical weather data. It analyses meteorological features — **annual rainfall, cloud visibility, and seasonal rainfall patterns** — to classify the likelihood of a flood event, and serves predictions through a lightweight, accessible **Flask web application**.

---

## 🎯 Problem Statement

- Conventional flood forecasting is often reactive rather than predictive.
- Disaster response teams frequently lack enough lead time to issue evacuation advisories.
- Existing systems are not always accessible, scalable, or easy for non-technical field staff to use.

**Goal:** Build a reliable, data-driven classification system that predicts flood probability early enough to support evacuation planning and resource allocation, packaged in a simple web interface deployable on the cloud.

---

## ✨ Key Features

- 🔍 **Multi-model comparison** — Decision Tree, Random Forest, K-Nearest Neighbours (KNN), and XGBoost trained and benchmarked against each other.
- 🏆 **Best model auto-selection** — the highest-performing model (XGBoost, 96.55% test accuracy) is serialized and used for inference.
- 🌐 **Flask web application** — simple form-based UI for entering rainfall/cloud visibility data and receiving instant flood-risk predictions.
- ☁️ **Cloud-ready** — designed for deployment on **IBM Cloud** for scalability and remote accessibility.
- 📊 **Interpretable outputs** — clear "Flood" / "No Flood" risk classification to support fast decision-making.

---

## 🧠 Use Case Scenarios

### 1️⃣ Early Flood Warning & Evacuation Planning
A meteorologist enters current rainfall and cloud visibility readings for a flood-prone district. The model predicts a high probability of flooding, allowing authorities to issue evacuation advisories several hours in advance.

### 2️⃣ Disaster Response & Resource Allocation
A disaster relief coordinator uses the web application during monsoon season to monitor multiple regions simultaneously. By entering regional weather data for each area, the system provides instant flood risk classifications, helping prioritize resource deployment.

### 3️⃣ Model Validation & Performance Assessment
A government analyst tests the model against historical flood event data to evaluate accuracy. The **XGBoost model achieves 96.55% accuracy** on test data, confirming the system's reliability for operational use.

---

## 🏗️ System Architecture

```
Historical Weather Data
        │
        ▼
 Data Preprocessing & Feature Engineering
 (rainfall, cloud visibility, seasonal patterns)
        │
        ▼
 Model Training & Evaluation
 ┌───────────────┬────────────────┬─────────┬──────────┐
 │ Decision Tree │ Random Forest  │  KNN    │ XGBoost  │
 └───────────────┴────────────────┴─────────┴──────────┘
        │
        ▼
 Best Model Selection (highest accuracy)
        │
        ▼
 Model Serialization (.pkl)
        │
        ▼
 Flask Web Application (UI + Inference API)
        │
        ▼
 Deployment on IBM Cloud
```

---

## 🛠️ Tech Stack

| Layer            | Technology                                   |
|-------------------|-----------------------------------------------|
| Language          | Python 3.9+                                    |
| ML Libraries      | scikit-learn, XGBoost, pandas, NumPy           |
| Model Persistence | pickle / joblib                                |
| Web Framework     | Flask                                          |
| Frontend          | HTML, CSS (Jinja2 templates)                   |
| Deployment        | IBM Cloud (Cloud Foundry / Code Engine)        |
| Version Control   | Git & GitHub                                   |

---

## 📊 Dataset

The model is trained on historical meteorological data including:

| Feature                  | Description                                      |
|---------------------------|--------------------------------------------------|
| Annual Rainfall           | Total yearly rainfall recorded (mm)               |
| Seasonal Rainfall         | Rainfall broken down by season (monsoon, etc.)    |
| Cloud Visibility          | Visibility/cloud cover readings                   |
| Flood Occurrence (Label)  | Binary target — Flood / No Flood                  |

> Replace this section with the actual source/citation of your dataset (e.g., government meteorological department, Kaggle dataset link, etc.)

---

## 🤖 Model Performance

| Model             | Accuracy   | Notes                                  |
|--------------------|-----------|------------------------------------------|
| Decision Tree      | —         | Fast, interpretable baseline              |
| Random Forest      | —         | Reduced overfitting vs. single tree       |
| KNN                | —         | Sensitive to feature scaling              |
| **XGBoost**        | **96.55%**| 🏆 Best performing — selected for deployment |

> Fill in the accuracy values for Decision Tree, Random Forest, and KNN once you finalize your evaluation table.

---

## 📁 Project Structure

```
flood-prediction-system/
│
├── data/
│   └── flood_dataset.csv              # Historical weather & flood data
│
├── notebooks/
│   └── model_training.ipynb           # EDA, training, evaluation
│
├── model/
│   └── xgboost_flood_model.pkl        # Serialized best model
│
├── app/
│   ├── static/                        # CSS/JS assets
│   ├── templates/
│   │   ├── index.html,homepage.html   # Input form
│   │   └── history.html,result.html   # Prediction output
│   └── app.py                         # Flask application
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.9 or higher
- pip

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/flood-prediction-system.git
cd flood-prediction-system

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Flask application
python app/app.py
```

The application will be available at:
```
http://127.0.0.1:5000/
```

---

## 🚀 Usage

1. Open the web app in your browser.
2. Enter the required meteorological inputs: **annual rainfall, seasonal rainfall, cloud visibility**.
3. Click **Predict**.
4. The system returns a **Flood** / **No Flood** classification along with the predicted risk level.

---

## ☁️ Deployment on IBM Cloud

This application is designed to be deployed on **IBM Cloud** for scalability and remote access:

1. Push the Flask app to an IBM Cloud **Code Engine** project or **Cloud Foundry** runtime.
2. Configure `requirements.txt` and a `Procfile` (`web: python app/app.py`).
3. Bind any required storage/model artifacts to the deployment.
4. Access the app via the public IBM Cloud endpoint from any location.

> Add your specific IBM Cloud deployment steps, service names, and configuration details here once deployed.

---

## 📈 Results & Impact

- Enables **hours of early warning** for flood-prone regions, supporting proactive evacuation planning.
- Provides disaster response teams with a **centralized dashboard** to monitor multiple regions during monsoon season.
- Validated against historical flood records with **96.55% accuracy**, confirming reliability for operational deployment.

---

## 🔮 Future Scope

- Integration with live satellite/weather API feeds for real-time predictions.
- Addition of geospatial mapping to visualize flood-risk zones.
- SMS/email alert integration for automated evacuation notifications.
- Expansion to include river water-level and soil-saturation data for higher precision.

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m "Add your feature"`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📬 Contact

For questions, suggestions, or collaboration opportunities, feel free to open an issue or reach out via GitHub.

---

⭐ If you find this project useful, consider giving it a star on GitHub!
