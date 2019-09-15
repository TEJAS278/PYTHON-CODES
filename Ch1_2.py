#first program 
n=42
a,b,c=23,43,52
str="""
Java
Python
"""
print(n,a,b,c)
print(str)
print(a%2)
print(4**3)


print(c/3)
print(c//3)

print(c!=52)
print(not(c<50 or (c%2==0)))
str1="perl "+"Cpp"
print(str1)
print(str1*5)
print(str1[3])
print(str1.capitalize())
print(str.count('a',3,len(str)))
print(str1.count('p',0,len(str1)))
print(str1.find('C',0,7))


if a%2==0:
    print(a," is a even number")
else:
    print(a," is a odd number")


if a>0:
    print("positive")
elif a<0:
    print("negative")
else:
    print("zero")


i=1
while i<11:
    print(i)
    i=i+1

print("====================================")
for x in range(10):
    print(x)
    
print("====================================")
for x in range(1,11):
    print(x)

print("====================================")
for x in range(1,11,2):
    print(x)
print("====================================")
for x in range(0,11,2):
    print(x)


print("====================================")
for x in range(1,11):
    print(x)
    if x==5:
        break
   

print("====================================")
for x in range(1,11):
    if x==5:
        continue
    print(x)
else:
    print("for loop terminated")
print("====================================")
print("Enter the number:")
num=input()
print("You have entered :",num)

print("====================================")

num=input("Enter the number:")
print("You have entered :",num+"10")


print("====================================")

num=input("Enter the number:")
n1=int(num)
print("You have entered :",n1+10)

print("====================================")

num=int(input("Enter the number:"))

print("You have entered :",num+10)

















