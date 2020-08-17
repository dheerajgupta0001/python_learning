
#%%
import cx_Oracle
con= cx_Oracle.connect("system/torreto@localhost")
cursor=con.cursor()
print(con.version)
sql_create = """
CREATE TABLE angle_data(
    id VARCHAR(10) PRIMARY KEY,
    Date TIMESTAMP NOT NULL,
    Wide angle pair VARCHAR(50) NOT NULL,
    Angular limit VARCHAR(30),
    violation VARCHAR(10),
    max(degree) VARCHAR(10),
    min(degree) VARCHAR(10)
)
"""
cursor.execute(sql_create)

# %%
