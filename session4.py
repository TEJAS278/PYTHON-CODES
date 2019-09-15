l1=[12,43,54,46]
l2=[46,42,34]
for x in zip(l1,l2):
    print(x)

nList=["Priyank","Rahul","Kamal","Aniket"]
mList=[80,85,98,78]
d={name:mark for name,mark in zip(nList,mList)}
print(d)
