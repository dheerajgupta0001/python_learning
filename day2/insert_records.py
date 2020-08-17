#%%
import cx_Oracle
con= cx_Oracle.connect("system/torreto@localhost")
cursor=con.cursor()
print(con.version)