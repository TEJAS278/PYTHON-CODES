## with UDF
def sum(a,b):
     return a+b

L1=[1,2,3]
L2=[5,6,7]  
L=[x for x in map( sum, L1,L2) ]
print(L)


## with lambda() reducing code to compact

L1=[1,2,3]
L2=[5,6,7]  
L=[ x for x in map( lambda a,b : a+b, L1 , L2 ) ]
print( L )


##lamda for even no's

L1=[1,2,3,8,6,11,7]
L=[x for x in filter( lambda a : a%2==0,L1) ]
print(L)
