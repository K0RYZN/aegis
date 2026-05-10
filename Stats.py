import time
from collections import Counter
from colorama import Fore, Style


class MothmanStats:
    def __init__(self):
        self.started_at = time.time()
        self.total_requests = 0
        self.blocked_requests = 0
        self.allowed_requests = 0
        self.blocked_domains = Counter()

    def record_allowed(self):
        self.total_requests += 1
        self.allowed_requests += 1

    def record_blocked(self, host: str):
        self.total_requests += 1
        self.blocked_requests += 1
        self.blocked_domains[host] += 1

    def uptime_seconds(self) -> int:
        return int(time.time() - self.started_at)

    def format_uptime(self) -> str:
        seconds = self.uptime_seconds()
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        secs = seconds % 60
        return f"{hours:02}:{minutes:02}:{secs:02}"

    def block_rate(self) -> float:
        if self.total_requests == 0:
            return 0.0
        return (self.blocked_requests / self.total_requests) * 100

    def top_blocked(self, limit: int = 5):
        return self.blocked_domains.most_common(limit)

    def print_summary(self):
        print(f"\n{Style.BRIGHT}{Fore.MAGENTA}MOTHMAN STATS{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Uptime:{Fore.RESET} {self.format_uptime()}")
        print(f"{Fore.CYAN}Total Requests Seen:{Fore.RESET} {self.total_requests}")
        print(f"{Fore.RED}Blocked Requests:{Fore.RESET} {self.blocked_requests}")
        print(f"{Fore.GREEN}Allowed Requests:{Fore.RESET} {self.allowed_requests}")
        print(f"{Fore.YELLOW}Block Rate:{Fore.RESET} {self.block_rate():.2f}%")

        top_domains = self.top_blocked()

        if top_domains:
            print(f"\n{Fore.RED}Top Blocked Domains:{Fore.RESET}")
            for domain, count in top_domains:
                print(f"  {domain} - {count}")
        else:
            print(f"\n{Fore.YELLOW}No blocked domains yet.{Fore.RESET}")

        print()
