FROM python:3.11-slim

WORKDIR /app

# Install minimal system dependencies
RUN apt-get update && apt-get install -y \
    ca-certificates \
    openssl \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose mitmproxy HTTP/S proxy port
EXPOSE 8080

ENV PYTHONUNBUFFERED=1
ENV MITMPROXY_CADIR=/root/.mitmproxy

# Run Le-Phrog as a normal HTTP/S intercepting proxy
CMD ["mitmdump", \
     "--listen-host", "0.0.0.0", \
     "--listen-port", "8080", \
     "--mode", "regular", \
     "--ssl-insecure"]
