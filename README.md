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

## Why I Built This

Mothman started as a personal experiment in HTTPS interception, proxy-based traffic filtering, and tracker blocking. The goal was to understand how browser traffic moves through a local proxy, how certificate trust affects HTTPS inspection, and how domain-based filtering can be implemented with mitmproxy addons.

This project helped me practice Docker deployment, mitmproxy scripting, request inspection, blacklist design, and privacy-focused network tooling.

---

## Demo Output

When Mothman blocks a tracker or ad request, it logs the blocked host and full URL:
```
THE MOTHMAN is ACTIVE

BLOCKED HOST: google-analytics.com | URL: https://www.google-analytics.com/g/collect
BLOCKED HOST: stats.g.doubleclick.net | URL: https://stats.g.doubleclick.net/j/collect
BLOCKED HOST: pagead2.googlesyndication.com | URL: https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js
BLOCKED HOST: analytics.tiktok.com | URL: https://analytics.tiktok.com/i18n/pixel/events.js
```
Blocked requests receive a local 403 Forbidden response:
```
BLOCKED BY THE MOTHMAN
```
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

## Limitations

Mothman currently performs domain-based filtering only. It does not yet fully parse EasyList/uBlock Origin filter syntax, cosmetic filters, request resource types, or advanced allow/exception rules. It is intended as a local learning and traffic-filtering project, not a replacement for a mature browser ad blocker.

---

## Disclaimer

Mothman is intended for local traffic inspection, filtering, and educational security research.

Only intercept or inspect traffic you own or are authorized to analyze.
