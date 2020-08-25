import PySimpleGUI
import mootrix
from collections import Counter
#variables
svParsed = "svparsed is empty"
cnt = Counter()
exceptionList = ["@", ",", ".", "!", ":", ";","-", "?", "»", ""]
inclusionList = [" ", "\n"]
svParsed = ''
svParsed2 = ''
svRead = ''
#Checks and initiation
mootrix.fileopen()
print(len(svRead))
mootrix.listmaker(cnt, svParsed, svParsed2, svRead, exceptionList)
print("svParsed and svParsed2 values:")
print(len(svParsed))
print(len(svParsed2))
print("starting to rank words...")
print("Most used words:")
print(cnt.most_common(10))
print("\n")
print("Writing a CSV-File...")
print("CSV-file written!")
print("Shutting down...")
