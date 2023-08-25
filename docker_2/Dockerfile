# Use the official Python image as the base 
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the local application files into the container
COPY app.py .
COPY requirements.txt .

# Install dependencies 
RUN pip install -r requirements.txt

# Define the command to run when the container starts
CMD ["python", "app.py"]