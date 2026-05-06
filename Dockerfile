FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    ca-certificates \
    openssl \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir mitmproxy

EXPOSE 8080

ENV PYTHONUNBUFFERED=1
ENV MITMPROXY_CADIR=/root/.mitmproxy

CMD ["mitmdump", \
     "--listen-host", "0.0.0.0", \
     "--listen-port", "8080", \
     "--mode", "regular", \
     "--set", "block_global=false"]
