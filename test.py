
# import helper.scapy as scapyHelper
import helper.nmap as nmapHelper
import helper.info_pi as infoHelper
import subprocess

if __name__ == "__main__":
    network = "192.168.92.102"
    if network == "None" :
        print("None network")
    else:
        cidr= "/24" # /24	255.255.255.0	254
        ip= "%s%s" %(network, cidr)
        print("ippppppppp", ip)
        data = nmapHelper.scan(ip)
        nmapHelper.display_result(data)
