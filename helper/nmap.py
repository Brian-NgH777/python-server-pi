import sys, nmap
import urllib.request as req
import helper.info_pi as infoHelper

 def scan(ip):
    nm = nmap.PortScanner()
    nm.scan(hosts=ip, arguments='-sP -PR') #  -PR

    lHosts=[]
    for ip in nm.all_hosts():
        print("all_hostsall_hostsall_hosts", ip)
        host = nm[ip]
        mac = "-"
        vendorName = "-"
        if 'mac' in host['addresses']:
            mac = host['addresses']['mac']
            if mac in host['vendor']:
                vendorName = host['vendor'][mac]

        status = host['status']['state']
        rHost = {'ip': ip, 'mac': mac, 'vendor': vendorName, 'status': status}
        
        lHosts.append(rHost)
    
    return lHosts

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

def new():
    network = infoHelper.networkInformation()
    if network == "None" :
        print("None network")
        sys.exit(0)
    else:
        cidr= "/24" # /24	255.255.255.0	254
        ip= "%s%s" %(network, cidr)
        print("ippppppppp", ip)
        data = scan(ip)
        display_result(data)
        return data