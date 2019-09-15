name="NIIT"
def accept():
    global name
    name=input("Enter the name ")

def display():
    print(name)

def calc_square():
    sum=0
    for x in range(1,11):
        print(x**2)
        sum=sum+(x**2)
    return sum,10
res,count=calc_square()

print("Sum of first ",count," squares : ",res)
accept()
display()  #invoke a function

def even_odd(a):
    if(a%2==0):
        print(a," is even no...")
    else:
        print(a," is odd no...")

num=int(input("Enter the number :"))
even_odd(num)
