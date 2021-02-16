import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

bblabel=[]
data = pd.read_csv('/home/mayank_s/saved_work/interplai/OneDrive_1_30-01-2021/oct 15 - oct 31 - orders.csv')
print(data.head)
data['time taken for meters/second'] = data["f_location_to_client_distance"]/data['f_location_to_client_time']
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

    plt.figure()
    df_filter[column_name].plot.hist(orientation="vertical", cumulative=False)
    # df_filter[column_name].plot()
    plt.show()

columns = ['column_name', 'mean', 'median', 'mode', 'max', 'min','total_nan','total_zero']

df = pd.DataFrame(bblabel, columns=columns)
# df.to_csv('filter_order.csv',index=False)


# # df_after_removing_nan.boxplot()
# from pandas.plotting import scatter_matrix
# scatter_matrix(df_filter, alpha=0.2, figsize=(6, 6), diagonal='kde')
# # plt.show()
# plt.savefig('books_read.png')
