#print("hello word")
import cx_Oracle
con= cx_Oracle.connect("system/torreto@localhost")
cursor=con.cursor()
print(con.version)
sq_create = """
CREATE TABLE task2(
    id VARCHAR(10) NOT NULL,
    name VARCHAR(10) NOT NULL,
    salary NUMBER(6) NOT NULL
)
"""

cursor.execute(sq_create)
print("dheeraj")
