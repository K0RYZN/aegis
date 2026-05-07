FROM mitmproxy/mitmproxy:latest

WORKDIR /addons

COPY . /addons

EXPOSE 8080

CMD ["mitmdump", \
     "--listen-host", "0.0.0.0", \
     "--listen-port", "8080", \
     "--mode", "regular", \
     "--set", "block_global=false", \
     "-s", "/addons/Main.py"]
