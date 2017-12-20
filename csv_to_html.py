DocContents = []
import csv
with open('.\Docs\workbook3.csv', 'rt', encoding='utf8') as csvfile:
    CSVData = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in CSVData:
        DocContents.append(row)




Count = 0
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
            Prefix = '<div id="level1tab"><a href=test.html#%s>' % (Words[0])
            Suffix = '<a href=test.html#%s></div>' % (Words[0])
        elif DotCount == 2:
            Prefix = '<div id="level2tab"><a href=test.html#%s>' % (Words[0])
            Suffix = '<a href=test.html#%s></div>' % (Words[0])

        else:
            Prefix = ""
            Suffix = "<br>"

    print(Prefix + Words[0] + " - " + " ".join(Words[1:5]) + "..." + Suffix)

    Count += 1
