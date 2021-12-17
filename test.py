
import helper.scapy as scapyHelper
import helper.info_pi as infoHelper
import subprocess

if __name__ == "__main__":
    network = infoHelper.networkInformation()
    if len(network) == 0 :
        print("Not newwork")
    else:
        cidr= "/24" # /24	255.255.255.0	254
        ip= "%s%s" %(network, cidr)
        print("ippppppppp", ip)
        data = scapyHelper.scan(ip)
        scapyHelper.display_result(data)
