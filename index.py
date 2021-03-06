#%%
import cx_Oracle

#%%
con= cx_Oracle.connect("system/torreto@localhost")
cursor= con.cursor()
print(con.version)
sq_create = """
CREATE TABLE angle_data1(
    ID NUMBER(10) GENERATED BY DEFAULT ON NULL AS IDENTITY,
    DATE_TIME DATE NOT NULL,
    WIDE_ANGLE_PAIR VARCHAR(40) NOT NULL,
    angular_limit NUMBER(10) NOT NULL,
    violation FLOAT(10),
    max_degree FLOAT(10),
    min_degree FLOAT(10),
    UNIQUE(DATE_TIME, WIDE_ANGLE_PAIR),
    PRIMARY KEY(ID)
)
"""
#%%
cursor.execute(sq_create)

#%%
print("table created")
