
import helper.scapy as scapyHelper
import subprocess

if __name__ == "__main__":
    cidr= "/24" # /24	255.255.255.0	254
    ip= "%s%s" %(subprocess.call(["hostname","-I"]), cidr)
    print("ippppppppp", ip)
    data = scapyHelper.scan(ip)
    scapyHelper.display_result(data)
