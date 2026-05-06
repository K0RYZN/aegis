FROM python:3.11-slim

WORKDIR /app

# Install system dependencies including CA certificates
RUN apt-get update && apt-get install -y \
    ca-certificates \
    openssl \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . /app

# Install Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose proxy port
EXPOSE 8080

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV MITMPROXY_CADIR=/root/.mitmproxy

# Run Le-Phrog proxy with Main.py addons script in regular proxy mode
# Main.py contains: Loader, Blacklister, Agents (User-Agent rotation), BlockJS (JavaScript blocker)
# Using --mode regular for standard HTTP/HTTPS proxying
# Certificates will be auto-generated on first run
CMD ["mitmdump", \
     "--listen-host", "0.0.0.0", \
     "--listen-port", "8080", \
     "--mode", "regular", \
     "--no-server", \
     "--ssl-insecure", \
     "-s", "Main.py"]
