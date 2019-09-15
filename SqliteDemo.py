import sqlite3

conn = sqlite3.connect('test.db')

print("Opened database successfully")

##conn.execute('''CREATE TABLE COMPANY1
##         (ID INT PRIMARY KEY     NOT NULL,
##         NAME           TEXT    NOT NULL,
##         AGE            INT     NOT NULL,
##         ADDRESS        CHAR(50),
##         SALARY         REAL);''')
##print("Table created successfully")

##conn.execute("INSERT INTO COMPANY1(ID,NAME,AGE,ADDRESS,SALARY)  VALUES (1, 'Paul', 32, 'California', 20000.00 )");
##conn.execute("INSERT INTO COMPANY1 (ID,NAME,AGE,ADDRESS,SALARY)  VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");
##
##conn.execute("INSERT INTO COMPANY1 (ID,NAME,AGE,ADDRESS,SALARY)  VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");
##
##conn.execute("INSERT INTO COMPANY1(ID,NAME,AGE,ADDRESS,SALARY)  VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");
##
##conn.commit()
##print("Records inserted successfully")
cursor = conn.execute("SELECT id, name, address, salary from COMPANY1")
for row in cursor:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("ADDRESS = ", row[2])
   print("SALARY = ", row[3], "\n")

print("Operation done successfully")


conn.execute("UPDATE COMPANY1 set SALARY = 25000.00 where ID = 3")
conn.commit
print("Total number of rows updated :", conn.total_changes)

cursor = conn.execute("SELECT id, name, address, salary from COMPANY1")
for row in cursor:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("ADDRESS = ", row[2])
   print("SALARY = ", row[3], "\n")

print("Updation done successfully")

conn.execute("DELETE from COMPANY1 where ID = 2;")
print("Total number of rows deleted :", conn.total_changes)

cursor = conn.execute("SELECT id, name, address, salary from COMPANY1")
for row in cursor:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("ADDRESS = ", row[2])
   print("SALARY = ", row[3], "\n")

print("Deletion done successfully")


conn.close()
