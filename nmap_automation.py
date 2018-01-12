#nmap scanning automation tool

#goal is to segment types of scans based on open ports. This intelligence
#has not been coded as of yet....


import os
import subprocess
import sys

import time


IPAddress = sys.argv[1]
NmapResults = ""
NmapWebScanStatus = False
NmapSSLScanStatus = False

WebOnlyScanPortsList = ["80", "8080", "8081", "8181"]
WebScanPortsList = ["80", "8080", "8081", "8181", "443", "4443"]
SSLScanPortsList = ["443", "4443"]


WebPorts = "-p 80,8080,8081,8181,443,4443 "
WebOnlyPorts = "-p 80,8080,8081,8181 "
SSLPorts = "-p 443,4443 "

ResultsFullBreak = "\n\n\n" + "*" * 20 + "\n" + "*" * 20 + "\n\n"
ResultsHeaderBreak = "\n\n" + "*" * 20 + "\n"

OpenPorts = []

NmapResults += "Scans initiated at " + time.strftime('%X %x %Z') + "\n\n"

NmapScans = ["nmap -A -O -PN ", "nmap -Pn -sP --script discovery ", "nmap -p 443 --script ssl-heartbleed ", "nmap -Pn --script http-shellshock "]

NmapWebScans = ["nmap -Pn --script http-apache-negotiation ", "nmap -Pn --script http-apache-server-status ", "nmap -Pn --script http-cookie-flags ",
                "nmap -Pn --script http-cors ", "nmap -Pn --script http-cross-domain-policy ", "nmap -Pn --script http-enum ",
                "nmap -Pn --script http-headers ", "nmap -Pn --script http-php-version ", "nmap -Pn --script http-robots.txt ",
                "nmap -Pn --script http-security-headers ", "nmap -Pn --script snmp-info "]

NmapSSLScans = ["nmap -Pn --script ssl-enum-ciphers ", "nmap -Pn --script ssl-cert ", "nmap -Pn --script sslv2 "]



for i in WebOnlyScanPortsList:
    GrepCut = " | grep -w " + i + "/tcp"# | cut -d' ' -f3"
    OpenPortCheck = (subprocess.check_output(("nmap -Pn " + WebOnlyPorts + IPAddress + GrepCut), shell=True)).strip()
    if " open " in OpenPortCheck:
        print("Port " + i + " is open!")
        OpenPorts.append(i)
        NmapWebScanStatus = True
    else:
        print("Port " + i + " is closed/filtered/unknown.")


for i in SSLScanPortsList:
    GrepCut = " | grep -w " + i + "/tcp"# | cut -d' ' -f3"
    OpenPortCheck = (subprocess.check_output(("nmap -Pn " + SSLPorts + IPAddress), shell=True)).strip()
    if "open" in OpenPortCheck:
        print("Port " + i + " is open!")
        OpenPorts.append(i)
        NmapSSLScanStatus = True
    else:
        print("Port " + i + " is closed/filtered/unknown.")

print("\n\n")


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



if NmapWebScanStatus == True:
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

if NmapSSLScanStatus == True:
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

print(OpenPorts)
