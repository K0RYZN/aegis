from mitmproxy import http

class BlockJS:
    def request(self, flow: http.HTTPFlow) -> None:
        """Intercept and block JavaScript requests."""
        if flow.request.pretty_url.endswith(".js"):
            flow.response = http.Response.make(
                403,  # HTTP Forbidden
                b"",  # Empty response
                {"Content-Type": "text/plain"},
            )

# Register the addon
addons = [BlockJS()]
