from platform import release
import sqlite3
con= sqlite3.connect("student.db")
print("database connected")
con.execute('''create table stud_details (rno int,name text,city text, marks int)''')
print("table created")
con.execute('''insert into stud_details(rno,name,city,marks) values (1,'Jenny','Ahemdabad',85)''')
con.execute('''insert into stud_details(rno,name,city,marks) values (2,'Suhana','Junagadh',96)''')
con.execute('''insert into stud_details(rno,name,city,marks) values (2,'William','Vadodara',74)''')
con.execute('''insert into stud_details(rno,name,city,marks) values (2,'Sarah','Surat',56)''')
con.commit()
print("data inserted successfully")

con.execute('''create table movie(name text, actor text, actress text, director text, yearofrelease int)''')

con.execute('''insert into movie(name ,actor ,actress ,director ,yearofrelease) values('Pushpa','AlluArjun','RasmikaMandhana','Rajamoli',2021)''')
con.execute('''insert into movie(name ,actor ,actress ,director ,yearofrelease) values('3idiots','Amirkhan','Karinakapoor','Rajamoli',2015)''')
con.commit()

data=con.execute('''select * from movie''')
for row in data:
   print('name',row[0])
   print('actor',row[1])
   print('actress',row[2])
   print('director',row[3])
   print('yearofrelease',row[4])
con.commit()