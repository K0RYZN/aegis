from mitmproxy import http
from colorama import Fore
import random

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
]
# Rotating USERS AGENTS
class Agents:
    def request(self, flow: http.HTTPFlow) -> None:
        """Modify HTTP request headers."""
        flow.request.headers["User-Agent"] = random.choice(USER_AGENTS)
        flow.request.headers["Referer"] = flow.request.pretty_url

addons = [Agents]