'''
# main functon to run
'''
#%%
from datetime import datetime
from appConfig import getConfig
from xcel_read import read_xcl
from insertRecords import pushData
import pandas as pd
# test the function for usage
angleFolder, connStr= getConfig('angleFolder','connStr')
print("angle in index file: {0}".format(angleFolder))
print(connStr)

'''
temp_list= angle.split('_')[2:]
temp_list[-1]=temp_list[-1].split('.')[0]
dat='-'.join(temp_list)
print(dat)
'''
#%%
# call the function for reading the excel file data
df1 , df2= read_xcl(angleFolder)
#df_adj= read_xcl(angle)

# %%
# push wide angle data
pushData(df1, connStr)

# push adjacent angle record
pushData(df2, connStr)

# %%
