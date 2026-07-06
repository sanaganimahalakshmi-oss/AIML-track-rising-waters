# 🌊 Rising Waters – Intelligent Flood Risk Prediction Using Machine Learning

## 📚 Project Overview

**Rising Waters** is a web-based Machine Learning application designed to estimate flood risk using important weather and environmental factors. The system analyzes user-provided data and predicts whether the flood risk is **High** or **Low**.

The application is built with **Python**, **Flask**, and a **Random Forest Classifier**, providing quick and reliable predictions through a clean and interactive interface.

---

## 🎯 Aim of the Project

- Develop an intelligent flood prediction system.
- Assist in early flood risk assessment.
- Apply Machine Learning to disaster management.
- Create a simple web application for users.
- Improve awareness through AI-based prediction.


## 💻 Technologies Used

- Python
- Flask Framework
- HTML
- CSS
- Pandas
- NumPy
- Scikit-learn
- Joblib

---

## 🧠 Machine Learning Model

### Random Forest Classifier

The prediction model is developed using the **Random Forest Classifier**, which performs well on classification tasks and provides accurate predictions by combining multiple decision trees.

---

## 📥 User Inputs

The prediction is based on the following parameters:

- Annual Rainfall
- Seasonal Rainfall
- Temperature
- Humidity
- River Level
- Soil Moisture
- Wind Speed
- Atmospheric Pressure
- Visibility
- Cloud Cover

---

## 📤 Prediction Result

After processing the input values, the application displays one of the following:

- 🌊 High Flood Risk
- ✅ Low Flood Risk


## 🌟 Key Features

- AI-powered flood prediction
- Fast prediction results
- Easy-to-use interface
- Machine Learning integration
- Responsive Flask application
- Simple project architecture

---

## 📁 Project Structure

```
Raising_Waters/
│── app.py
│── flood_data.csv
│── flood_model.pkl
│── scaler.pkl
│── generate_dataset.py
│── requirements.txt
│── README.md
│
├── templates/
│   ├── index.html
│   └── result.html
│
└── static/
    └── style.css
```

---

## ⚙️ Setup Instructions

## ⚙️ Installation Guide

Follow these steps to run the project on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Raising_Waters.git
```

### 2. Navigate to the Project Directory

```bash
cd Raising_Waters
```

### 3. Install the Required Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask Application

```bash
python app.py
```

### 5. Open in Your Browser

Visit the following URL:

```
http://127.0.0.1:5000
```

The application will start, and you can enter the required weather and environmental parameters to predict the flood risk.

## 🔄 Workflow

1. Enter environmental data.
2. Flask receives the input.
3. Data is scaled using the trained scaler.
4. Random Forest predicts flood risk.
5. The result is displayed instantly.

---

## 🚀 Future Scope

- Weather API integration
- Live flood monitoring
- Google Maps support
- SMS and Email notifications
- Mobile application
- IoT sensor connectivity
- Improved prediction accuracy

---

## 👩‍💻 Developer

**Name:** Mahalakshmi Sanagari

**Branch:** Artificial Intelligence and Machine Learning

**Year:** IV B.Tech

**Rollno:**23AK1A3345

**College:** Annamacharya Institute of Technology and Sciences, Tirupati

****Internship**: SmartBridge

## 📌 Final Thoughts

**Rising Waters** demonstrates how Machine Learning can be effectively used to predict flood risk based on environmental conditions. By integrating AI with a Flask web application, the project offers a practical solution that can be expanded with real-time data and smart alert systems in the future.

