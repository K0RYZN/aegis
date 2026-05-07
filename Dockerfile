FROM mitmproxy/mitmproxy:latest

WORKDIR /addons

COPY requirements.txt /addons/requirements.txt
RUN pip install --no-cache-dir -r /addons/requirements.txt

COPY . /addons

EXPOSE 8080

CMD ["mitmdump", \
     "--listen-host", "0.0.0.0", \
     "--listen-port", "8080", \
     "--mode", "regular", \
     "--set", "block_global=false", \
     "-s", "/addons/Main.py"]
