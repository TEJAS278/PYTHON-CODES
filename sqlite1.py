import sqlite3
con=sqlite3.connect('d:\\data13.db')
print('connected...')
con.execute('''create table employee12
            (EmpId int not null,
            EName varchar(50) not null,
            Address varchar(50) not null);
            ''')
print('table created...')
con.execute('''insert into employee12(EmpId,EName,Address)
                values(102,'Harsh','Mumbai');''')
con.commit()
print('Record Inserted .....')
print('====================================')
cursor=con.execute('select * from employee12;')
for r in cursor:
    print("EmpId :",r[0],"\nEmployee name : ",r[1],"\nAddress :",r[2])
    
con.execute("update employee12 set ename='Ashley' where empid =102;")
con.commit()
print('====================================')
cursor=con.execute('select * from employee12;')
for r in cursor:
    print("EmpId :",r[0],"\nEmployee name : ",r[1],"\nAddress :",r[2])
con.execute("delete from employee12 where empid=101")
print('====================================')
cursor=con.execute('select * from employee12;')
for r in cursor:
    print("EmpId :",r[0],"\nEmployee name : ",r[1],"\nAddress :",r[2])
