# automate tools


import re
import time, sys, os
import subprocess, platform


def GetOpenPorts(FileName):
    FirstTerm = "open"
    SecondTerm = "^\d*"

    for line in open(FileName, 'r'):
        if re.search(FirstTerm, line):
            x = (re.search(SecondTerm, line).group(0))
            if x != "":
                print(x)


# TODO Import file containing IP Addresses
# TODO Run set of commands per IP Address
# TODO Create Folder based on IP Address
# TODO Create subfolder based on Tool used
# TODO Determine Open Ports


def CheckPythonVersion():
    PyVerTuple = sys.version_info[:1]
    if PyVerTuple[0] > 2:
        return 0
    else:
        print("\n\nPlease run Python 3.x or newer\n")
        sys.exit(1)


def GetOSVersion():
    return (platform.system())

def SaveDataToFile(Data, FileName):
    SaveFile = open(FileName, "w")
    SaveFile.write(str(Data))
    SaveFile.close()
    print("file has been saved")

def CreateIPFolder(IPAddress):
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


def NmapScans():
    print('in progress')


def GetIPAddressesFromFile(FileNameIPAddress):
    # print("in progress")
    IPAddressList = []
    TempFile = open(FileNameIPAddress, 'r')
    IPAddressList.append(TempFile.read())
    TempFile.close()
    return (IPAddressList)


def CommandList(IPAddress):
    print("in progress")
    CreateIPFolder(IPAddress)
    DetermineOpenPorts(IPAddress)


def CreateToolFolder():
    print("based on commands")


def DetermineOpenPorts(IPAddress):
    print("in progress - Determine Open Ports against %s" % IPAddress)
    NmapCommand = "nmap -Pn -p 80,443,22 %s" % IPAddress
    NmapResults = subprocess.check_output((NmapCommand), shell=True)
    FileName = "./%s/nmap_%s.txt" % (IPAddress, IPAddress)
    SaveDataToFile(NmapResults.strip(), FileName)
    OpenPorts = GetOpenPorts(FileName)


def main():
    #CheckPythonVersion()
    FileNameIPAddress = "ipaddress.txt"  # input("Please enter the file name that contains the hosts/IPs: ")
    # print(FileNameIPAddress)
    IPAddresses = GetIPAddressesFromFile(FileNameIPAddress)
    for IP in IPAddresses:
        CommandList(IP.strip())


if __name__ == main():
    main()
