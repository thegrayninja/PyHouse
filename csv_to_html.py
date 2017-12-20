DocContents = []
import csv
#if encoding is required, replace with this line:
#with open('.\\files\workbook2.csv', 'rt', encoding='utf8') as csvfile:
with open('.\\files\workbook2.csv', 'rt') as csvfile:
    CSVData = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in CSVData:
        DocContents.append(row)




Count = 0
ToC = ""
Content = ""
for row in DocContents:
    Word = ""
    for i in DocContents[Count][0]:
        Word += i
        Words = Word.split()


    for a in "a":
        DotCount = 0
        for i in Words[0]:
            if i == ".":
                DotCount += 1
        if DotCount == 1:
            Prefix = '<div id="level1tab"><a href=audit_helper.html#%s>' % (Words[0])
            Suffix = '</a></div>'
        elif DotCount == 2:
            Prefix = '<div id="level2tab"><a href=audit_helper.html#%s>' % (Words[0])
            Suffix = '</a></div>'
        elif DotCount == 3:
            Prefix = '<div id="level3tab"><a href=audit_helper.html#%s>' % (Words[0])
            Suffix = '</a></div>'

        else:
            Prefix = "<br><br>"
            Suffix = "<br>"
        try:
            Content += "<p id=%s>" % (Words[0]) + DocContents[Count][0] + "</p></ br> </ br>\n"
        except:
            Content += "\n"

    ToC += Prefix + Words[0] + " - " + " ".join(Words[1:5]) + "..." + Suffix + "\n"
    Count += 1
WebContent = ""
WebContent += '<html><head><title>Prioritized Approach to Stuff</title><link rel="stylesheet" href="basic.css" type="text/css" /> </head>'
WebContent += "<body>"
WebContent += ToC
WebContent += "\n\n"
WebContent += Content
WebContent += "</body></html>"

PageHTML = open(".\\files\\audit_helper.html", "w")
PageHTML.write(WebContent)
PageHTML.close()
