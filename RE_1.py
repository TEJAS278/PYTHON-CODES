import re

pattern=re.compile("S\d\d00103\d\d\d\d\d")
mO=pattern.match(input("Enter the string :"))
if(mO):
    print(mO.group(0))
    print(mO.span())
##mO=pattern.search(input("Enter the string :"))
##if(mO):
##    print(mO.group(0))
##mO=pattern.findall(input("Enter the string :"))
##for x in mO:
##    print(x)
mO=pattern.sub('1234',input("Enter the string :"),count=0)
print(mO)
 
