a=90  #declaring and assigning the value to a variable a
print(a) #Displaying the value of a
name="Shubham"
f=34.45
_m_='''Core

Java
'''
print(_m_)


print("======================================")

b=56
c=a+b
print("c =",c)
print("======================================")
a=38
c=a/3
print("c = ",c)
print("======================================")
c=a//3
print("c = ",c)
print("======================================")
c=5**3
print(c)
print("======================================")
c=a%3
print("c = ",c)
print("======================================")

print(a==b)
print(a!=b)
print(a>b)
print(a!=b and a>b)
print(not(a!=b or a>b))


print("======================================")

str=name+" R D"
print(str)
print(name*4)
print(name[3])
print("======================================")
str1="java"
str1=str1.capitalize()
str1=str1.upper()
print(str1)
print("======================================")

i=str1.count('A',0,2)
print(i)

print("======================================")

i=str1.find('V',0,4)
print(i)

print("======================================")

if (a>b):
    print("a is greater....")
else:
   print("b is greater")


print("======================================")
c=87

if a>b and a>c :
    print("a is greater....")
elif b>a and b>c :
    print("b is greater....")
else:
    print("c is greater....")

print("======================================")

char='a'

if char=='a' or char=='e':
    print('its a vowel')

print("======================================")

n=1
while n<11:
    print(n)
    n=n+1


print("======================================")

n=10
while n>0:
    print(n)
    n=n-1
print("======================================")

for x in range(10):
    print(x)
print("======================================")

for x in range(1,11):
    print(x)

print("======================================")

for x in range(1,11,2):
    print(x)
print("======================================")

for x in range(0,11,2):
    print(x)
print("======================================")
count=0
for x in "Spring Framework":
    if x=='r':
        count+=1  #count=count+1

print("count = ",count)
print("======================================")

for x in range(1,11):
    print(x)
    if x==5:
        break
   

print("======================================")

for x in range(1,11):
    if x==5:
        continue
    print(x)
else:
    print("in else of for loop")

print("======================================")

name=input("Enter the name :")

print("You have entered : ",name)

print("======================================")

num=int(input("Enter a number :"))
num=num*2
print("Square : ",num)





























































