# Use official Python image as base
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy your project code
COPY . .

# Expose the port FastAPI runs on
EXPOSE 8000

# Command to run the app with Uvicorn
CMD ["uvicorn", "main3:app", "--host", "0.0.0.0", "--port", "8000"]
