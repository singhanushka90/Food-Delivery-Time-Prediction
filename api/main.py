from pathlib import Path
import json

import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel




BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "artifacts" / "model" / "final_model.pkl"
PREPROCESSOR_PATH = BASE_DIR / "artifacts" / "transformed" / "preprocessor.pkl"
METRICS_PATH = BASE_DIR / "artifacts" / "evaluation" / "metrics.json"

FRONTEND_DIR = BASE_DIR / "frontend"


model = joblib.load(MODEL_PATH)
preprocessor = joblib.load(PREPROCESSOR_PATH)

with open(METRICS_PATH, "r") as file:
    metrics = json.load(file)



app = FastAPI(
    title="Food Delivery Time Predictor",
    version="1.0"
)


class DeliveryInput(BaseModel):
    Distance_km: float
    Weather: str
    Traffic_Level: str
    Time_of_Day: str
    Vehicle_Type: str
    Preparation_Time_min: int
    Courier_Experience_yrs: float


@app.get("/api/health")
def health_check():
    return {
        "status": "ok",
        "message": "Food Delivery API is running"
    }



@app.get("/api/metrics")
def get_metrics():
    return metrics


@app.post("/api/predict")
def predict_delivery_time(data: DeliveryInput):

    try:
        input_data = pd.DataFrame([data.model_dump()])

        # Apply same preprocessing used during training
        transformed_data = preprocessor.transform(input_data)

        # Prediction
        prediction = model.predict(transformed_data)[0]

        return {
            "predicted_delivery_time_min": round(float(prediction), 2),
            "model": "Linear Regression"
        }

    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )




if FRONTEND_DIR.exists():

    app.mount(
        "/static",
        StaticFiles(directory=FRONTEND_DIR),
        name="static"
    )


@app.get("/", include_in_schema=False)
def home():

    index_file = FRONTEND_DIR / "index.html"

    if index_file.exists():
        return FileResponse(index_file)

    return {
        "message": "Frontend is not created yet."
    }