## Troubleshooting

### `Client connection killed by block_global option`

If Mothman logs an error like:

```text
Client connection killed by block_global option
```

mitmproxy is rejecting the incoming browser connection because it appears to come from a non-local IP address.

This can happen when running mitmproxy inside Docker because Docker may route traffic through a bridged or virtual network interface instead of showing the client as 127.0.0.1.

Mothman uses:
```
--set block_global=false
```
in the Dockerfile to allow these Docker-networked client connections.

Only run Mothman on a trusted local machine. Do not expose port 8080 publicly.
