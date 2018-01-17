##let's see if this works

import csv
import sys


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

    #csvfile.close()
    return(Platforms)

def ModifyReport2(old_report,Platforms):
    with open(old_report, 'r') as csvfile:
        delimfile = csv.DictReader(csvfile)
        for row in delimfile:
            RowValue = row['IP']
            PlatformName = row['Application']
            if PlatformName in Platforms.keys():
                Platforms[PlatformName]["assets"].append(RowValue)
            else:
                Platforms[PlatformName] = {"assets":[RowValue]}

    #csvfile.close()
    return(Platforms)


def SaveIP(PlatformData):
    for key in PlatformData:
        FileName = ".\Docs\Assets\master\\" + key + ".txt"
        x = PlatformData[key]['assets']
        y = ""
        for i in x:
            y += i + "\n"
        print(y)
        with open(FileName, 'w') as NewFile:
            NewFile.write(str(y))
        if NewFile.closed:
            print("file is closed")
        else:
            print("whatever, yo")

def main():

    LinuxData = ModifyReport(".\Docs\LinuxServers2017.csv")
    SaveIP(ModifyReport2(".\Docs\WindowsServers2018.csv",LinuxData))


if __name__ == main():
    main()


print("\n\nall done.")
