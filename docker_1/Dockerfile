#Use the official Python image as base image
FROM python:3.8-slim

#Set the working directory inside the container
WORKDIR /app

#Copy the local app.py file into the container at /app
COPY app.py .

#Run the Python script when the container starts 
CMD ["python", "app.py"]

