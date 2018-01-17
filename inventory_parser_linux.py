##let's see if this works

import csv
import sys

try:
    UserSwitch = sys.argv[1]
except:
    UserSwitch = ""

def ModifyReport(old_report):
    Platforms = {}
    with open(old_report, 'r') as csvfile:
        delimfile = csv.DictReader(csvfile)
        for row in delimfile:
            RowValue = row['IP address']
            PlatformName = row['Platform']
            if PlatformName in Platforms.keys():
                Platforms[PlatformName]["assets"].append(RowValue)
            else:
                Platforms[PlatformName] = {"assets":[RowValue]}

    csvfile.close()
    return(Platforms)

def SaveIP(PlatformData):
    for i in PlatformData:
        FileName = ".\Docs\Assets\Linux\\" + i + ".txt"
        x = PlatformData[i]['assets']
        y = ""
        for i in x:
            y += i + "\n"
        print(y)
        with open(FileName, 'w') as NewFile:
            NewFile.write(str(y))
        NewFile.close()

def SaveAssetInfo(PlatformData):
    for i in PlatformData:
        print("\n\n\n\n")
        FileName = ".\Docs\Assets\Linux\\" + i + ".json"
        print(FileName)
        x = PlatformData[i]
        with open(FileName, 'w') as NewFile:
            NewFile.write(str(x))
        NewFile.close()


def HelpMenu():
    print("\n")
    print("too many snakes on the plane\n\n")
    print("  -i          save IP Addresses only to .txt file")
    print("  -a          save all asset info to .json file")
    print("\n\n")
    sys.exit(0)

def main():
    ReportName = ".\Docs\LinuxServers2017.csv"
    if UserSwitch == "-i":
        SaveIP(ModifyReport(ReportName))
    elif UserSwitch == "-a":
        SaveAssetInfo(ModifyReport(ReportName))
    else:
        HelpMenu()

if __name__ == main():
    main()


print("\n\nall done.")
