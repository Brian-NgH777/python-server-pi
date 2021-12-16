# import helper.scapy as scapy

# if __name__ == "__main__":
#     network = '192.168.92.102'
#     cidr= "/24" # /24	255.255.255.0	254
#     ip= "%s%s" %(network, cidr)
#     scanned_output = scapy.scan(ip)
#     scapy.display_result(scanned_output)

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("0.0.0.0", 5566))
s.listen(10)

while True:
    conn, addr = s.accept()
    msg = conn.recv(1024)
    str_data = msg.decode("utf8")
    print(str_data)
    conn.send(msg)