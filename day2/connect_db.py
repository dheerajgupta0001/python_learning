#%%
import cx_Oracle
con= cx_Oracle.connect("REPORTING_WEB_UI_UAT_LEARNING/uat_learning#@10.2.100.56:15210/ORCLWR")
cursor=con.cursor()
print(con.version)


#%%
sql_fetch= """ SELECT * FROM AC_TRANS_LINE_MASTER """
cursor.execute(sql_fetch)
row = cursor.fetchall()
print(row)  #records are fetched as a list of touples

#%%
for i in row:
    print(i[0],i[1])
for index, record in enumerate(row):
    print(index,record)
print("QUERY FETCHED")

# %%
