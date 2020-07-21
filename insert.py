import cx_Oracle
con= cx_Oracle.connect("system/torreto@localhost")
cursor=con.cursor()
print(con.version)
sql_insert= """ INSERT INTO task2 VALUES(10, 'DHEERAJ', 60000) """
cursor.execute(sql_insert)
print("QUERY INSERTED")
con.commit()
cursor.close()
con.close()