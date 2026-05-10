from logo import logo
from Blacklister import Blacklister
from Stats import MothmanStats
from colorama import Fore, Style

stats = MothmanStats()


class Loader:
    def load(self, loader):
        logo()
        print(f"{Style.BRIGHT}{Fore.MAGENTA}THE MOTHMAN is ACTIVE{Fore.RESET}{Style.RESET_ALL}")

    def done(self):
        print(f'\n{Style.BRIGHT}{Fore.MAGENTA}THE MOTHMAN is INACTIVE {Fore.RESET}{Style.RESET_ALL}')
        stats.print_summary()


addons = [
    Loader(),
    Blacklister(stats),
]
