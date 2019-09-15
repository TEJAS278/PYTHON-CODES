d={}
d={101:"Shubham",102:"Niit"}
print(d[101])
print("len(d) : ",len(d))

d={"A":80,"B":70,"C":60,"A":67}
print(d.pop("D",10))
#print("Enter the name :")
#name=input()

#if name in d:
#    print("Student is passed..")
#else:
#    print("Failed...")

d.setdefault("B",40)
print(d)

sq={x:x**2 for x in range(1,6)}
print(sq)
d1={"B":65}
d.update(sq)
print(d)
print(d.keys())
print(d.values())
print("==============")
for k,v in d.items():
    print(k," : ",v)
print("++++++++++++++++++++")
l=[10,{"A":80,"B":70,"C":60},"JAVA",7932]
print(l[1])
print(l[1]["B"])
print("++++++++++++++++++++")
d2={1:10,2:[80,70,60],'lang':"JAVA",'ccode':7932}
print(d2[2])
print(d2[2][2])

print('<++++++++++++++++++Modular programming (UDF)++++++++++++++>')
print('function without arguments and not returning any value');
def display():      #function definition
    print("display() function is invoked")
    
print("Before the display()...")
display()   #function call/invocation
print("After the display()...")

print('function with arguments and not returning any value');

def calc_sq(a):  #a is formal argument
    res=a**2
    print("Square of ",a," is ",res)

num=int(input("Enter the number for calculating the sqaure :"))
calc_sq(num)   # num actual arguments


print('function with arguments and returning single value');

def calc_sq(a):  #a is formal argument
    res=a**2
    return res
    

num=int(input("Enter the number for calculating the sqaure :"))
r=calc_sq(num)   # num actual arguments
print("Square of ",num," is ",r)

print('=========function with arguments and returning multiple values =========');

def calc_sq_cube(a):  #a is formal argument
    s=a**2
    c=a**3
    return s,c
    

num=int(input("Enter the number for calculating the sqaure :"))
s,c=calc_sq_cube(num)   # num actual arguments
print("Square of ",num," is ",s)
print("Cube of ",num," is ",c)


print('function with arguments and returning any value');

def greater(a,b):  
    if a>b:
        return a
    else:
        return b
    
print("Enter the two  numbers  :")
num1=int(input("num1 :"))
num2=int(input("num2 :"))
print("The greater no is :",greater(num1,num2))

print('================function with list  arguments');

id1=45
def show_list(l2):
    #  n=35    # local varaible to show_list() only which is accessible in this funtion only
    id1=87
    print("id : ",id1)
    for x in l2:
       print(x)
    
l=[10,42,65,74]
show_list(l)

#print(n)


























