
import helper.scapy as scapyHelper
import subprocess

if __name__ == "__main__":
    cmd = "hostname -I"
    network = subprocess.run(cmd, shell=True)
    cidr= "/24" # /24	255.255.255.0	254
    ip= "%s%s" %(network, cidr)
    print("ippppppppp", ip)
    data = scapyHelper.scan(ip)
    scapyHelper.display_result(data)
