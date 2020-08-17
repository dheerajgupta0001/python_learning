# %%
import pandas as pd

def read_xcl(input_excel):
    # read complete excel file
    xls = pd.ExcelFile(input_excel)
    #xls = pd.ExcelFile('Angle_violation.xlsm')

    # get date from file name
    temp_list= input_excel.split('_')[2:]
    temp_list[-1]=temp_list[-1].split('.')[0]
    dat='-'.join(temp_list)
    print("Date in called function: {0}".format(dat))

    # read excel sheet final one
    df1 = pd.read_excel(xls, 'Final', skiprows=6, skipfooter=6)
    wide = ['wide', 'wide','wide', 'wide','wide', 'wide','wide', 'wide','wide', 'wide','wide']
    df1['Type'] = wide
    df1['Unnamed: 0'] = dat

    
    # read data for adjacent angle
    df2 = pd.read_excel(xls, 'Final', skiprows=19, skipfooter=1)
    adj = ['adj','adj','adj']
    df2['Type'] = adj
    df2['Unnamed: 0'] = dat

    # rename a column
    df1.rename(columns={'Unnamed: 0': 'Date'}, inplace=True)
    df2.rename(columns={'Unnamed: 0': 'Date'}, inplace=True)

    # drop a column
    df1 = df1.drop("Sr. No.", axis=1)
    df2 = df2.drop("Sr. No.", axis=1)
    return df1, df2
# %%
