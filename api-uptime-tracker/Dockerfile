# Use a lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app files
COPY checker.py .
COPY config.yaml .

# Expose metrics port
EXPOSE 8000

# Run the app
CMD ["python", "checker.py"]
