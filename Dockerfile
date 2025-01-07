# Use the official Python image as a base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask app code into the container
COPY . /app

# Expose the Flask app's port (if running on default 5000)
EXPOSE 5000

# Specify the command to run the Flask app
CMD ["python", "application.py"]
