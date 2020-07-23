import cx_Oracle
con= cx_Oracle.connect("system/torreto@localhost")
cursor=con.cursor()
print(con.version)
sql_fetch= """ SELECT * FROM task2 """
cursor.execute(sql_fetch)
row = cursor.fetchall()
print(row)  #records are fetched as a list of touples

for i in row:
    print(i[0],i[1])
for index, record in enumerate(row):
    print(index,record)
print("QUERY FETCHED")
