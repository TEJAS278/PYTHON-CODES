d={'Ashley' :76,'Abhi' :56,'Seema':74}
print(d)
print(d['Ashley'])
print(len(d))
d['Abhi']=98
print(d)
#del d['Abhi']
print(d.pop('Abhi',10))
print(d)
print(d.pop('Abhi',10))
print(d)
print(d.get('Seema'))
print(d.get('Abhi',50))
print(d.setdefault('Abhi',50))
print(d)
print("====================================")

sq={y:y**2 for y in range(1,6)}

print(sq)

print("====================================")

d.update(sq)
print(d)

print("====================================")
print(d.keys())

print(d.values())
print(d.items())
print("====================================")
l=[24,65,78,{'Ashley' :76,'Abhi' :56,'Seema':74},"Python","JAVA",45.565]
print(l)
print(l[3])
print(l[3]['Seema'])


print("====================================")
d2={'Ashley' :76,'Abhi' :56,'Seema':74,'grades':['A','B','C','D']}
print(d2)
print(d2['grades'])
print(d2['grades'][1])






















