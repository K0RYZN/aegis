from logo import logo
from Blacklister import Blacklister
from Stats import AEGISStats
from colorama import Fore, Style

stats = AEGISStats()


class Loader:
    def load(self, loader):
        logo()
        print(f"{Style.BRIGHT}{Fore.MAGENTA}AEGIS is ACTIVE{Fore.RESET}{Style.RESET_ALL}")

    def done(self):
        print(f'\n{Style.BRIGHT}{Fore.MAGENTA}AEGIS is INACTIVE {Fore.RESET}{Style.RESET_ALL}')
        stats.print_summary()


addons = [
    Loader(),
    Blacklister(stats),
]
