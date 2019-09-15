t=(10,2.5,14,"Python")

print(t)
print(t[3])
t1=(45,45,2345)
t=t+t1
print(t)

s=set()
s={3,34,2,3,67}
print(s)
s1={34,45,3,56}

s2=s-s1
print(s2)
s2=s&s1
print(s2)
s2=s|s1
print(s2)
s2=s^s1
print(s2)
s2=s-s1|s1-s
print(s2)

l=[12,23,34,[65,79],56,"JAVA"]
print(l)
print(l[3])
l[1]=56
print(l)
for x in l:
    print(x)
for x in t:
    print(x)
print(l[3][1])
l.append(109)
print(l)
l1=[35,7,576,75]
l.extend(l1)
print(l)
l1.insert(3,342)
print(l1)

print(l)
del l[2:5]
print(l)

str="JAVA"
str1='-'.join(str)
print(str1)
str1=str1.split('-')
print(str1)























