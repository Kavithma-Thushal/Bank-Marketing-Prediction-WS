# Use official Python
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy all files to container
COPY . .

# Expose correct port
EXPOSE 80

# Run flask app
CMD ["python", "app.py"]