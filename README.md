# Healthcare Diagnosis Assistant - Capstone Project

## 🎯 Project Overview
The Healthcare Diagnosis Assistant predicts diseases based on symptoms using machine learning.  
It features:
- XGBoost-based prediction model
- FastAPI backend for serving predictions
- Streamlit frontend for interactive UI
- Logging of predictions and performance metrics

## 🛠️ Features
- 133 symptoms as input
- Real-time predictions
- Dynamic frontend updates automatically with dataset
- Logs predictions for audit and analytics

## 🖥️ System Architecture
- Frontend: Streamlit
- Backend: FastAPI
- ML: XGBoost, Scikit-learn
- Data: CSV dataset of symptoms and diseases

## 🚀 How to Run Locally

### Backend:
```bash
cd backend
python -m uvicorn api.app:app --reload

### Frontend:
```bash
cd frontend
python -m streamlit run app.py

### Open:
Backend API docs: http://127.0.0.1:8000/docs
Frontend UI: http://localhost:8501


📈 Results
Model Accuracy: ~100% on training set (for demo purposes)
Predictions are returned in real-time through API
Logs stored at backend/logs/predictions.log


📁 Project Structure
capstone-project/
├── backend/
├── frontend/
├── ml-pipeline/
├── docs/
├── tests/
├── requirements.txt
