d=dict() #empty dict

d={11:"Ashley",12:"Rushabh",13:"Tejas",10:"Jude"}

print(d[11])

d[11]="Shubham"
print(len(d))
del d[11]
print(d)
print(d.get(15,"Key 15 is not in the dict d"))
d.setdefault(15,"NIIT")
d.setdefault(15,"JAVA")
print(d.pop(12))
print(d)
##d.clear()  
##print(d)
print("========================================")
d1={x: x**2 for x in range(1,11)}
print(d1)
print("========================================")
d2={}
for x in range(1,11):
    d2[x]=x**2

print(d2)

print("========================================")

d.update(d1)
print(d)
print("========================================")

print(d.keys())
print(d.values())

print("========================================")
print(d.items())


print("========================================")



l=[12,45,365,{12:"C++",14:"JAVA",17:"Python"},67,23,"NIIT"]



print(l[3])
print(l[3][17])



d3={'rollnos':[101,102,103],'grades':['A','B','C']}

print(d3['rollnos'][0]," : ",d3['grades'][0])





















