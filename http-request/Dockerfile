# Use official Python image
FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Copy application files
COPY app.py .
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Run the script
CMD ["python", "app.py"]