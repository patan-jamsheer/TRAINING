# CropWise AI - Flask + Random Forest

A crop recommendation web application using:

- Frontend: HTML, CSS, JavaScript
- Backend: Flask
- Machine Learning: Random Forest Classifier
- Dataset: crop_recommendation.csv
- Features: N, P, K, temperature, humidity, ph, rainfall
- Target: label

## 1. Create virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

## 2. Install dependencies

```bash
pip install -r requirements.txt
```

## 3. Train the model

```bash
python train_model.py
```

This creates:

```text
model/random_forest_model.pkl
```

## 4. Run Flask

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

## Project structure

```text
crop_recommendation_app/
│
├── app.py
├── train_model.py
├── crop_recommendation.csv
├── requirements.txt
│
├── model/
│   └── random_forest_model.pkl   # generated after training
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js
```

## Important

The model is trained from the uploaded CSV. Do not manually change the feature names unless you also update `train_model.py` and `app.py`.
