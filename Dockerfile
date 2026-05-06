FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir mitmproxy

# Expose proxy port (default MITMPROXY port)
EXPOSE 8080

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Run Le-Phrog proxy application
CMD ["mitmproxy"]
