count = 0

number = int(input("Enter a number "))
n=int(input("Enter a number to count  "))
while (number > 0):
  t=number%10
  number = number//10
  if n==t:
      count = count + 1
print ("Total number of digits : ",count)


##1232
##
##t=1232%10
##t=2
##num=123
##
##count=1
##
##t=123%10
##t=3
##num=12
##count=1
##t=12%10
##t=2
##num=1
##count=2
##
##t=1%10
##t=1
##num=0
##count=2

##
##0  1 1 2 3 5 8 
