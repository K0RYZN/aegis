# Mothman

Mothman is a Dockerized HTTP/HTTPS filtering proxy built on top of mitmproxy.

It intercepts browser traffic and blocks known advertising, telemetry, and tracking domains using a modular Python addon system.

---

## Features

- HTTP and HTTPS traffic interception
- Tracker and ad-provider domain filtering
- Dockerized deployment
- Modular mitmproxy addon architecture
- Persistent certificate support for HTTPS inspection
- Lightweight and locally hosted

---

## Current Addons

| Addon | Description |
|---|---|
| `Loader` | Displays startup and shutdown messages |
| `Blacklister` | Blocks requests matching domains defined in `Blacklist.py` |

---

## Requirements

- Docker
- Firefox or another browser with manual proxy support
- Git

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

The `mitmproxy-certs` volume preserves the generated certificate authority between runs. This prevents HTTPS trust issues caused by certificate regeneration.

---

## Browser Configuration

Configure your browser to use the proxy manually.

### Firefox Example

Go to:

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

Leave SOCKS proxy settings empty unless specifically required.

---

## HTTPS Certificate Installation

To enable HTTPS interception, Mothman’s certificate authority must be trusted by the browser.

While the proxy is running, visit:

```text
http://mitm.it
```

Download the certificate for your browser/platform and follow the provided installation instructions.

After importing the certificate, restart the browser.

---

## Testing

Test standard HTTP traffic:

```text
http://example.com
```

Test HTTPS traffic:

```text
https://example.com
```

If both pages load correctly, the proxy is functioning properly.

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

## Technical Notes

Mothman runs on the official `mitmproxy/mitmproxy` Docker image.

The proxy uses:

```text
--set block_global=false
```

to prevent mitmproxy from rejecting Docker-networked client connections in certain bridged networking environments.

---

## Disclaimer

Mothman is intended for local traffic inspection, filtering, and educational security research.

Only intercept or inspect traffic you own or are authorized to analyze.
