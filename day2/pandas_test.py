#%%
import pandas as pd

dataArr = [
    ['persona', 21, 'male'],
    ['personb', 23, 'male'],
    ['personc', 25, 'male']
]
df= pd.DataFrame(dataArr,
                columns=['name','age','sex']
)
df1=pd.read_csv('data/persondb.csv')
colnames = df1.columns.tolist()
print(colnames)

names=df1['age'].values.tolist()
for i in names:
    print(i)
# %%
