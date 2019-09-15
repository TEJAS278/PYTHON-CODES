a,b,c=24,54.25,"Python"   #Multiple assignments in the same statement
print("a : ",a,"\nb: ",b,"\nc: ",c)

a+=5 
print(a)

res=int("10")  #converting string type numeric value into integer format
print(res+5)

res=int("0x41",16) #converting string type  hexadecimal numeric value into integer format
print(res)

res=int("1010",2) #converting string type binary numeric value into integer format
print(res)

res=int(12.45) #converting float type value into integer format/value
print(res)

res=float(2) #converting int type numeric value into float type
print(res)

res=float("21.42") #converting string type numeric value into float type
print(res)

print(chr(67))  # C
print(ord('a')) # 97
print(abs(-23))  # 23

q,r=divmod(5,2)
print("q = ",q,"\tr= ",r)

print(round(2.3))  # 2.0
print(round(3.5))  # 4
print(round(2.445,2)) # 2.44
print(round(2.44444,0))  # 2.0

print("Its  "+"Python programing")
print("a"*3)

str="  Java   "
print('a' in str) #true
print('a' not in str) #false

a,b=20,20
if a is b:
    print("Both are identical")
else:
    print("Both are not identical")

b=34

if a is not b:
    print("Both are not identical")
else:
    print("Both are  identical")
print(str)
print(str.lstrip())  #removes leading/left side blank spaces
print(str.rstrip())  #removes  trailing/right side blank spaces
print(str.strip().lower()) #removes blank spaces from both side of string
print(str.startswith(' '))
str="abc124"
print(str.isalnum())
str="afad"
print(str.isalpha())
str="547539"
print(str.isdigit())
print(str[2:5:2])  # string type sequence with slicing - 753
print(str[-1:-4:-2]) # 935
print(str[-1::-1]) # 935745
str1=str[::-1] #to reverse str into str1 
print(str1)


t=(10,24,56,"Python")
print(t)
print(t[3])
print(len(t))

t2=(24,40)
t3=t+t2  #combinig two tuple values
print(t3)

s={10,20,40}
s1={70,20,84,30}
print(s-s1)
print(s1-s)
print(s&s1)
print(s|s1)
print(s^s1)

print((s-s1)|(s1-s))

l=[10,"dff",5.4] #list 
print("=========")
for x in l:
    print(x)
print(l)

l[2]=45
print(l)
l.append(78)

print(l)
l.extend([45,73])
print(l)
l.remove(10)
print(l)

y=l.pop()
print(y)
print(l)


l2=[1,2,[4,5],7]  #nested  list
print(l2)
print(l2[0:3])
print(l2[2])
print(l2[2][0])
print(l2[2][1])
l2=[64,152,72,12,4]
l2.sort()
print(l2)
l2.reverse()
print(l2)

a=[x for x in range(2,10,2)]
print(a)
b=tuple(l2)
print(b)

name="Java"
n='-'.join(name)
print(n)
c=n.split('-')
print(c)



