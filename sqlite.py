import sqlite3

##connect to Sqlite 

connection=sqlite3.connect("student.db")

#create a cursor object to insert reccord, create table

cursor= connection.cursor()

##cerarte the table
table_info="""
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), 
SECTION VARCHAR(25));

"""
cursor.execute(table_info)

##Insertb some more records

cursor.execute('''Insert Into Student values ('Krish','Data Science','A')''')
cursor.execute('''Insert Into Student values ('Zeel','Data Science','B')''')
cursor.execute('''Insert Into Student values ('naman','Data Science','A')''')
cursor.execute('''Insert Into Student values ('yash','DevOps','A')''')
cursor.execute('''Insert Into Student values ('smit','DevOps','A')''')

##Display all the records 

print("The inserted record are ")
data=cursor.execute('''select * from student''')
for row in data:
    print(row)

connection.commit()
connection.close()