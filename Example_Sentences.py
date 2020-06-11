import re
filename = "sentences2.txt"      #locates .txt database within same folder

infile = open(filename, "r", encoding="utf8")       #opens file; allows for cyrillic characters
lines = infile.readlines(20)

print("What word would you like examples for?")
phrase = input()            #assigns a variable phrase

for lines in infile:
    if re.findall('(.+)'+phrase+'(.+)', lines, re.MULTILINE):       #searches .txt document for key word/phrase
        print(lines)            #prints all lines which include phrase

input('Press Enter to exit')        #prevents application from losing without input