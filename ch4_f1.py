fo=open("d://file1234.txt","w")
print("File123 is opened in write mode...")
s="""Its a function to write to the files...!!

Welcome to python programming..."""
l=["125","45","64.45","48,458"]
fo.write(s)
print(fo.tell())
fo.writelines(l)
print("String written to the file")
fo.write("adfasdfd")

f2=open("d://file1234.txt","r")
print(f2.read())
f2.close()


print("=====================================")
f3=open("d://demo.txt","w")
f3.write("content to be converted in uppercase...")
f3.close()
f3=open("d://demo.txt","r")
str=f3.read()
print(str)
f3.close()
print("=====================================")
str=str.upper()
f3=open("d://f2.txt","w")
f3.write(str)
f3.close()

f3=open("d://f2.txt","r")
print(f3.read())
f3.close()
print("=====================================")




l1=[12,456,76,56]
l2=[34,45,67,68,78]
for x,y in zip(l1,l2):
    print(x,y)

print("=====================================")
def decre_value(a):
    a=a-1
    return a 
for x in map(decre_value,l1):
    print(x)
print("=====================================")
def sum(a,b):
    return a+b
for x in map(sum,l1,l2):
    print(x)


print("=====================================")

def odd(a):
    if a%2!=0:
        return True
    else:
        return False
for y in filter(odd,l2):
    print(y)
print("=====================================")
str=lambda x:x+" python"
print(str("Welcome"))

sq=lambda y:y*y
print(sq(12))
print("=====================================")

for x in map(lambda a,b: a+b,l1,l2):
    print(x)























