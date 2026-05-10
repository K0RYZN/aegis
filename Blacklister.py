from mitmproxy import http
from Blacklist import BLOCK_DOMAINS
from colorama import Fore

BLOCK_SET = {d.lower().strip().lstrip(".") for d in BLOCK_DOMAINS}


def host_matches(host: str, domain: str) -> bool:
    host = host.lower().strip(".")
    domain = domain.lower().strip().lstrip(".")
    return host == domain or host.endswith("." + domain)


def is_blocked(host: str) -> bool:
    return any(host_matches(host, d) for d in BLOCK_SET)


class Blacklister:
    def __init__(self, stats=None):
        self.stats = stats

    def request(self, flow: http.HTTPFlow) -> None:
        host = flow.request.host or ""

        if is_blocked(host):
            if self.stats:
                self.stats.record_blocked(host)

            flow.response = http.Response.make(
                403,
                b"\nBLOCKED BY THE MOTHMAN\n",
                {"Content-Type": "text/plain"}
            )

            print(f"{Fore.RED}BLOCKED HOST: {host} | URL: {flow.request.pretty_url}{Fore.RESET}")
            return

        if self.stats:
            self.stats.record_allowed()from mitmproxy import http
from Blacklist import BLOCK_DOMAINS
from colorama import Fore

BLOCK_SET = {d.lower().strip().lstrip(".") for d in BLOCK_DOMAINS}

def host_matches(host: str, domain: str) -> bool:
    host = host.lower().strip(".")
    domain = domain.lower().strip().lstrip(".")
    return host == domain or host.endswith("." + domain)

def is_blocked(host: str) -> bool:
    return any(host_matches(host, d) for d in BLOCK_SET)

class Blacklister:
    def request(self, flow: http.HTTPFlow) -> None:
        host = flow.request.host or ""

        if is_blocked(host):
            flow.response = http.Response.make(
                403,
                b"\nBLOCKED BY THE MOTHMAN\n",
                {"Content-Type": "text/plain"}
            )
            print(f"{Fore.RED}BLOCKED HOST: {host} | URL: {flow.request.pretty_url}{Fore.RESET}")

addons = [Blacklister()]
