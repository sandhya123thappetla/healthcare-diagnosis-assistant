# API Documentation

## POST /predict
Predict disease based on symptoms.

**Request Body (JSON)**:
```json
{
  "itching": 1,
  "skin_rash": 0,
  ...
  "chronic_kidney_disease": 0
}


### Response (JSON):
{
  "predicted_disease": "Fungal infection",
  "model_version": "1.0.0",
  "timestamp": "2026-04-07T16:00:00"
}

### GET /health
Returns service status
### GET /metrics
Returns logs and prediction metrics