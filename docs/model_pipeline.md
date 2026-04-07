# ML Pipeline Explanation

## 1. Data Loading
- Dataset: `ml-pipeline/data/dataset.csv`
- 133 symptoms as features
- Target: `prognosis`

## 2. Preprocessing
- Convert all categorical/yes-no values to numeric (0/1)
- Handle missing values
- Keep column order same as training

## 3. Model Training
- Algorithm: XGBoost Regressor
- Hyperparameters:
  - n_estimators=200
  - learning_rate=0.1
  - max_depth=6

## 4. Evaluation
- Metrics:
  - MAE (Mean Absolute Error)
  - R² Score
- Metrics stored in `docs/metrics.json`

## 5. Production Deployment
- Model saved as `backend/models/model.pkl`
- Served using FastAPI
- Frontend sends symptom inputs to backend API