#%%
import pandas as pd
df =pd.read_csv('data/dc_data.csv', skiprows=2,nrows=96)
df.to_csv('data/out.csv',index=False)
#shape of dataframe
dfshape=df.shape
print('The shape of dtaframe is {0}'.format(dfshape))

# %%
#to select only selected columns
dfsubset= df[['Time Block','KAPS(0)']]

# %%
#from time bock 3 to 10
dfsubset= df[(df['Time Block']>=3)& (df['Time Block']<=10)][['Time Block','KAPS(0)']]

# %%
df1= df.iloc[3:6,6:8]

# %%
