import unicodedata
unicode = open('everyUnicodeCharacter.txt', 'r', encoding = 'UTF-8')
unicodeRead = unicode.read()
unicode.close()
unicodeParsed = ''
for char in unicodeRead:
    if char.isalnum():
        unicodeParsed += char

with open('isalnum()characters.txt', 'w', encoding = 'UTF-8') as textfile:
        textfile.write(unicodeParsed)

print("Number of unicode characters:")
print(len(unicodeRead))
print("Number of alphanumeric unicode characters")
print(len(unicodeParsed))
textfile.close()
