# backend/Dockerfile
FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY . .

# Expose port
EXPOSE 8000

# Run FastAPI
CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8000"]