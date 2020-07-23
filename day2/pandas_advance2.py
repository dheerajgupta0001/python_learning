#%%
import pandas as pd
df =pd.read_csv('data/dc_data.csv', skiprows=2, nrows=96)

#%%
# set time block as index
df=df.set_index('Time Block')

# %%
dfsubset= df.loc[1:10, :]

# %%
avgval= df['KHARGONE-I(3)'].mean()
print("average of 'KHARGONE-I(3)' column is {0}",format(avgval))


# %%
'''
sumVal=[]
for itr in range(df.shape[0]):
    sum=0
    for col in df.columns.tolist()[3:-1]:
        sum= sum+ df[col].iloc[itr]
    sumVal.append(sum)
df['Total1']= sumVal
'''
# %%
df['Total2']= df[df.columns.tolist()[1:-1]].sum(axis=1)

# %%
