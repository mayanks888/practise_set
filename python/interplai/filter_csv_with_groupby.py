import numpy as np
import pandas as pd
from collections import namedtuple

def split(df, group):
    data = namedtuple('data', ['country', 'territory'])
    # filename='img_name'
    # data = namedtuple('data', ['img_name', 'obj_class'])
    gb = df.groupby(group)
    return [data(filename, gb.get_group(x)) for filename, x in zip(gb.groups.keys(), gb.groups)]



bblabel=[]
data = pd.read_csv('/home/mayank_s/saved_work/interplai/OneDrive_1_30-01-2021/oct 15 - oct 31 - orders.csv')
print(data.head)

############################333
# mydata=data.groupby('country')
# print(data.groupby('country').count())
# index=mydata.groups['country'].values
# data.groupby(["Age", "Sex"])['Survived', 'Pclass'].mean()  # groupby only specific column
################################################
grouped = split(data, 'country')
##############################################
mydata = data.groupby(['country'], sort=True)
# print(data.groupby('class').count())
len_group = mydata.ngroups
mygroup = mydata.groups
#########################################3

###############################################3333
x = data.iloc[:, 0].values
y = data.iloc[:, 4:8].values
z = data.iloc[:, -1].values
##################################################
loop = 0
for ind, da1 in enumerate(sorted(mygroup.keys())):
    loop += 1
    # print(da1)
    index = mydata.groups[da1].values
    ###########33
###################################
# column_names = data.columns
df_numerics_only = data.select_dtypes(include=np.number)
column_nan=df_numerics_only.isnull().sum()
column_zero=df_numerics_only.isin(['0']).sum(axis=0)
# df_after_removing_nan = df_numerics_only.replace([np.inf, -np.inf], np.nan)
df_after_removing_nan = df_numerics_only.replace(np.nan, 0)

for column_name in df_after_removing_nan.columns:
    print(column_name)
    # print(f'before filter {df_after_removing_nan[column_name].mean()}')
    if column_name=="f_driver_avg_speed":
        df_after_removing_nan=df_after_removing_nan.replace([np.inf, -np.inf], 0)
    df_filter = df_after_removing_nan[df_after_removing_nan[column_name] != 0]

    mean=df_filter[column_name].mean()
    median=(df_filter[column_name].median())
    # mode=df_filter[column_name].mode()
    mode=df_filter[column_name].mode().values[0]

    max=(df_filter[column_name].max())
    min=(df_filter[column_name].min())
    nan_val=column_nan[column_name]
    zero_val=column_zero[column_name]

    # data_label = [column_name, mean, median, mode, max, min,nan_val,zero_val]
    dec_plc=3
    data_label = [column_name, round(mean,dec_plc), round(median,dec_plc), round(mode,dec_plc), round(max,dec_plc), round(min,dec_plc),nan_val,zero_val]
    bblabel.append(data_label)

columns = ['column_name', 'mean', 'median', 'mode', 'max', 'min','total_nan','total_zero']

df = pd.DataFrame(bblabel, columns=columns)
df.to_csv('filter_order.csv',index=False)