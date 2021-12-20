import sys
from scapy.all import ARP,Ether,srp
import urllib.request as req
import argparse
import helper.info_pi as infoHelper
import subprocess

# def get_args():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('-t', '--target', dest='target', help='Target IP Address/Adresses')
#     options = parser.parse_args()

#     #Check for errors i.e if the user does not specify the target IP Address
#     #Quit the program if the argument is missing
#     #While quitting also display an error message
#     if not options.target:
#         #Code to handle if interface is not specified
#         parser.error("[-] Please specify an IP Address or Addresses, use --help for more info.")
#     return options
  
def scan(ip):
    arp_req_frame = ARP(pdst = ip)
    broadcast_ether_frame = Ether(dst = "ff:ff:ff:ff:ff:ff")
    
    broadcast_ether_arp_req_frame = broadcast_ether_frame / arp_req_frame

    answered_list = srp(broadcast_ether_arp_req_frame, timeout = 1, verbose = False)[0]
    result = []
    for i in range(0,len(answered_list)):
        client_dict = {"ip" : answered_list[i][1].psrc, "mac" : answered_list[i][1].hwsrc, "vendor": resolveMac(answered_list[i][1].hwsrc)}
        result.append(client_dict)

    return result

def resolveMac(mac):
    try:
        url = "http://macvendors.co/api/vendorname/"
        request = req.Request(url + mac, headers={'User-Agent': "API Browser"})
        response = req.urlopen(request)
        vendor = response.read()
        vendor = vendor.decode("utf-8")
        vendor = vendor[:25]
        return vendor
    except:
        return "N/A"
  
def display_result(result):
    print("-----------------------------------\nIP Address\tMAC Address\tVendor\n-----------------------------------")
    for i in result:
        print("{}\t{}\t{}".format(i["ip"], i["mac"], i["vendor"]))

def permissionRoot():
    subprocess.check_output("sudo su -", shell=True).decode("utf-8")


def new():
    network = infoHelper.networkInformation()
    if network == "None" :
        print("None network")
        sys.exit(0)
    else:
        # change permission Root not pi 
        permissionRoot()
        # Scaner
        cidr= "/24" # /24	255.255.255.0	254
        ip= "%s%s" %(network, cidr)
        print("ippppppppp", ip)
        data = scan(ip)
        display_result(data)
        return data