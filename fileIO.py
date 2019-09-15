
###zip 
l1=[1,2]
l2=[3,4]


for x in zip(l1,l2):
    print(x)

###zip comprehension
nList=["Anurag","Deepti","Jack","Hina"]
mList=[ 56, 78, 63, 82]
D={ name:mark for name,mark in zip( nList, mList ) }
print(D)

## MAP
def square(a):
     return a*a
L1=[1,2,3]
L2=[5,6,7]  
L=[ x for x in map( square, L1 ) ]
print(L)

## Filter
def even(a):
    if a%2==0: return True
    else: return False
L1=[1,2,3,8,6,11,7]
L=[ x for x in filter( even, L1) ]     # even is the function name
print( L )    # selects even values from a list

## Lambda
square=lambda x : x * 2
cube=lambda x : x * x * x

print( square(1551) )   
print( cube(3) )        
