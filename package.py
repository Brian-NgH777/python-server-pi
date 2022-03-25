import socket 
from scapy.all import *


def arp_scan(ip):
    request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip)

    ans, unans = srp(request, timeout=2, retry=1)
    result = []
    print("ansansans", ans)
    for sent, received in ans:
        result.append({'IP': received.psrc, 'MAC': received.hwsrc})

    return result


def tcp_scan(ip, ports):
    """
    Performs a TCP scan by sending SYN packets to <ports>.
    Args:
        ip (str): An IP address or hostname to target.
        ports (list or tuple of int): A list or tuple of ports to scan.
    Returns:
        A list of ports that are open.
    """
    try:
        syn = IP(dst=ip) / TCP(dport=ports, flags="S")
    except socket.gaierror:
        raise ValueError('Hostname {} could not be resolved.'.format(ip))

    ans, unans = sr(syn, timeout=2, retry=1)
    result = []

    for sent, received in ans:
        if received[TCP].flags == "SA":
            result.append(received[TCP].sport)

    return result


def main():
    Scanner = 'ARP'
    hostname=socket.gethostname()   
    IPAddr=socket.gethostbyname(hostname) 
    # if Scanner == 'ARP':
    result = arp_scan(IPAddr)
    print("IPAddrIPAddr", result)
    for mapping in result:
        print('{} ==> {}'.format(mapping['IP'], mapping['MAC']))

    # elif Scanner == 'TCP':
    #     if args.range:
    #         ports = tuple(args.ports)
    #     else:
    #         ports = args.ports
        
    #     try:
    #         result = tcp_scan(args.IP, ports)
    #     except ValueError as error:
    #         print(error)
    #         exit(1)

    #     for port in result:
    #         print('Port {} is open.'.format(port))


if __name__ == '__main__':
    main()