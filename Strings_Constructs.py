
name="shubham"+"R D"
print(name*3)
print(name.capitalize())
print(name[1]*4)
print("===================================")
print(name.count('h',0,len(name)))
print(name.count('h',2,len(name)))
print(name.count('h',0,4))
print("===================================")
print(name.find('h',0,len(name)))
print(name.find('h',2,len(name)))

#Decision making constructs


n=-80
print("===================================")
if n>0:
    print("n is a positive no..")
    if n%2==0:
        print(n," is even number...")
    else:
        print(n," is odd number...")
elif n<0:
    print("n is a negative no..")
else:
    print("n is zero...")


n1=124
n2=64
n3=126
print("===================================")

if n1>n2 and n1>n3:
    print("n1 is greater...!!!")
elif n2>n3:
    print("n2 is greater...!!!")
else:
    print("n3 is greater...!!!")
print("===================================")
i=1
while i<=10:
    if i%2==0:
         print(i)
    i=i+1
print("===================================")
count=0
for x in name:
    if(x=='h'):
        count=count+1
    print(x)
print("count of char 'h' :",count)

print("===================================")
for y in range(10):
    print(y)
    if y==6:
        break
   


print("===================================")
for y in range(1,10):
    print(y)



print("===================================")
for y in range(1,10,2):
    print(y)

print("===================================")
for y in range(10):
    if y==6:
        continue
    print(y)
    
if n==89:
    pass
print("===================================")
##j=0
##while j<2:
##    print(j)
##    j=j+1
##else:
##    print("Invalid value for j")

print("===================================")
print("Enter the value :")
num1=input()
num2=input()
res=num1+num2
print("num1 ",num1," num2 ",num2, " res :  ",res)

print("===================================")
name=input("Enter the name :")
print(name)


print("===================================")
print("Enter the value :")
num1=input()
num1=int(num1)
num2=input()
num2=int(num2)
res=num1+num2
print("num1 ",num1," num2 ",num2, " res :  ",res)


print("===================================")
print("Enter the value :")
num1=int(input())
num2=int(input())
res=num1+num2
print("num1 ",num1," num2 ",num2, " res :  ",res)
















