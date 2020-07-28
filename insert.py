#%%
import cx_Oracle
con= cx_Oracle.connect("system/torreto@localhost")
cursor=con.cursor()
print(con.version)
sql_insert= """ INSERT INTO ANGLE_DATA VALUES(1, to_date('1882-01-31','yyyy-mm-dd'),'KORBA-KALWA', '60', '0', '25', '15') """

#%%
cursor.execute(sql_insert)
print("QUERY INSERTED")
con.commit()
cursor.close()
con.close()

# %%
