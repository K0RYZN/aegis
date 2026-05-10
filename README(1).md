# Mothman

Mothman is a Dockerized HTTP/HTTPS filtering proxy built on top of [mitmproxy](https://mitmproxy.org/).

It intercepts browser traffic and blocks known advertising, telemetry, and tracking domains using a modular Python addon system.

The project was built as a hands-on networking and security project focused on:

* HTTP/HTTPS interception
* Dockerized proxy deployment
* TLS certificate handling
* Domain filtering logic
* mitmproxy addon development
* Browser proxy configuration
* Traffic inspection and filtering

---

## Features

* HTTP and HTTPS proxy support
* Dockerized deployment
* Modular mitmproxy addon system
* Domain-based tracker and ad blocking
* Persistent HTTPS certificate support
* Lightweight and locally hosted

---

## Current Addons

### Loader

Displays startup and shutdown status messages when the proxy starts.

### Blacklister

Blocks requests matching domains listed in `Blacklist.py`.

Current filtering targets include:

* Advertising networks
* Telemetry providers
* Tracking services
* Analytics domains

---

## Project Structure

```text
mothman/
├── Main.py
├── Blacklister.py
├── Blacklist.py
├── logo.py
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## Requirements

You need:

* Docker
* Firefox (or another browser with manual proxy support)
* Git

---

## Installation

Clone the repository:

```bash
git clone https://github.com/M0usetrap777/mothman.git
cd mothman
```

Build the Docker image:

```bash
docker build -t mothman .
```

---

## Running Mothman

Start the proxy:

```bash
docker run --rm -it \
  -p 8080:8080 \
  -v mitmproxy-certs:/home/mitmproxy/.mitmproxy \
  mothman
```

This starts Mothman on port `8080`.

The `mitmproxy-certs` Docker volume preserves the mitmproxy certificate authority between runs. Without this volume, Docker may generate a new CA certificate every time the container starts, which can break HTTPS trust in the browser.

---

## Browser Proxy Configuration

In Firefox:

```text
Settings → Network Settings → Manual proxy configuration
```

Set:

```text
HTTP Proxy: 127.0.0.1
Port: 8080

HTTPS Proxy: 127.0.0.1
Port: 8080
```

Leave SOCKS blank unless you intentionally plan to chain another proxy.

---

## HTTPS Setup

To enable HTTPS interception and filtering:

1. Start Mothman
2. Open:

```text
http://mitm.it
```

3. Download the certificate for Firefox
4. Follow the browser instructions provided by mitmproxy
5. Restart Firefox

Once the certificate is trusted, HTTPS traffic can be intercepted and filtered correctly.

---

## Why `block_global=false` Is Used

Mothman runs mitmproxy inside Docker.

In some Docker networking environments, browser traffic may appear to come from a non-local IP address. Mitmproxy blocks these connections by default using the `block_global` security option.

Mothman disables this behavior with:

```text
--set block_global=false
```

This allows local Docker networking to function correctly during development and testing.

---

## Example Console Output

```text
THE MOTHMAN is ACTIVE

BLOCKED HOST: google-analytics.com
URL: https://google-analytics.com/g/collect

BLOCKED HOST: doubleclick.net
URL: https://doubleclick.net/pagead/id
```

---

## Dockerfile

```dockerfile
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
```

---

## Troubleshooting

### HTTPS Sites Fail To Load

Make sure:

* The mitmproxy certificate is installed correctly
* Firefox is configured to use the proxy
* The Docker cert volume is mounted properly

If needed, remove old mitmproxy certificates from Firefox and reinstall the current one from:

```text
http://mitm.it
```

---

### `Client connection killed by block_global option`

This occurs when mitmproxy believes the client connection is coming from a global/non-local address.

Mothman fixes this by launching mitmproxy with:

```text
--set block_global=false
```

---

### `ModuleNotFoundError`

Rebuild the Docker image:

```bash
docker build -t mothman .
```

---

## Disclaimer

Mothman is intended for local traffic inspection, filtering, and educational security research.

Only intercept traffic you own or are authorized to inspect.
