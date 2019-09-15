print("Before exception ...")
#p=45
try:
    print(p)
except NameError:
    print("p is not defined...")
finally:
    print("In finally..")
print("After exception ...")


l=[20,45]
try:
    print(l[2])
except IndexError as e:
    print(e)

#raise IOError
