#github.com/thegrayninja

#a set of tools to make my windows life easier

#Current Version: PyWhois 0.1.1
#Changes: exported to csv (|), save to file..and changed the name

#version history
#0.1.0 - the begining


##to install whois (python-whois) on windows:
##cd c:\program files\Python36\Lib\site-packages\
##python .\easy-install.py python-whois

import whois
import sys


def CheckPythonVersion():
    PyVerTuple = sys.version_info[:1]
    if PyVerTuple[0] > 2:
        return 0
    else:
        print("\n\nPlease run Python 3.x or newer\n")
        sys.exit(1)
def WelcomeScreen():
    print("\nPyWhois, the utility to help make Windows more linux like...")
    print("...for those times when you can't escape the M$")
    print("github.com/thegrayninja\n\n")


def PyHelp():
    print("")
    print("<>\tperform basic whois. Example: PyWhois.py operationecho.com")
    print("-e\tto export to csv (|). Example: PyWhois.py operationecho.com -e")
    print("-h\tthis help menu. Example: PyWhois.py -h")
    print("-i\timport a list of domains for whois lookup (column formatted)\n  \tExample: PyWhois.py -i file.txt")
    print("")


def SaveWhoisFile(Data):
    SaveFile = open("WhoisResults.csv", "w")
    SaveFile.write(Data)
    SaveFile.close()
    print("\n\nWhoisResults.csv has been saved to the current directory.")


def ExportCSVHeader():
    Header = "domain_name|registrar|whois_server|updated_date|created_date|expiration_date|name_servers|emails|dnssec|name|org|address|city|state|zipcode|country\n"
    return(Header)


def ExportCSV(WhoisResults):
    Content = "%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s\n" %(WhoisResults.domain_name,WhoisResults.registrar,WhoisResults.whois_server,WhoisResults.updated_date,WhoisResults.created_date,WhoisResults.expiration_date,WhoisResults.name_servers,WhoisResults.emails,WhoisResults.dnssec,WhoisResults.name,WhoisResults.org,WhoisResults.address,WhoisResults.city,WhoisResults.state,WhoisResults.zipcode,WhoisResults.country)
    return(Content)


def PyWhoisSingle(Domain, Export):
    WhoisResults = whois.whois(Domain)
    if Export == "-e":
        Results = ExportCSVHeader()
        Results += ExportCSV(WhoisResults)
        SaveWhoisFile(Results)
    else:
        print(WhoisResults)



def PyWhoisImport(FileName, Export):
    try:
        FileNameContents = open(FileName, "r")
    except:
        print("\nFile does not exist")
        sys.exit(1)
    DomainList = FileNameContents.readlines()
    FileNameContents.close()

    Results = ExportCSVHeader()
    for Domain in DomainList:
        WhoisResults = whois.whois(Domain.strip())
        Results += ExportCSV(WhoisResults)

    if Export == "-e":
        SaveWhoisFile(Results)

    else:
        print(Results)



def main():
    WelcomeScreen()
    CheckPythonVersion()
    try:
        FirstSwitch = sys.argv[1]
    except:
        print("\nInvalid Syntax\n")
        PyHelp()
        sys.exit(1)
    if FirstSwitch[0] != "-":
        #ExportData = ""
        try:
            ExportData = sys.argv[2]
        except:
            ExportData = ""
        PyWhoisSingle(FirstSwitch, ExportData)

    else:
        try:
            FirstSwitchText = sys.argv[2]
        except:
            print("\nInvalid Syntax")
            print(PyHelp())
            sys.exit(1)

    if FirstSwitch == "-i":
        try:
            ExportData = sys.argv[3]
        except:
            ExportData = ""
        PyWhoisImport(FirstSwitchText, ExportData)

    elif FirstSwitch == "-h":
        PyHelp()



if __name__ == main():
    main()

