# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the rest of the app code to the container
COPY . .

# Expose the port that the app will run on
EXPOSE 5000

# Start the app
CMD ["python", "run.py"]
