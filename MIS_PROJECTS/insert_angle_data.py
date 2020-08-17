'''
# function to push data into tables 
'''
#%%
import cx_Oracle
#%%

def push_data_to_DB(df, connStr):
    # prepare list of angle data
    #print(df['% violation'])
    df['max (degrees)'] = df['max (degrees)'].apply(lambda x: round(x,2))
    df['min (degrees)'] = df['min (degrees)'].apply(lambda x: round(x,2))
    df['Angular limit'] = df['Angular limit'].astype(str)
    df['% violation'] = df['% violation'].astype(str)
    df['max (degrees)'] = df['max (degrees)'].astype(str)
    df['min (degrees)'] = df['min (degrees)'].astype(str)
    recrd= df.to_records(index=False)
    data= list(recrd)

    # create connection to database for pushing records
    con= cx_Oracle.connect(connStr)
    cursor=con.cursor()
    print(con.version)
    insert_sql = "INSERT INTO DAILY_ANGLE_DATA(DATE_TIME,WIDE_ANGLE_PAIR,ANGULAR_LIMIT,VIOLATION,MAX_DEGREE,MIN_DEGREE,TYPE) VALUES(:col1,:col2,:col3,:col4,:col5,:col6,:col7)"
    cursor.execute("ALTER SESSION SET NLS_DATE_FORMAT = 'YYYY-MM-DD' ")
    
    cursor.executemany(insert_sql, data)
    # closing the connection
    con.commit()
    print("Record Inserted")
    cursor.close()
    con.close()



# %%