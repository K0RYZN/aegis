from mitmproxy import http
from BLACKLIST import Blacklist, WHITELIST
from urllib.parse import urlparse
from colorama import Fore
import random

class Blacklister:
    def request(self, flow: http.HTTPFlow) -> None:
        for domain in Blacklist:
            if domain in flow.request.pretty_url:
                flow.response = http.Response.make(
                    403,
                    b"\nBLOCKED BY PHANTOM\n",
                    {"Content-Type": "text/plain"}
                )
                print(f"{Fore.RED}BLOCKED: {flow.request.pretty_url}{Fore.RESET}")
                return
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
] # 5/30/25 I have no idea if USER_AGENTS is even doing anything, I alrady have the rotator so ill just check up on it later



addons = [
          Blacklister(),
          ]


