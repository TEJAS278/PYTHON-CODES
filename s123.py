num=0
if num>15:
    print(num," is greater than 15...")
    print("num  : ",num)
else:
    print("Num is less than 15 ...")
sid=102
name="Raj"
print("Student id : ",sid," Student Name : ",name)


#if elif

if(num>0):
    print(num," is positive")
elif (num<0):
    print(num," is negative")
elif (num==0):
    print(num," is zero")

n=1
while (n<11):
    print(n)
    n=n+1

print("After the while loop")

for x in range(11):
    print(x)

print("=======================Use of break Statement")

for x in range(1,11):
    if x==5:
         break
    print(x)
print("=======================Use of continue Statement")
for x in range(1,11):
    if x==5:
        continue
    print(x)
    
print("=======================")

for x in range(1,11,2):
    print(x)
print("=======================")
count=0
for x in "Welcome to NIIT":
    if x=='e':
        count=count+1        
    print(x)
print("count  :",count)


#taking input from user
print("=========Use input() Statement=======")
nm=int(input("Enter the number :"))
print(nm*2)  
print("Sqaure ",nm**2) 
























