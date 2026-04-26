from mitmproxy import http
from logo import logo
from Filter import Blacklister
from colorama import Fore, Style
from Rotator import Agents
from JS_blocker import BlockJS

class Loader: # Start and end of the proxy
    def load(self, loader):
            logo()
            print(f"{Style.BRIGHT}{Fore.MAGENTA}THE PHANTOM is ACTIVE{Fore.RESET}{Style.RESET_ALL}")
    def done(self):
         print(f'\n{Style.BRIGHT}{Fore.MAGENTA}THE PHANTOM is INACTIVE {Fore.RESET}{Style.RESET_ALL}')

         #add script to turn off TOR service


addons = [
    Loader(),
    Blacklister(),
    Agents(),
    BlockJS()
]