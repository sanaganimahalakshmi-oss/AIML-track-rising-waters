from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load model and scaler
model = joblib.load("models/flood_model.pkl")
scaler = joblib.load("models/scaler.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = [
            float(request.form["annual_rainfall"]),
            float(request.form["seasonal_rainfall"]),
            float(request.form["temperature"]),
            float(request.form["humidity"]),
            float(request.form["river_level"]),
            float(request.form["soil_moisture"]),
            float(request.form["wind_speed"]),
            float(request.form["pressure"]),
            float(request.form["visibility"]),
            float(request.form["cloud_cover"])
        ]

        data = np.array(data).reshape(1, -1)
        data = scaler.transform(data)

        prediction = model.predict(data)[0]
        probability = model.predict_proba(data)[0][1] * 100

        result = "HIGH FLOOD RISK" if prediction == 1 else "LOW FLOOD RISK"

        return render_template(
            "result.html",
            result=result,
            probability=round(probability, 2)
        )

    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    app.run(debug=True)