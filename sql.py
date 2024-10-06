import sqlite3

conn=sqlite3.connect('main.db')
cursor=conn.cursor()
cursor.execute('CREATE TABLE STUDENT(name varchar(255),father varchar(255),gender varchar(50),DOB varchar(60),email varchar(255),mark INTEGER,rank INTEGER,telephone INTEGER,Address varchar(200),coursetype TEXT,coursename varchar(100))')
#cursor.execute("DROP TABLE STUDENT")
conn.commit()

conn.close()

