from flask import Flask, request, jsonify, render_template, Response, session
import joblib
import numpy as np
import pandas as pd
import shap
import json, time, random, logging

app = Flask(__name__)
app.secret_key = "secret123"

# Logging
logging.basicConfig(filename='logs/app.log', level=logging.INFO)

# Load model
model = joblib.load("saved_models/model.pkl")
explainer = shap.Explainer(model)

# Dummy users
users = {"admin": "1234"}

@app.route("/")
def home():
    return render_template("index.html")

# ================= LOGIN =================
@app.route("/login", methods=["POST"])
def login():
    data = request.json
    if users.get(data["username"]) == data["password"]:
        session["user"] = data["username"]
        return jsonify({"status": "success"})
    return jsonify({"status": "fail"})

# ================= PREDICT =================
@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    features = np.array([[float(data["amount"]), float(data["time"])]])

    pred = model.predict(features)[0]
    prob = model.predict_proba(features)[0][1]

    shap_values = explainer(features)

    logging.info(f"Prediction: {pred}, Prob: {prob}")

    return jsonify({
        "prediction": int(pred),
        "probability": float(prob),
        "shap": shap_values.values.tolist()[0]
    })

# ================= CSV UPLOAD =================
@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    df = pd.read_csv(file)

    preds = model.predict(df[['Amount','Time']])
    df["Fraud"] = preds

    return df.to_json()

# ================= LIVE STREAM =================
@app.route("/stream")
def stream():
    def generate():
        while True:
            data = {
                "amount": round(random.uniform(10, 5000), 2),
                "time": random.randint(1, 100000)
            }

            features = np.array([[data["amount"], data["time"]]])
            pred = model.predict(features)[0]

            data["prediction"] = int(pred)

            yield f"data:{json.dumps(data)}\\n\\n"
            time.sleep(2)

    return Response(generate(), mimetype='text/event-stream')

if __name__ == "__main__":
    app.run(debug=True)
