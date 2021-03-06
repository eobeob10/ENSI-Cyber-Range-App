import scapy.all as scapy
from netaddr import IPNetwork
import netifaces

def scan(ip):
    arp_req_frame = scapy.ARP(pdst = ip)

    broadcast_ether_frame = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    
    broadcast_ether_arp_req_frame = broadcast_ether_frame / arp_req_frame

    answered_list = scapy.srp(broadcast_ether_arp_req_frame, timeout = 1, verbose = False)[0]
    result = []
    for i in range(0,len(answered_list)):
        client_dict = {"ip" : answered_list[i][1].psrc, "mac" : answered_list[i][1].hwsrc}
        result.append(client_dict)

    print(result)
    return result



def network():
    result = []
    netmask = []
    for interface in netifaces.interfaces(): # interate through interfaces: eth0, eth1, wlan0...
        print("interface = ", interface)
        if (interface != "lo") and (interface != "docker0") and (netifaces.AF_INET in netifaces.ifaddresses(interface)): # filter loopback, and active ipv4
            for ip_address in netifaces.ifaddresses(interface)[netifaces.AF_INET]: 
                if (ip_address['addr'] != "127.0.0.1") :          
                    result.append(ip_address['addr'])
                    netmask.append(ip_address['netmask'])

    return (result,netmask)

def scanner():

    result, netmask = network()
    ip_networks = []

    for i in range(len(result)):
        ip_networks.append(str(IPNetwork(result[i]+'/'+netmask[i]).cidr))
    print (ip_networks)

    scanned =[]
    for i in ip_networks :
        scanned+=scan(i)
    print("Scanned successfully")
    return scanned

    