
# Frontend Instructions - Streamlit App

## How to Run

1. Open terminal in `frontend/` folder.
2. Run the Streamlit app:

```bash
python -m streamlit run app.py

### UI Features
Select symptoms from a dynamically generated list (133 symptoms)
Symptoms are read automatically from the dataset
Click Predict Disease to get a real-time prediction
Frontend sends symptom inputs to the FastAPI backend
Predicted disease is displayed instantly

### Tips
Ensure the backend is running (uvicorn api.app:app --reload) before making predictions
Logs of predictions are saved at backend/logs/predictions.log