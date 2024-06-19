import re

f = open('Regexe.html')
fileContents = f.read()

print(fileContents)

print(re.escape(fileContents))
