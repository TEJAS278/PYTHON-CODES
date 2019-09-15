d=dict()
d={101:"Ashley",102:"Abhinay"}
print(d)
print(d[102])
print(d.keys())
print(d.values())
del d[101]
print(d.pop(101,25))
print(d)
print(d.get(101,"Python"))
d.setdefault(101,"Python")

print(d)
d1={x:x**2 for x in range(1,5)}
print(d1)

d.update(d1)
print(d)
print(d.items())
print('=====================')
for k,v in d.items():
    print("Key :",k,"\tValue : ",v)

l=[87,{101:"Ashley",102:"Abhinay"},"JAVA"]
print('============================')
print(l)
print(l[0])
print(l[1])
print(l[1][101])
d2={101:"Ashley",102:"Abhinay",'marks':[78,98,78,48,68]}
print(d2['marks'])
print(d2['marks'][1])
print('============================')
for i in d2['marks']:
    print(i)






##def function_name(parameters):
##    //block of statements
##
##function_name(parameters)
##
##

def sum(a,b):
    return a+b
res=sum(50,75)
print('Sum  is :',res)

def sumList(a):
    global s
    s=0  #local variable
    for j in a:
        s=s+j
    return s
 
l1=[34,45,56,76,57]  
res=sumList(l1)
print('Sum of all the values from list l1 is :',res)


def display():
    print('*'*20)

display()





def squareCube(x):
    sq=x**2
    c=x**3
    return sq,c

n=int(input('Enter the number'))
a,b=squareCube(n)
print('Square of ',n,' is :',a)
print('Cube of ',n,' is :',b)






















