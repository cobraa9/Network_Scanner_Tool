from scapy.all import sniff

def packet_callback(packet):
    print(packet.show())
    
sniff(count=10,prn=packet_callback)



