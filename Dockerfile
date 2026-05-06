FROM python:3.11-slim

RUN pip install --no-cache-dir mitmproxy

EXPOSE 8080

CMD ["mitmdump", \
     "--listen-host", "0.0.0.0", \
     "--listen-port", "8080", \
     "--mode", "regular"]
