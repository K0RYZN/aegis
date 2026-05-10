# Mothman

Mothman is a Dockerized HTTP/HTTPS filtering proxy built on top of mitmproxy.

It intercepts browser traffic and blocks known tracker, telemetry, and advertising domains using a modular Python addon system.

---

# Features

- HTTP/HTTPS interception using mitmproxy
- Tracker and ad-provider domain blocking
- Dockerized deployment
- Modular addon architecture
- Persistent HTTPS certificate support
- Local browser traffic inspection and filtering

---

# Requirements

You need:

- Docker
- Firefox (recommended) or another browser with manual proxy support
- Git

---

# Installation

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

# Running Mothman

Start the proxy:

```bash
docker run --rm -it \
  -p 8080:8080 \
  -v mitmproxy-certs:/home/mitmproxy/.mitmproxy \
  mothman
```

Mothman will now run locally on port `8080`.

---

# Browser Proxy Setup

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

Leave SOCKS proxy empty unless you intentionally need it.

---

# HTTPS Certificate Setup

Mothman uses mitmproxy to intercept HTTPS traffic.

To enable HTTPS support:

1. Start Mothman
2. Open your browser
3. Visit:

```text
http://mitm.it
```

IMPORTANT:

```text
Use HTTP, not HTTPS.
```

4. Download the certificate for your browser
5. Follow the browser instructions shown on the page
6. Restart your browser

After this, HTTPS traffic should work correctly.

---

# Why the Docker Volume Matters

This command is important:

```bash
-v mitmproxy-certs:/home/mitmproxy/.mitmproxy
```

Mitmproxy generates its own Certificate Authority (CA).

Without the Docker volume:

- the container stops
- the certificate disappears
- a new certificate gets generated next run
- HTTPS trust breaks in your browser

The volume keeps the certificate persistent between runs.

---

# Important Docker Networking Fix

Mothman runs mitmproxy inside Docker.

Some Docker networking setups make browser traffic appear as a non-local connection.

Without this option:

```text
--set block_global=false
```

mitmproxy may reject the connection with:

```text
Client connection killed by block_global option.
```

Mothman already includes this fix in the Dockerfile.

---

# Project Structure

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

# Current Addons

## Loader

Displays startup and shutdown messages.

## Blacklister

Blocks requests matching domains inside `Blacklist.py`.

---

# Example Blocked Response

```text
BLOCKED BY THE MOTHMAN
```

---

# Troubleshooting

## `http://mitm.it` does not load

Make sure:

- the container is running
- your browser proxy settings are correct
- you are visiting:

```text
http://mitm.it
```

and NOT:

```text
https://mitm.it
```

---

## HTTPS websites fail to load

Delete old mitmproxy certificates from your browser and reinstall the current one from:

```text
http://mitm.it
```

Also make sure you are running the container with:

```bash
-v mitmproxy-certs:/home/mitmproxy/.mitmproxy
```

---

## `Client connection killed by block_global option`

This means mitmproxy rejected the connection because Docker networking made it appear non-local.

Mothman fixes this using:

```text
--set block_global=false
```

---

# Notes

Mothman is intended for:

- local traffic filtering
- HTTP/HTTPS inspection
- learning mitmproxy addon development
- educational security research

Only intercept traffic you own or have permission to inspect.
