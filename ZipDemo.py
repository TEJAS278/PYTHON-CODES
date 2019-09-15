print("<==============ZIP function ===================>")
l1=[20,70,89]
l2=[80,60,70,86]
for y in zip(l1,l2):
    print(y)
names=["Shubham","Raj"]
marks=[90,98]
d={name:mark for name,mark in zip(names,marks)}

print(d)

print("<==============Map function ===================>")
def sum(a,b):
    return a+b

add=[x for x in map(sum,l1,l2)]
print(add)
n=[10,8,9]
print(n)
def sq(p):
    return p*p
squares=[x for x in map(sq,n)]
print(squares)


print("<==============Filter function ===================>")
def even(n1):
    if(n1%2==0):
        return True
    else:
        return False
inp=[20,13,15,12,4]
print("inp list = ",inp)
evenList=[k for k in filter(even,inp)]
print(evenList)
print("<==============Lambda function ===================>")
m=lambda x:x*5
print(m(6))

