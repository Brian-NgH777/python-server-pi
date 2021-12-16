import helper.scapy as scapy

if __name__ == "__main__":
    network = '192.168.2.9'
    cidr= "/24" # /24	255.255.255.0	254
    ip= "%s%s" %(network, cidr)
    scanned_output = scapy.scan(ip)
    scapy.display_result(scanned_output)