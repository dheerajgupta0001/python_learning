#%%
from datetime import datetime
from appConfig import getConfig
from xcel_read import read_xcl
import pandas as pd
# test the function for usage
angle= getConfig('angleFolder')
print("angle in index file: {0}".format(angle))

'''temp_list= angle.split('_')[2:]
temp_list[-1]=temp_list[-1].split('.')[0]
dat='-'.join(temp_list)
print(dat)'''
#%%
# call the function for reading the excel file data
df1 , df2= read_xcl(angle)
#df_adj= read_xcl(angle)

# %%
