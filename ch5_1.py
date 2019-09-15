class demo:
    "This is  first class example to accept and display value of a variable"
    def __init__(self,a=10):
        self.a=a
    def display(self):
        print(self.a)

print(demo.__doc__)
d=demo(98)
d.display()
print(d.a)


##class class_name:
##    #data members
##    #memeber functions
##
##
##syntax for creating object of a class :
##
##object_name= class_name()
##
##object_name.datamember
##object_name.memberfunction
