##num=int(input("Enter a number "))
##count=0
##d=0
##rev=0
##temp=num
##while num>0:
##    d=num%10
##    count=count+1
##    rev=rev*10+d
##    num=num//10
##    
##print(count)
##print(rev)
##if(temp==rev):
##    print(temp," is a palindrome...")
##else:
##    print(temp," is not a palindrome...")


##123
##
##123%10 = 3
##123//10=12
##0*10+3=3
##
##12%10=2
##12//10=1
##3*10+2=32

n=int(input("Enter the limit :"))
n1=0
n2=1
n3=1
if(n==0):
    print(n1)
elif(n>=1):
    print(n1,n2)
    while n<n3:
        n3=n1+n2
        print(n3)
        n1=n2
        n2=n3
        
else:
    print("please enter the positive number")



##10
##
##
##0 1 1
##n1=1
##n2=1
##n3=2
##0 1 1 2
##n1=1
##n2=2
##n3=3
##0 1 1 2 3









































