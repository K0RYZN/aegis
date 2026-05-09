from mitmproxy import http
from logo import logo
from Blacklister import Blacklister
from colorama import Fore, Style

class Loader: # Start and end of the proxy
    def load(self, loader):
            logo()
            print(f"{Style.BRIGHT}{Fore.MAGENTA}THE MOTHMAN is ACTIVE{Fore.RESET}{Style.RESET_ALL}")
    def done(self):
         print(f'\n{Style.BRIGHT}{Fore.MAGENTA}THE MOTHMAN is INACTIVE {Fore.RESET}{Style.RESET_ALL}')


addons = [
    Loader(),
    Blacklister()
]
