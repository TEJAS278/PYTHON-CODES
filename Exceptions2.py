try:
   fh = open("testfile2.txt", "r")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print("Error: can\'t find file or read data")
finally:
   print("in finally block...")

##try:
##   fh = open("testfile", "w")
##   try:
##      fh.write("This is my test file for exception handling!!")
##   finally:
##      print("Going to close the file")
##      fh.close()
##except IOError:
##   print("Error: can\'t find file or read data")
