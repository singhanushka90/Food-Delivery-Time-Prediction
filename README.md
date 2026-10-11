# 🍔 Food Delivery Time Prediction

An end-to-end machine learning project that predicts how long a food delivery will take, based on distance, weather, traffic, time of day, vehicle type, preparation time and courier experience. The model is served through a **FastAPI** backend with a clean web frontend, and the training pipeline is tracked with **DVC**.

## 🚀 Live Demo

- **App:** https://food-delivery-time-prediction-4jbg.onrender.com
- **API Docs (Swagger):** https://food-delivery-time-prediction-4jbg.onrender.com/docs

> Hosted on Render's free tier, so the app sleeps after 15 minutes of inactivity. The first request may take ~50 seconds to wake it up.

## ✨ Features

- Predicts estimated delivery time (in minutes) from user inputs
- Interactive frontend (HTML, CSS, JavaScript) served by the same FastAPI app
- Displays model performance (R², RMSE, MAE) next to every prediction
- Modular ML pipeline: ingestion → validation → transformation → training → evaluation
- Multiple models compared, best one saved as the final model
- Data and pipeline versioning with DVC

## 🧠 Model Performance

| Metric | Value |
|--------|-------|
| Final Model | Linear Regression |
| R² Score | 82.12% |
| RMSE | 8.95 |
| MAE | 6.06 |

Models compared during training: Linear Regression, Decision Tree, Random Forest, Gradient Boosting, XGBoost.

## 📥 Input Features

| Feature | Description |
|---------|-------------|
| Distance | Delivery distance (km) |
| Weather | e.g. Clear, Rainy, Foggy, Snowy, Windy |
| Traffic Level | Low / Medium / High |
| Time of Day | Morning / Afternoon / Evening / Night |
| Vehicle Type | e.g. Bike, Scooter, Car |
| Preparation Time | Restaurant preparation time (minutes) |
| Courier Experience | Courier experience (years) |

## 🗂️ Project Structure

```
Food-Delivery-Time-Prediction/
├── api/
│   └── main.py              # FastAPI app (loads model, serves frontend + API)
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
├── src/
│   ├── data_ingestion.py
│   ├── data_validation.py
│   ├── data_transformation.py
│   ├── model_trainer.py
│   └── model_evaluation.py
├── artifacts/
│   ├── model/               # final_model.pkl
│   ├── transformed/         # preprocessor.pkl
│   └── evaluation/          # metrics.json
├── data/experiments/        # raw dataset (tracked with DVC)
├── dvc.yaml                 # DVC pipeline stages
├── dvc.lock
├── requirements.txt
└── README.md
```

## 🛠️ Tech Stack

- **Language:** Python 3.11
- **ML:** scikit-learn, XGBoost, pandas, NumPy, joblib
- **Backend:** FastAPI, Uvicorn
- **Frontend:** HTML, CSS, JavaScript
- **MLOps:** DVC
- **Deployment:** Render

## ⚙️ Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/singhanushka90/Food-Delivery-Time-Prediction.git
cd Food-Delivery-Time-Prediction

# 2. Create a virtual environment (Python 3.11 recommended)
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS / Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start the API
uvicorn api.main:app --reload
```

Open http://127.0.0.1:8000 for the app and http://127.0.0.1:8000/docs for the API docs.

## 🔁 Re-train the Model (optional)

```bash
dvc repro
```

This runs the full pipeline (ingestion → validation → transformation → training → evaluation) and regenerates the files inside `artifacts/`.

## ☁️ Deployment (Render)

- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `uvicorn api.main:app --host 0.0.0.0 --port $PORT`
- **Environment Variable:** `PYTHON_VERSION = 3.11.9`

The trained artifacts (`final_model.pkl`, `preprocessor.pkl`, `metrics.json`) are committed to the repo so that Render can load them at startup.

## 📌 Future Improvements

- Add input validation and sensible value limits to avoid unrealistic predictions
- Try hyperparameter tuning and more models
- Add automated tests and CI/CD with GitHub Actions
- Move model storage to a DVC remote or cloud storage

## 👩‍💻 Author

**Anushka Singh**
GitHub: [@singhanushka90](https://github.com/singhanushka90)

---

⭐ If you found this project useful, consider giving it a star!