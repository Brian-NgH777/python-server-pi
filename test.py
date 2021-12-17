
import helper.scapy as scapyHelper
import subprocess

if __name__ == "__main__":
    network = subprocess.call(["hostname","-I"])
    print("networknetworknetwork", network)
    cidr= "/24" # /24	255.255.255.0	254
    ip= "%s%s" %(network, cidr)
    print("ippppppppp", ip)
    data = scapyHelper.scan(ip)
    scapyHelper.display_result(data)
