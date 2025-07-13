#!/bin/bash

echo "🚀 Building Docker image..."
docker build -t api-uptime-tracker .
if [[ $? -ne 0 ]]; then
  echo "❌ Docker build failed!"
  exit 1
fi

# Remove old container if it exists
if docker ps -a --format '{{.Names}}' | grep -Eq '^uptime-tracker$'; then
  echo "🧹 Removing old container..."
  docker rm -f uptime-tracker
fi

echo "🟢 Running container..."
docker run -d -p 8000:8000 --name uptime-tracker api-uptime-tracker
echo "✅ Uptime tracker is now running at http://localhost:8000/metrics"

