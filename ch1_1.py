a=90    #Declaring a variable
b=78.45
course="PYTHON"
lines='''Core
Java
'''
print(a)
print(b) 
print(lines)

print("===========================")
c=7;
res=a/c
print(res)
print("===========================")
res=a//c
print(res)

print("===========================")
res=a%c
print("res=a%c ",res)
print("===========================")
i=3
print(i**3)

print("===========================")

print(a>70)
print(not((a>75) or (a>100)) )
print("===========================")

name="amulya"
lname="Saxena"
print(name)
print(name*4)
print(name+lname)

print(name[2:5])
print(name[-1:1:-1])
print("===========================")

print(name.capitalize())
print(lname.count("a",2,4))
print(lname.find("n"))
    
print("===========================")
a=0
if a>0: print(a," is positive")


print("===========================")
if a>0 : print(a," is positive")
else: print(a," is negative")
print("===========================")
if a>0 : print(a," is positive")
elif a==0: print(a," is equals to zero...")
else: print(a," is negative")

print("===========================")
j=1
while j<11:
    print(j)
    j=j+1

print("===========================")
j=11
while j>0:
    print(j)
    j=j-1
print("===========================")
j=1

while j<5:
    k=1
    while k<5:
        print(j," ",k)
        k=k+1
    print()
    j=j+1

print("===========================")

for x in name:
    print(x)

print("===========================")
for x in range(10):
    print(x)

print("===========================")
for x in range(1,11):
    print(x)
print("===========================")
for x in range(0,11,2):
    print(x)

print("===========================")
for x in range(1,11,2):
    print(x)
print("===========================")
for x in range(1,11,2):
    if x==5:
        break
    print(x)

print("===========================")
for x in range(1,11,2):
    if x==5:
        continue
    print(x)
print("===========================")    

print("Enter the value of x :")
x=input()
print("x = ",x)
print("===========================")   
y=int(input("Enter the value of y :"))
print("y*2 = ",y*2)









































