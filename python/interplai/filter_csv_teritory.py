import numpy as np
import pandas as pd
from collections import namedtuple

data = pd.read_csv('/home/mayank_s/saved_work/interplai/OneDrive_1_30-01-2021/oct 15 - oct 31 - orders.csv')
# print(data.head)
data['time taken for meters/second'] = data["f_location_to_client_distance"]/data['f_location_to_client_time']

index=data.groupby("territory").count().vertical_id
#####################################333
country_list=list(data['territory'].unique())
for teritory_name in country_list:
    print(teritory_name)
    ##################33333
    total_entries=index[teritory_name]
    ######################3
    mydata=data.copy()
    bblabel = []
    mydata.drop(mydata.loc[mydata['territory']!=teritory_name].index, inplace=True)
    ##########################3
#############################################
# column_names = data.columns
    df_numerics_only = mydata.select_dtypes(include=np.number)
    column_nan=df_numerics_only.isnull().sum()
    column_zero=df_numerics_only.isin(['0']).sum(axis=0)
    # df_after_removing_nan = df_numerics_only.replace([np.inf, -np.inf], np.nan)
    df_after_removing_nan = df_numerics_only.replace(np.nan, 0)

    for column_name in df_after_removing_nan.columns:
        # print(column_name)
        # print(f'before filter {df_after_removing_nan[column_name].mean()}')
        if column_name=="f_driver_avg_speed":
            df_after_removing_nan=df_after_removing_nan.replace([np.inf, -np.inf], 0)
        df_filter = df_after_removing_nan[df_after_removing_nan[column_name] != 0]

        mean=df_filter[column_name].mean()
        median=(df_filter[column_name].median())
        mode=df_filter[column_name].mode()
        # mode=df_filter[column_name].mode().values[0]

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
    pdf_filename="teritory/"+teritory_name+"_"+str(total_entries)+".csv"
    df.to_csv(pdf_filename,index=False)