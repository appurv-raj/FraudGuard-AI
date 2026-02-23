from flask import Flask, render_template, request
import pandas as pd
from catboost import CatBoostClassifier
import os

app = Flask(__name__)

# Load model
model = CatBoostClassifier()
model.load_model("catboost_fraud_model.cbm")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        transaction_id = request.form["transaction_id"]  # only for display
        amount = float(request.form["amount"])
        merchant_id = int(request.form["merchant_id"])
        transaction_type = request.form["transaction_type"]
        location = request.form["location"]

        date = pd.to_datetime(request.form["date"])
        time_value = request.form["time"]  # format HH:MM

        # Extract only hour (ignore minutes)
        hour = int(time_value.split(":")[0])

        input_data = pd.DataFrame({
            "Amount": [amount],
            "MerchantID": [merchant_id],
            "TransactionType": [transaction_type],
            "Location": [location],
            "year": [date.year],
            "month": [date.month],
            "day": [date.day],
            "hour": [hour]
        })

        probability = model.predict_proba(input_data)[:, 1][0]
        risk_score = round(probability * 100, 2)

        if risk_score > 70:
            risk_level = "High Risk ⚠"
            status_class = "high"
        elif risk_score > 40:
            risk_level = "Medium Risk ⚠"
            status_class = "medium"
        else:
            risk_level = "Low Risk ✅"
            status_class = "low"

        return render_template(
            "index.html",
            risk_score=risk_score,
            risk_level=risk_level,
            status_class=status_class,
            transaction_id=transaction_id
        )

    except Exception as e:
        return render_template("index.html", error=str(e))


if __name__ == "__main__":
    app.run(debug=True)