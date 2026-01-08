from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

MODULES = [
    "../module2_centralized_model.py",
    "../module3_federated_learning.py",
    "../module4_drift_detection.py",
    "../module5_model_swapping.py",
    "../module6_evaluation.py"
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/run")
def run_all():
    logs = []

    age = request.args.get("age")
    bp = request.args.get("bp")
    chol = request.args.get("chol")
    heart_rate = request.args.get("heart_rate")
    activity = request.args.get("activity")
    disease = request.args.get("disease")

    logs.append(f"Patient Age: {age}")
    logs.append(f"Blood Pressure: {bp}")
    logs.append(f"Cholesterol: {chol}")
    logs.append(f"Heart Rate: {heart_rate}")
    logs.append(f"Activity Level: {activity}")
    logs.append(f"Known Conditions: {disease}")

    for m in MODULES:
        logs.append(subprocess.getoutput(f"python3 {m}"))

    return render_template("index.html", logs=logs)

if __name__ == "__main__":
    app.run(debug=True)
