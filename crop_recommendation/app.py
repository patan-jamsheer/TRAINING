from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

MODEL_PATH = "model/random_forest_model.pkl"
model = joblib.load(MODEL_PATH)

FEATURES = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        values = [float(data[feature]) for feature in FEATURES]
        X = np.array(values, dtype=float).reshape(1, -1)

        prediction = model.predict(X)[0]

        # Probability gives a useful confidence indicator.
        confidence = None
        if hasattr(model, "predict_proba"):
            confidence = float(np.max(model.predict_proba(X)) * 100)

        return jsonify({
            "success": True,
            "crop": prediction,
            "confidence": round(confidence, 2) if confidence is not None else None
        })

    except (KeyError, TypeError, ValueError) as e:
        return jsonify({
            "success": False,
            "message": f"Invalid input: {str(e)}"
        }), 400

    except Exception as e:
        return jsonify({
            "success": False,
            "message": "Prediction failed. Please check the server."
        }), 500


if __name__ == "__main__":
    app.run(debug=True)
