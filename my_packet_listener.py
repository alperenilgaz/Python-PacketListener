import scapy.all as scapy
from scapy_http import http

def listened_packet(interface):
    scapy.sniff(iface=interface,store=False,prn=analyzed_packet)
    #prn=callback function

def analyzed_packet(packet):
    #packet.show()
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            print(packet[scapy.Raw].load)

listened_packet("eth0")