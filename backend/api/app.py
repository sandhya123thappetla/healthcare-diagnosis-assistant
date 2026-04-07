from fastapi import FastAPI
import pandas as pd
import pickle
import os

app = FastAPI(title="Healthcare Diagnosis API", version="1.0.0")

# ✅ Load XGBoost model
base_dir = os.path.dirname(__file__)
model_path = os.path.join(base_dir, "..", "models", "model.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)

# ✅ Home route
@app.get("/")
def home():
    return {"message": "Healthcare Diagnosis ML API Running 🚀"}

# ✅ Prediction route
@app.post("/predict")
def predict(data: dict):
    try:
        # All features expected by model
        model_features = list(model.feature_names_in_)
        
        # Create full input with 0 for missing features
        input_dict = {feature: 0 for feature in model_features}
        
        # Update with user input only if feature exists
        for key, value in data.items():
            if key in input_dict:
                input_dict[key] = value
        
        # Convert to DataFrame in correct order
        input_data = pd.DataFrame([input_dict])[model_features]
        
        # Predict
        prediction = model.predict(input_data)[0]
        
        return {"predicted_disease": prediction}
    
    except Exception as e:
        return {"error": str(e)}
    



import logging

logging.basicConfig(level=logging.INFO, filename="logs/predictions.log", filemode="a",
                    format="%(asctime)s - %(message)s")

# Inside predict endpoint, after prediction
logging.info(f"Predicted: {prediction} for input: {request.dict()}")