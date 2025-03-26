# Use the official Python image from the Docker Hub
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt to the container
COPY requirements.txt /app/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . /app

# Expose the port on which the Flask app will run
EXPOSE 80

# Command to run the Flask app
CMD ["python", "app.py"]