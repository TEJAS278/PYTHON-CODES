import os

obj=open("file1.txt","r")  
s1=obj.read()

#os.rename("abcd.txt","demo.txt")
#os.remove("demo.txt")
#os.mkdir("dddd")
#os.chdir("dddd")

s=os.getcwd()
print(s)
obj.close()
obj1=open("file2.txt","w")  
obj1.write(s1.upper())
obj1.close()
#os.remove("file2.txt")
#os.rmdir("dddd")
 
#obj2=open("file2.txt","r")
#s1=obj2.read(10)  
#print(s1)  
#obj2.close()  




