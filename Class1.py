class Employee:
   ' class for all employees'
   empCount = 0

   def __init__(self, name="Shobhit", salary=45000):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print("Name : ", self.name,  ", Salary: ", self.salary)
print(Employee.__doc__)

emp1 = Employee()
emp1.displayEmployee()
emp1.displayCount()
emp2 = Employee("Shubham", 34000)
emp2.displayEmployee()
emp2.displayCount()
emp1.age = 7  # Add an 'age' attribute.
emp1.age = 8  # Modify 'age' attribute.
#del emp1.age  # Delete 'age' attribute.

print(hasattr(emp1, 'age'))    # Returns true if 'age' attribute exists
print(getattr(emp1, 'name'))    # Returns value of 'age' attribute
setattr(emp1, 'name', "Ashley") # Set attribute 'age' at 8
print(getattr(emp1, 'name')) 
delattr(emp1, 'salary')    # Delete attribute 'age'


##class Point:
##   def __init__( self, x=0, y=0):
##      self.x = x
##      self.y = y
##   def __del__(self):
##      class_name = self.__class__.__name__
##      print(class_name, "destroyed")
##
##pt1 = Point()
##pt2 = pt1
##pt3 = pt1
##print id(pt1), id(pt2), id(pt3) # prints the ids of the obejcts
##del pt1
##del pt2
##del pt3
