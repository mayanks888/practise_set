import numpy as np
import pandas as pd

data = pd.read_csv('/home/mayank_s/saved_work/interplai/OneDrive_1_30-01-2021/oct 15 - oct 31 - orders.csv')
print(data.head)
cool = list(data.columns)
# print(cool)
df = df_numerics_only = data.select_dtypes(include=np.number)
# checking for null values
print(f"total null before change to nan {df.isnull().sum()}")
print(f"total 0 before change to nan {df.isin(['0']).sum(axis=0)}")
df_after_removing_nan=df.replace(np.nan, 0)

# data['Age'].isnull().sum()
print(f"total null after after to nan {df_after_removing_nan.isnull().sum()}")
print(f"total 0 after change to nan {df_after_removing_nan.isin([0]).sum(axis=0)}")
# df[df == 0].sum(axis=0)
print((df_after_removing_nan['partner_assigned_time'] == 0).sum())
# 1
# print("\n----------- Calculate Mean -----------\n")
# print(df.mean())
#
# print("\n----------- Calculate Median -----------\n")
# print(df.median())
#
# print("\n----------- Calculate Mode -----------\n")
# print(df.mode())
#
# print("\n----------- Calculate max -----------\n")
# print(df.max())
# print("\n----------- describe------------------\n")
print(df.describe())
for col in df_after_removing_nan.columns:
    print(col)
    print(f'before filter {df_after_removing_nan[col].mean()}')
    # (df_after_removing_nan[df_after_removing_nan[col] > 0])
    df_filter = df_after_removing_nan[df_after_removing_nan[col] != 0]
    print(f'after filter{df_filter[col].mean()}')
    print(df_filter[col].median())
    print(df_filter[col].mode())
    print(df_filter[col].max())
    print(df_filter[col].min())
