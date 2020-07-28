'''
# function to push data into tables 
'''
#%%
import cx_Oracle
#%%

def pushData(df, connStr):
    # prepare list of angle data
    df['Angular limit'] = df['Angular limit'].astype(str)
    df['% violation'] = df['% violation'].astype(str)
    df['max (degrees)'] = df['max (degrees)'].astype(str)
    df['min (degrees)'] = df['min (degrees)'].astype(str)
    recrd= df.to_records(index=False)
    data= list(recrd)
    #print(data)
    print(" Data typr of each columnn")
    tmp= data[0]
    print([type(i) for i in tmp])

    # print the list of data
    #print(len(data))

    # create connection to database for pushing records
    con= cx_Oracle.connect(connStr)
    cursor=con.cursor()
    print(con.version)
    insert_sql = "INSERT INTO ANGLE_DATA1(DATE_TIME,WIDE_ANGLE_PAIR,ANGULAR_LIMIT,VIOLATION,MAX_DEGREE,MIN_DEGREE,TYPE) VALUES(:col1,:col2,:col3,:col4,:col5,:col6,:col7)"
    cursor.execute("ALTER SESSION SET NLS_DATE_FORMAT = 'YYYY-MM-DD' ")
    
    cursor.executemany(insert_sql, data)
    '''insert_sql = "INSERT INTO ANGLE_DATA1(DATE_TIME,WIDE_ANGLE_PAIR,ANGULAR_LIMIT,VIOLATION,MAX_DEGREE,MIN_DEGREE,TYPE)\
         VALUES('1998-01-01', 'Korba-Kalwa', '65', '0', '37.18', '29.21000000000001', 'wide')"
    cursor.execute(insert_sql)'''
    # closing the connection
    con.commit()
    print("Record Inserted")
    cursor.close()
    con.close()



# %%
