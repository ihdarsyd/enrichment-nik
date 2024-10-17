# Dockerfile

# Use a Python base image
FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .

# Install required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Command to run your Python application
CMD ["python", "main_kafka.py"]
