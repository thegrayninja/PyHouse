#nmap scanning automation tool

#goal is to segment types of scans based on open ports. This intelligence
#has not been coded as of yet....


import os
import subprocess
import sys

import time


#IPAddress = "10.1.110.171"
IPAddress = sys.argv[1]
NmapResults = ""
ResultsFullBreak = "\n\n\n" + "*" * 20 + "\n" + "*" * 20 + "\n\n"
ResultsHeaderBreak = "\n\n" + "*" * 20 + "\n"
Port80Status = False
Port443Status = False
Port21Status = False
Port22Status = False

WebPorts = "-p 80,8080,8081,8181,443,4443 "
SSLPorts = "-p 443,4443 "

NmapResults += "Scans initiated at " + time.strftime('%X %x %Z') + "\n\n"

NmapScans = ["nmap -A -O -PN ", "nmap -Pn -sP --script discovery ", "nmap -p 443 --script ssl-heartbleed ", "nmap -Pn --script http-shellshock "]

NmapWebScans = ["nmap -Pn --script http-apache-negotiation ", "nmap -Pn --script http-apache-server-status ", "nmap -Pn --script http-cookie-flags ",
                "nmap -Pn --script http-cors ", "nmap -Pn --script http-cross-domain-policy ", "nmap -Pn --script http-enum ",
                "nmap -Pn --script http-headers ", "nmap -Pn --script http-php-version ", "nmap -Pn --script http-robots.txt ",
                "nmap -Pn --script http-security-headers ", "nmap -Pn --script snmp-info "]

NmapSSLScans = ["nmap -Pn --script ssl-enum-ciphers ", "nmap -Pn --script ssl-cert ", "nmap -Pn --script sslv2 "]


for i in NmapScans:
    try:
        print("Running scan: " + i + IPAddress)
        NmapResults += ResultsFullBreak
        NmapResults += i + IPAddress
        NmapResults += ResultsHeaderBreak
        NmapResults += subprocess.check_output((i + IPAddress), shell=True)

    except:
        NmapResults += ResultsFullBreak
        NmapResults += "Failed scan: " + i + IPAddress
        NmapResults += ResultsHeaderBreak
        print("Failed scan: " + i + IPAddress)
        print("Try running as root.")


for i in NmapWebScans:
    PortAndIP = i + WebPorts + IPAddress
    try:
        print("Running scan: " + PortAndIP)
        NmapResults += ResultsFullBreak
        NmapResults += PortAndIP
        NmapResults += ResultsHeaderBreak
        NmapResults += subprocess.check_output((PortAndIP), shell=True)

    except:
        NmapResults += ResultsFullBreak
        NmapResults += "Failed scan: " + PortAndIP
        NmapResults += ResultsHeaderBreak
        print("Failed scan: " + PortAndIP)
        print("Try running as root.")


for i in NmapSSLScans:
    SSLPortAndIP = i + SSLPorts + IPAddress
    try:
        print("Running scan: " + SSLPortAndIP)
        NmapResults += ResultsFullBreak
        NmapResults += SSLPortAndIP
        NmapResults += ResultsHeaderBreak
        NmapResults += subprocess.check_output((SSLPortAndIP), shell=True)

    except:
        NmapResults += ResultsFullBreak
        NmapResults += "Failed scan: " + SSLPortAndIP
        NmapResults += ResultsHeaderBreak
        print("Failed scan: " + SSLPortAndIP)
        print("Try running as root.")

print(NmapResults)

FileName = "NmapScan_" + IPAddress + ".txt"
SaveFile = open(FileName, "w")
SaveFile.write(NmapResults)
SaveFile.close()
