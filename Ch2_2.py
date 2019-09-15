a,b,c=21,23,"Python"
print(a,b,c)
b=int("0x41",16)
print(b)
b=int("10101",2)
print(b)

print(chr(68))
print(ord('a'))
print(abs(-56))

q,r=divmod(65,3)
print(q,r)

print("==============================")
n=round(65.45555,1)
print(n)
n=round(65.55555)
print(n)
n=round(65.45555,0)
print(n)
n=round(65.45555,2)
print(n)
n=round(65.5)
print(n)
n=round(3.5)
print(n)

print("==============================")

str="JAVA PYTHON"
print(str.count("A",0,len(str)))
print(str.lower())


str="JAVA PYTHON"

print(str)
print(str.lstrip())
print(str.rstrip())
print(str.strip())
print(str.startswith('  '))

str2="456"
print(str2.isalnum())
print(str2.isalpha())
print(str2.isdigit())

print("==============================")

print(str[0:len(str):3])


print(str[-1:4:-1])
print(str[-1::-1])

print("==============================")


t=tuple()
a=549
t=(a,15,"CPP",45.56,'A')
print(t)
#a=34
#t[0]=a
print(t[2:len(t)])
t1=(34,456,67,23)
t=t+t1
print(t)
print("==============================")
s={10,25,96,45}
print(s)
s1={25,64,32}

#print(s1[0])
print(s-s1)
print(s1-s)
print(s&s1)
print(s|s1)
print(s^s1)
print(s-s1|s1-s)
print("==============================")
l=[34,45,[34,75],56]
print(l[2])
print(l[2][0])

l.append(90)
print(l)
l.extend([87,45,75])

print(l.pop(2))
print(l)



































