#function with paramters but which does not return any value

def sum(a,b):
    global count  #global scope
    count+=1
    print("in sum function \n count : ",count)
    print(a+b)
count=12
sum(42,75) #function call
print(count)
print("=================================")

#function with paramters but which returns any value
def sum(a,b):
    return a+b,b-a
s,sub=sum(34,45)
print('sum is :',s,' Subtraction  is ',sub)
    
