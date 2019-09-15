import sqlite3
conn=sqlite3.connect('db31.db')
print('Connected to db1 ...')
##conn.execute('''create table Student(
##                rollno int not null,
##                Name varchar not null,
##                Address varchar not null);''')
##print('Table created successfully...')
conn.execute('''insert into Student
                values(12,'Shubham','Mumbai')''')

conn.commit()
print('Record inserted...')
print('Table Contents ==========')
cursor= conn.execute("select * from Student")
for row in cursor:
    print('Roll NO : ',row[0],'\nName :',row[1],'\nAddress :',row[2])
conn.execute("update Student set  name='Sahil' where rollno=12")
conn.commit()
print('Table Contents ==========')
cursor= conn.execute("select * from Student")
for row in cursor:
    print('Roll NO : ',row[0],'\nName :',row[1],'\nAddress :',row[2])
