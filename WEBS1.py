from urllib.request import urlopen
file1=urlopen("https://en.wikipedia.org/wiki/Python")
##print(file1.read())
from bs4 import BeautifulSoup
s=BeautifulSoup(file1,"html.parser")
print(s.title)
print(s.title.string)

for a in s(["script","style"]):
    print(a.extract())
text=s.get_text()
print(text)
lines=(line.strip() for line in text.splitlines() )
for x in lines:
    print(x)

import json
d={101:"Ashley",102:"Seema"}
j=json.dumps(d)
print(d)
print(j)

l=[10,40,50,60,52,78]

j=json.dumps(l)
print(j)
d1=json.loads(j)
print(d1)
