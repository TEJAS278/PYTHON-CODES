import re
p=re.compile("\D[A-Z]..")
m=p.match("aDas")
if(m):
    print("String mathced")
else:
    print("Invalid string")
