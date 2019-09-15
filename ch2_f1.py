a=int("0x41",16)
print(a)
b=int("1011",2)
print(b)

print(chr(97))

print(chr(65))
print(ord('A'))
print(abs(97))


q,r=divmod(178,7)
print(q,r)


print(round(56.5325,0))   #56
print(round(20.5))   #20
print(round(23.5))   #24
print(round(24.5))   #24
str="htdhyy456544"
print(str.upper())
str1="PYTHON    "
print(str1.lower())
print(str1.lstrip())
print(str1.rstrip())
print(str1.strip())
print(str.isalnum())
print(str.isalpha())
print(str.isdigit())

s="PYTHON"
print(s[3:5])
print(s[1:5:3])
print(s[1:5:2])
print(s[0:-1])

print(s[-1:3:-1])
print(s[-1:0:-1])
print(s[::-1])

t=tuple()  #empty tuple
t=(10,32,15.45,'Python')

print(t)
#t[2]=46
print(t[2])
print(len(t))

if 324 in t:
    print('found')


t1=(34,67)
t2=t+t1
print(t,t1,t2)


set1={10,10,20,45}
set2={64,35,20,48}
print(set1)

print(set1-set2)
print(set2-set1)
print(set1&set2)
print(set1|set2)
print(set1^set2)
print((set1-set2),(set2-set1))

l=[10,45,[70,84],6.5,"NIIT"]
print(l[1:len(l)])
print(l[2])
print(l[2][1])
l.append("Training.com")
print(l)
l.extend({98,78,76,787})
l.extend(set1)
l.append(set2)
print(l)

l.insert(2,"Welcome")
print(l)
print(l.count(10))
print(l.pop(4))
print(l)
l.reverse()
print(l)

even=[]
for x in range(0,21,2):
       even.append(x)

print(even)


odd=[x for x in range(1,21,2)]
print(odd)
str1='-'.join(str1)
print(str1)
split=str1.split('-')
print(split)















































































