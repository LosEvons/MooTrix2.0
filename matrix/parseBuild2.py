#imports
import csv
import string
import re
from collections import Counter
import unicodedata

sv = open('sv.txt', 'r', encoding="utf-8")
svRead = sv.read()
svRead = svRead.lower()
print("Total characters in file:")
print(len(svRead))

#variables
svParsed = "svparsed is empty"
svTF = "svTF is empty"
cnt = Counter()
OrdCnt = Counter()

#cleanup
svParsed = ""
svTF = ""
exceptionList = ["@", ",", ".", "!", ":", ";","-", "?", "»", "—",]
for char in svRead:
    if char.casefold() in exceptionList:
        newChar = char.replace(char, '')
        svParsed += newChar
    elif char.casefold() not in exceptionList:
        svParsed += char
    else:
        continue

#listmaker
def listmaker(svParsed, cnt):
    svParsed = svParsed.casefold()
    svParsed = svParsed.strip()
    for word in re.split(" |\n", svParsed):
        if word in cnt:
            cnt[word]+=1
        else:
            cnt[word] = 1

    with open('filematrix2.csv', 'w', newline='', encoding='UTF-8') as csvfile:
        cntCommon = cnt.most_common()
        cntWrite = Counter(dict(cntCommon))
        fieldnames = ['Word', 'Wordcount']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for tag, count in cntWrite.items():
            writer.writerow({'Word': tag, 'Wordcount': str(count)})
    csvfile.close()

#Checks and initiation
listmaker(svParsed, cnt)
print(len(cnt))
print("starting to rank words...")
print("Most used words:")
print("\n")
print("Writing a CSV-File...")
#filewriter(cnt)
print("CSV-file written!")
print("Shutting down...")
#fileclosures
sv.close()
