#%%
import glob

#%%
#read file name  from a folder
for fName in glob.glob('data/*'):
    print('filename is {0}'.format(fName))
    print('processing')

# %%
# push name of files in a folder
