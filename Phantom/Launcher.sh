tor
sudo systemctl enable tor
sudo systemctl start tor

proxychains4 mitmdump --listen-port 8080 --set upstream_proxy=socks5://127.0.0.1:9050 -s /home/redfield/Documents/Projects_CS/Phantom/Main.py


#sudo nano /etc/proxychains.conf
#Proxychains - by using its configuration file, I can confgiure it to strictly bring traffic through TOR.

#strict_chain
#proxy_dns 
#tcp_read_time_out 15000
#tcp_connect_time_out 8000

#[ProxyList]
#socks5 127.0.0.1 9050

