 from urllib.request import urlopen
file1=urlopen("https://en.wikipedia.org/wiki/Python")
from bs4 import BeautifulSoup
s=BeautifulSoup(file1,"html.parser")
print(s.title)
print(s.title.string)
for a in s(["script","style"]):
    print(a.extract())
text=s.get_text()
print(text)
lines=(line.strip() for line in text.splitlines() )
print(lines)
def count_individual_words(lines):
    global  word_count 
    word_count = {x: text.count(x) for y in lines for x in y.split()}
    return word_count
for i,v in count_individual_words(lines).items():
   print(i,v)
