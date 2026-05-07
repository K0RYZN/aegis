# Le-Phrog

Le-Phrog is a intercepting forward proxy that uses MITMPROXY as its engine

## What It Does

Le-Phrog acts as an HTTP/HTTPS intercepting proxy.
<img width="1692" height="930" alt="ChatGPT Image May 5, 2026, 05_32_35 PM" src="https://github.com/user-attachments/assets/e544b8b1-a678-428f-980f-8f5b42951c3a" />
Current addon stack:

- `Loader` — prints startup/shutdown messages
- `Blacklister` — blocks requests matching domains in `BLACKLIST.py`
- `Agents` — modifies request headers
- `BlockJS` — blocks `.js` requests

Mitmproxy handles the proxy engine, TLS interception, certificate generation, and traffic forwarding.

## Requirements

You need:

- Docker
- Firefox or another browser with manual proxy settings
- Git

## Install

Clone the repository:

```bash
git clone https://github.com/M0usetrap777/Le-Phrog.git
cd Le-Phrog
```
Build the Docker image
```bash
docker build -t le-phrog .
```
Run Le-Phrog
```bash
docker run --rm -it \
  -p 8080:8080 \
  -v mitmproxy-certs:/home/mitmproxy/.mitmproxy \
  le-phrog
```
after you run it, it should work perfetly fine. Howver, if you want HTTPS support you will need to do a few extra simple steps.
