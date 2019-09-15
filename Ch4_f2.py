fo=open("abc.txt","w")
print("file opened in write mode ...")
l=["12","34","45","56","57"]
for x in l:
    fo.write(x)
print("Written the contents to file ...")
