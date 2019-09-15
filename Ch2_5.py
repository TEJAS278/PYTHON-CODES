num=int("45")
print(num)
num=int(45.56)
print(num)
num=int("0x16",16)
print(num)
num=int("101011",2)
print(num)

print(chr(97))
print(ord('K'))
print(abs(34-45))
print(divmod(13,4))

print("=====================================")

print(round(24.5655))

print(round(24.5655,2))
print(round(24.5655,1))
print(round(24.5))
print(round(23.5))
print("=====================================")
str="Python12"
print(str)
print(str.lstrip())
print(str.rstrip())
print(str.strip())
print("=====================================")
print(str.isalnum())
str="342355"
print(str.isdigit())
str="JAVA PRogramming"
print(str.isalpha())
print(str[1:4])
print(str[-1])
print(str[-1:5:-1])
print(str[-1:0:-1])
print(str[-1::-1])

print("=====================================")

t=tuple()
t=(10,24,56,57)
print(t)
print(t[2])
t1=(234,345,56)
t=t+t1
print(t)

print("=====================================")

s=set()
s={45,78,98,54,45}
print(s)
s1={45,56,96}
print(s-s1)
print(s1-s)

print(s|s1)

print(s&s1)
print(s-s1|s1-s)
print(s^s1)

print("=====================================")

l=[54,"Python",45.56,987,['A','E','I','O','U']]

print(l)
print(l[2:4])
l[3]=95
print(l)
print(l[4])
print(l[4][2:5])
l.append("JAVA")
print(l)
l.append([456,768,689,894])
print(l)
l.extend([54,768,689,894])
print(l)
l.insert(2,"C++")

print(l)
print(l.count(54))
l.remove(54)
print(l)
print(l.pop(5))
print(l)
print("=====================================")

l=[]
for x in range(0,21,2):
    l.append(x)
print(l)
print("=====================================")

l=[x for x in range(0,21,2)]
print(l)

print("=====================================")
str1='-'.join(str)
print(str1)
words=str.split(' ')
print(words)






    











