# Mothman

Mothman is a Dockerized HTTP/HTTPS filtering proxy built on top of mitmproxy.

It intercepts browser traffic and blocks known advertising, telemetry, and tracking domains using a modular Python addon system.

---

## Features

- HTTP/HTTPS intercepting proxy
- Tracker and telemetry filtering
- Dockerized deployment
- Persistent HTTPS certificate support
- Modular mitmproxy addon architecture
- Domain/subdomain filtering
- Console logging for blocked requests
- Session statistics and request counters

---

## Current Addon Stack

| Addon | Purpose |
|---|---|
| `Loader` | Prints startup and shutdown status |
| `Blacklister` | Blocks requests matching known tracking/advertising domains |

---

## Requirements

You will need:

- Docker
- Firefox (or another browser with manual proxy support)
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

Run Mothman:

```bash
docker run --rm -it \
  -p 8080:8080 \
  -v mitmproxy-certs:/home/mitmproxy/.mitmproxy \
  mothman
```

---

# Browser Setup

Open Firefox settings:

```text
Settings → Network Settings → Manual Proxy Configuration
```

Set:

```text
HTTP Proxy: 127.0.0.1
Port: 8080

HTTPS Proxy: 127.0.0.1
Port: 8080
```

Leave SOCKS blank unless you intentionally need it.

---

# HTTPS Certificate Setup

Mothman uses mitmproxy for HTTPS interception.

To enable HTTPS support:

1. Start Mothman
2. Open:

```text
http://mitm.it
```

3. Download the Firefox certificate
4. Import it into Firefox:

```text
Settings → Privacy & Security → Certificates → View Certificates → Authorities → Import
```

5. Enable:

```text
Trust this CA to identify websites
```

6. Restart Firefox

After this, HTTPS traffic should work correctly.

---

# Testing

Test plain HTTP:

```text
http://example.com
```

Test HTTPS:

```text
https://example.com
```

If both work, Mothman is functioning correctly.

---

# How Mothman Works

Mothman runs mitmproxy inside Docker and loads custom Python addons through `Main.py`.

Traffic flow:

```text
Browser
    ↓
Mothman Proxy (mitmproxy)
    ↓
Blacklist Filtering
    ↓
Destination Website
```

Blocked requests receive a local HTTP 403 response before they ever reach the target server.

---

# Session Statistics

Mothman supports session-level statistics and request counters.

Example console output:

```text
[MOTHMAN] BLOCKED HOST: google-analytics.com
[MOTHMAN] BLOCKED HOST: doubleclick.net

[MOTHMAN] SESSION SUMMARY
Blocked Requests: 17
Unique Domains Blocked: 6
```

This makes traffic filtering easier to observe and debug.

---

# Recommended Project Structure

```text
mothman/
├── Main.py
├── Blacklister.py
├── requirements.txt
├── Dockerfile
├── README.md
├── blocklists/
│   └── trackers.txt
├── tests/
│   └── test_blacklister.py
```

Moving the blacklist into a plain text file makes the project easier to maintain and expand.

---

# Pytest Support

Mothman can include pytest unit tests for blacklist matching logic.

Example test cases:

```python
def test_exact_match():
    assert host_matches("doubleclick.net", "doubleclick.net")

def test_subdomain_match():
    assert host_matches("ad.doubleclick.net", "doubleclick.net")

def test_false_match():
    assert not host_matches("notdoubleclick.net", "doubleclick.net")
```

This helps validate domain matching behavior and improves project quality.

---

# Docker Compose

A `docker-compose.yml` file allows Mothman to start with a single command.

Example:

```yaml
services:
  mothman:
    build: .
    ports:
      - "8080:8080"
    volumes:
      - mitmproxy-certs:/home/mitmproxy/.mitmproxy

volumes:
  mitmproxy-certs:
```

Then you can start Mothman with:

```bash
docker compose up
```

instead of manually typing the full Docker command every time.

---

# Troubleshooting

## HTTPS does not work

Make sure:

- You imported the mitmproxy certificate from:

```text
http://mitm.it
```

- The certificate was imported under:

```text
Authorities
```

- Firefox was restarted after import

- The proxy settings are correct

---

## `Client connection killed by block_global option`

This is a common Docker networking issue with mitmproxy.

In some Docker setups, browser connections may appear as non-local IP addresses.

Without this option:

```text
--set block_global=false
```

mitmproxy may reject all browser connections.

Mothman includes this setting by default inside the Dockerfile.

---

## `http://mitm.it` does not load

Check:

- Firefox is actually using the proxy
- Proxy settings point to `127.0.0.1:8080`
- HTTPS-only mode is disabled temporarily
- SOCKS proxy settings are empty

Also make sure you are visiting:

```text
http://mitm.it
```

NOT:

```text
https://mitm.it
```

---

## HTTPS suddenly stopped working after restarting Docker

This usually happens when mitmproxy generates a new certificate authority.

Mothman avoids this by using:

```bash
-v mitmproxy-certs:/home/mitmproxy/.mitmproxy
```

This keeps the same certificate authority between container runs.

---

## `ModuleNotFoundError`

Rebuild the Docker image:

```bash
docker build -t mothman .
```

Make sure all required Python dependencies exist inside `requirements.txt`.

---

## Websites partially break or load incorrectly

Some websites depend heavily on JavaScript, tracking scripts, or analytics endpoints.

Aggressive filtering may break portions of modern websites.

This is expected behavior for some domains.

---

# Security Notes

Mothman is intended for:

- Educational research
- Local traffic inspection
- Privacy experimentation
- HTTP/HTTPS filtering

Only intercept traffic you own or are authorized to inspect.

---

# Credits

- mitmproxy
- Docker
- Python
