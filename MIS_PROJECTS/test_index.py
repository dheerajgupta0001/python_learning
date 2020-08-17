'''
# main functon to run
'''
#%%
from datetime import datetime
from appConfig import getConfig
from read_angle_file import read_angle_data
from insert_angle_data import push_data_to_DB
import pandas as pd
# test the function for usage
angleFolder, connStr= getConfig('angleFolder','connStr')
print("angle in index file: {0}".format(angleFolder))
print(connStr)
print(angleFolder)

#%%
# call the function for reading the excel file data
df1 , df2= read_angle_data(angleFolder)


# %%
# push wide angle data
push_data_to_DB(df1, connStr)

# push adjacent angle record
push_data_to_DB(df2, connStr)

# %%
