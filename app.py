from flask import Flask, render_template, request
import pickle
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(__file__)
model_path = os.path.join(BASE_DIR, "spam_model.pkl")
vectorizer_path = os.path.join(BASE_DIR, "vectorizer.pkl")

try:
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    with open(vectorizer_path, "rb") as f:
        vectorizer = pickle.load(f)
except FileNotFoundError as e:
    raise FileNotFoundError(f"Required model file not found: {e.filename}")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    email = request.form["email"]

    data = vectorizer.transform([email])
    prediction = model.predict(data)

    if prediction[0] == 1:
        result = "🚨 Spam Email"
    else:
        result = "✅ Ham (Safe Email)"

    return render_template("index.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)