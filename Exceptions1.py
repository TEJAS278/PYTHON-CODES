try:
   fh = open("d:\\testfile4.txt", "r")
  # fh.write("This is my test file for exception handling!!")
except IOError:
   print("Error: can\'t find file or read data")
else:
   print("Written content in the file successfully",fh.read())
   fh.close()