import sqlite3

conn=sqlite3.connect("db1.db")
print("Connected to db successfully...")
query='''create table student123(rollno int not null,
name VARCHAR2(50) not null,primary key(rollno));
'''
##conn.execute(query)
print("Table created successfully...")

query='''insert into student123
values(103,'Divya');'''
#conn.execute(query)
conn.commit()
print("Record inserted successfully...")

cursor=conn.execute('select * from student123;')
for x in cursor:
    print("Roll no  :",x[0])
    print("Name :",x[1])
##query="'update student123 set name='Seema' where rollno=103;'"
##conn.execute(query)
conn.execute('delete from student123 where rollno=103;')
conn.commit()

cursor=conn.execute('select * from student123;')
for x in cursor:
    print("Roll no  :",x[0])
    print("Name :",x[1])
