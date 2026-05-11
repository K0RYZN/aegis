# AEGIS Docker Setup

## Quick Start

```bash
docker build -t AEGIS .
docker run -p 8080:8080 AEGIS
```

## Proxy Configuration

**Set your browser/application proxy to:**
- Host: `localhost` or `127.0.0.1`
- Port: `8080`
- Protocol: HTTP

## Important Notes

1. **HTTPS Warnings**: When accessing HTTPS sites through AEGIS, you may get certificate warnings because mitmproxy creates its own certificates for traffic inspection. This is normal.

2. **Importing Certificates** (Optional - to remove warnings):
   - The mitmproxy CA certificate is available at: `~/.mitmproxy/mitmproxy-ca-cert.pem` (on your host machine, copy from container)
   - Import this certificate into your browser's trusted certificates

3. **Traffic Blocking**: AEGIS blocks domains from `Blacklist.py` and JavaScript files (.js)

