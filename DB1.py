import sqlite3
con=sqlite3.connect('DB1.db')
print("Conncted to DB1.db successfully")

#Creating a table
##
##con.execute('''create table Student1
##    (id int PRIMARY KEY     NOT NULL ,
##    name varchar(50),
##    address varchar(50),
##    course varchar(25));''')
##print(" Student Table is created successfully...")

#inserting records into table Student

##con.execute(''' insert into Student1(id,name,address,course)
##            values(101,'Raj','Mumbai','Python') ''')
##con.execute(''' insert into Student1(id,name,address,course)
##            values(102,'Kirtan','Mumbai','Python') ''')
##con.execute(''' insert into Student1(id,name,address,course)
##            values(103,'Karan','Mumbai','Python') ''')
##print("Data inserted successfully")

#Displaying the records
con.execute(''' insert into Student1(id,name,address,course)
           values(?,?,?,?)''',(104,'Ashley','Mumbai','Python'))

cursor= con.execute('select * from Student1')
print("Student details are :")
for s in cursor:
    print('id : ',s[0])
    print('name : ',s[1])
    print('address : ',s[2])
    print('course : ',s[3])


con.execute("update student1 set course='JAVA' where id=103")
print("The data is updated")
cursor= con.execute('select * from Student1')
print("Student details are :")
for s in cursor:
    print('id : ',s[0])
    print('name : ',s[1])
    print('address : ',s[2])
    print('course : ',s[3])

con.execute("delete from student where id=102")
print("The data is deleted")
cursor= con.execute('select * from Student')
print("Student details are :")
for s in cursor:
    print('id : ',s[0])
    print('name : ',s[1])
    print('address : ',s[2])
    print('course : ',s[3])



con.commit() # To save the contents to the database
con.close()  # To close the connection

print("Connction closed successfully")
