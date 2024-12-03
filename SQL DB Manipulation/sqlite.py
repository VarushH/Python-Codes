import sqlite3

#Connect to sqllite
conncetion = sqlite3.connect("student.db")

#Create a cursor object to insert record, create table
cursor = conncetion.cursor()

#Create Table
table_info = """
create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25),MARKS INT)
"""

cursor.execute(table_info)

#Insert some more records
cursor.execute('''Insert Into STUDENT values('Varush','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('John','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Mukesh','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Jacob','DEVOPS','A',50)''')
cursor.execute('''Insert Into STUDENT values('Dipesh','DEVOPS','A',35)''')

# Display all the records
print('The inserted Records are')
data = cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

#Commit your changes in database
conncetion.commit()
conncetion.close()