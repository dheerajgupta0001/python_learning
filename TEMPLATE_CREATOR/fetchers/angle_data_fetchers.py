#%%
from docx.shared import Pt
from docxtpl import DocxTemplate, InlineImage
import cx_Oracle
import argparse
import pandas as pd
from datetime import datetime

# get an instance of argument parser from argparse module
parser = argparse.ArgumentParser()

# setup firstname, lastname arguements
parser.add_argument('--startdate', help="Enter start date here")
parser.add_argument('--enddate', help="Enter end date here")

# get the dictionary of command line inputs entered by the user
args = parser.parse_args()

# access each command line input from the dictionary
sDate = args.startdate
eDate = args.enddate

tmplPath = "assets/docxtpl/template_example.docx"
doc = DocxTemplate(tmplPath)

#%%
# connection creation
try:
    connection= cx_Oracle.connect("mis_warehouse/wrldc#123@10.2.100.56:15210/ORCLWR")
    cursor=connection.cursor()
    print(connection.version)
    
    print("wide angle report")
    sql_fetch =""" SELECT * FROM (select distinct wide_angle_pair as pair, angular_limit, violation \
        from daily_angle_data where type = 'wide' and date_time BETWEEN TO_DATE(:col1, 'YYYY-MM-DD')\
                and TO_DATE(:col2, 'YYYY-MM-DD')) A\
        left JOIN (select MAX(max_degree), min(min_degree), wide_angle_pair from daily_angle_data\
            where type= 'wide' and date_time BETWEEN TO_DATE(:col1, 'YYYY-MM-DD')\
                and TO_DATE(:col2, 'YYYY-MM-DD') GROUP BY wide_angle_pair) B\
                    on A.pair = B.wide_angle_pair"""

    cursor.execute("ALTER SESSION SET NLS_DATE_FORMAT = 'YYYY-MM-DD' ")
    df= pd.read_sql(sql_fetch, params={'col1': sDate, 'col2': eDate}, con=connection)
    '''cursor.execute(sql_fetch, {'col1':sDate, 'col2':eDate})
    row = cursor.fetchall()'''
    #print(row)  #records are fetched as a list of touples

    '''for index, record in enumerate(row):
        print(index,record)'''
    
    print("Adjacent angle report")
    sql_fetch =""" SELECT * FROM (select distinct wide_angle_pair, angular_limit, violation \
        from daily_angle_data where type = 'adj' and date_time BETWEEN TO_DATE(:col1, 'YYYY-MM-DD')\
                and TO_DATE(:col2, 'YYYY-MM-DD')) A\
        left JOIN (select MAX(max_degree), min(min_degree), wide_angle_pair from daily_angle_data\
            where type= 'adj' and date_time BETWEEN TO_DATE(:col1, 'YYYY-MM-DD')\
                and TO_DATE(:col2, 'YYYY-MM-DD') GROUP BY wide_angle_pair) B\
                    on A.wide_angle_pair = B.wide_angle_pair"""

    cursor.execute("ALTER SESSION SET NLS_DATE_FORMAT = 'YYYY-MM-DD' ")
    cursor.execute(sql_fetch, {'col1':sDate, 'col2':eDate})
    row = cursor.fetchall()
    #print(row)  #records are fetched as a list of touples

    for index, record in enumerate(row):
        print(index,record)
    print("QUERY FETCHED")

except:
    print('Error while fetching data from db')
finally:
    # closing database cursor and connection
    if cursor is not None:
        cursor.close()
    connection.close()
wideAngleData = []
for i in df.index:
    tempDict={
        'wide_angle_pair': df['WIDE_ANGLE_PAIR'][i],
        'angular_limit': df['ANGULAR_LIMIT'][i],
        'violation': df['VIOLATION'][i],
        'max_degree': df['MAX(MAX_DEGREE)'][i],
        'min_degree ': df['MIN(MIN_DEGREE)'][i],
    }
    wideAngleData.append(tempDict)
print(type(wideAngleData))
context = {
    'yr_str': "2020-21",
    'wk_num': 18,
    'st_dt': sDate,
    'end_dt': eDate,
    'angleData': wideAngleData
}
doc.render(context)
doc.save("assets/docxtpl/report_created.docx")