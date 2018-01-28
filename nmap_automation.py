# automate scan tools

import re
import time, sys, os
import subprocess, platform



# TODO Import file containing IP Addresses
# TODO Run set of commands per IP Address
# TODO Create Folder based on IP Address
# TODO Create subfolder based on Tool used
# TODO Determine Open Ports


def main():
    #CheckPythonVersion()
    FileNameIPAddress = "ipaddress.txt"
    IPAddresses = GetIPAddressesFromFile(FileNameIPAddress)
    for IP in IPAddresses:
        CommandList(IP.strip())



####
####
#Get Host Information

#TODO Current code to run shell command from python fails in v3.x
def CheckPythonVersion():
    PyVerTuple = sys.version_info[:1]
    if PyVerTuple[0] > 2:
        return 0
    else:
        print("\n\nPlease run Python 3.x or newer\n")
        sys.exit(1)

def GetOSVersion():
    return (platform.system())

#####
#####


####
####
#Admin Work

def SaveDataToFile(Data, FileName):
    SaveFile = open(FileName, "w")
    SaveFile.write(str(Data))
    SaveFile.close()
    print("file has been saved")


def CreateIPFolder(IPAddress):
    print("...Creating a working directory...")
    OSVersion = GetOSVersion()
    if "Windows" in OSVersion:
        ##TODO For Windows --doesn't work
        SaveFolder = r'.\%s' % IPAddress
        if not os.path.exists(SaveFolder):
            os.makedirs(SaveFolder)
            print("Folder .\%s has been created!" % IPAddress)

    else:
        ##TODO For Linux
        SaveFolder = './%s' % IPAddress
        if not os.path.exists(SaveFolder):
            os.makedirs(SaveFolder)
            print("Folder ./%s has been created!" % IPAddress)

def CreateToolFolder():
    print("based on commands")

####
####



####
####
#Initial Recon

def GetIPAddressesFromFile(FileNameIPAddress):
    print("...Getting IP Address from file...")
    IPAddressList = []
    TempFile = open(FileNameIPAddress, 'r')
    IPAddressList.append(TempFile.read())
    TempFile.close()
    return (IPAddressList)

def DetermineOpenPorts(IPAddress):
    print("...Running initial nmap scan against %s..." % IPAddress)
    NmapCommand = "nmap -Pn -p 80,443,22 %s" % IPAddress
    NmapResults = subprocess.check_output((NmapCommand), shell=True)
    FileName = "./%s/OpenPorts_%s.txt" % (IPAddress, IPAddress)
    SaveDataToFile(NmapResults.strip(), FileName)
    print("...Initial nmap scan is complete.")
    return FileName



def GetOpenPorts(FileName):
    print("...Trying to determine open ports...")
    FirstTerm = "open"
    SecondTerm = "^\d*"
    OpenPorts = []

    for line in open(FileName, 'r'):
        if re.search(FirstTerm, line):
            x = (re.search(SecondTerm, line).group(0))
            if x != "":
                OpenPorts.append(x)
    print("Open Ports: "),
    print(OpenPorts)
    return OpenPorts
####
####


####
####
#Tools to run

def CommandList(IPAddress):
    print("...Scanning against %s has started. Please be patient." % IPAddress)
    CreateIPFolder(IPAddress)
    FileName = DetermineOpenPorts(IPAddress)
    OpenPorts = GetOpenPorts(FileName)
    NmapScans(IPAddress, OpenPorts)

    print("...Scanning for %s has completed." % IPAddress)

def NmapScans(IPAddress, OpenPorts):
    NmapFolderName = IPAddress + "/nmap"
    CreateIPFolder(NmapFolderName)
    WebPorts = ['80', '8080', '8888', '8181', '443', '8443']
    SSLPorts = ['443', '8443']
    MailPorts = ['25', '110']
    RDP = ['3389']
    NmapResults = "Nmap Scans initiated at " + time.strftime('%X %x %Z') + "\n\n"

    NmapPortScans = ["nmap -A -O -Pn "]
    NmapDiscoveryScans = ["nmap -Pn -sP --script discovery "]

    NmapWebScans = ["nmap -Pn --script http-apache-negotiation ", "nmap -Pn --script http-apache-server-status ",
                    "nmap -Pn --script http-cookie-flags ",
                    "nmap -Pn --script http-cors ", "nmap -Pn --script http-cross-domain-policy ",
                    "nmap -Pn --script http-enum ",
                    "nmap -Pn --script http-headers ", "nmap -Pn --script http-php-version ",
                    "nmap -Pn --script http-robots.txt ",
                    "nmap -Pn --script http-security-headers ", "nmap -Pn --script snmp-info "]

    NmapSSLScans = ["nmap -Pn --script ssl-enum-ciphers ", "nmap -Pn --script ssl-cert ", "nmap -Pn --script sslv2 ",
                    "nmap --script ssl-heartbleed ", "nmap -Pn --script http-shellshock "]


    for Scan in NmapPortScans:
        for Port in OpenPorts:
            ScanCommand = Scan + "-p " + Port + " " + IPAddress
            print("Performing %s. Please be patient..." % ScanCommand)
            try:
                NmapResults += ScanCommand + " is initiating at " + time.strftime('%X %x %Z')
                NmapResults += (subprocess.check_output((ScanCommand), shell=True)).strip()
                NmapResults += "\n\n####################\n\n####################\n\n"
            except:
                print("%s FAILED!! Reasons unknown." % ScanCommand)

    for Scan in NmapDiscoveryScans:
        ScanCommand = Scan + IPAddress
        print("Performing %s. Please be patient..." % ScanCommand)
        try:
            NmapResults += ScanCommand + " is initiating at " + time.strftime('%X %x %Z') + "\n"
            NmapResults += (subprocess.check_output((ScanCommand), shell=True)).strip()
            NmapResults += "\n\n####################\n\n####################\n\n"
        except:
            print("%s FAILED!! Reasons unknown." % ScanCommand)

    for Port in SSLPorts:
        for OPort in OpenPorts:
            if Port == OPort:
                for Scan in NmapSSLScans:
                    ScanCommand = Scan + "-p " + Port + " " + IPAddress
                    print("Performing %s. Please be patient..." % ScanCommand)
                    try:
                        NmapResults += ScanCommand + " is initiating at " + time.strftime('%X %x %Z') + "\n"
                        NmapResults += (subprocess.check_output((ScanCommand), shell=True)).strip()
                        NmapResults += "\n\n####################\n\n####################\n\n"
                    except:
                        print("%s FAILED!! Reasons unknown." % ScanCommand)

    #print(NmapResults)
    NmapFileName = NmapFolderName + "/nmap_results_%s.txt" % IPAddress
    SaveDataToFile(NmapResults, NmapFileName)

####
####



if __name__ == main():
    main()
