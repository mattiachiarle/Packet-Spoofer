import sys

from scapy.all import *


def send_packet(src_ip, dst_ip, dst_port, payload):
    if sys.getsizeof(payload) > 150:  # if payload size is higher than 150 B we quit
        print("ERROR: payload size should be < 150 B")
        return
    send(IP(src=src_ip,dst=dst_ip)/UDP(dport=dst_port)/Raw(load=payload))  # We send a packet with spoofed source ip, destination ip, destination port and payload

send_packet("10.0.0.151","10.0.0.12",80,"Test")
