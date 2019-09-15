fo=open("d://file3.txt","w")
s="This is the output file...."
l=["10","20","30","40","50"]
fo.write(s)
fo.seek(0,2)
fo.writelines(l)
print("Successfully written the contents to the file...")
fo.close()
fo1=open("file.txt","r")
print("Cursor offset before reading the contents :",fo1.tell())
print("The file contents are:")
s1=fo1.read()
print(s1)
print("Cursor offset after reading the contents :",fo1.tell())
fo1.close()

fo2=open("file2.txt","w")
fo2.write(s1.upper())
fo2.close()
