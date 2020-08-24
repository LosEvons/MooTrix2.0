import unicodedata
svParsed = ''
svParsed2 = ''
problemChildren = []
problemChildren2 = []
exceptionList = ["@", ",", ".", "!", ":", ";","-", "?", "»", ""]
sv = open('sv.txt', 'r', encoding='UTF-8')
svRead = sv.read()
sv.close()
for char in svRead:
    if char.isalnum() or char == ' ' or char == '\n':
        svParsed += char
for char in svRead:
    if char.casefold() in exceptionList:
        newChar = char.replace(char, '')
        svParsed2 += newChar
    elif char.casefold() not in exceptionList:
        svParsed2 += char
for char in svParsed2:
    if char not in svParsed:
        if char in problemChildren:
            continue
        else:
            problemChildren.append(char)
            problemChildren2.append(ord(char))

print(problemChildren)
print(problemChildren2)
