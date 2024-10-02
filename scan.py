from scapy.all import ARP, Ether, srp, wrpcap

def scan_network(target_ip):
    # ARP packet
    arp = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp
    result = srp(packet, timeout=5, verbose=0)[0]
    clients = []

    for sent, received in result:
        clients.append({"ip": received.psrc, "mac": received.hwsrc})

    return clients

def save_to_pcap(clients, filename):
    packets = []
    for client in clients:
        # Constructing ARP request packet
        arp = ARP(pdst=client["ip"], hwdst=client["mac"])
        ether = Ether(dst=client["mac"])
        packet = ether / arp
        packets.append(packet)
    
    # Verify if packets have Ethernet layers
    for packet in packets:
        if not packet.haslayer(Ether):
            print("Warning: Packet missing Ethernet layer")

    # Save packets to pcap file
    if packets:
        wrpcap(filename, packets)
        print(f"Captured packets saved to {filename}")
    else:
        print("No valid packets to save")

def print_scan_results(clients):
    print("Available devices on the network:")
    print("IP" + " "*18 + "MAC")
    print(clients)
    for client in clients:
        print("{:16}     {}".format(client["ip"], client["mac"]))

if __name__ == "__main__":
    target_ip = input("Enter the IP address or subnet to scan (e.g., 192.168.1.0/24): ")

    # Perform network scan
    clients = scan_network(target_ip)

    # Print scan results
    print_scan_results(clients)

    # Prompt the user to input the filename for saving captured packets
    filename = input("Enter the filename to save the captured packets (e.g., network_scan.pcap): ")

    # Save captured packets to the specified filename
    save_to_pcap(clients, filename)
    

