import numpy as np
import pandas as pd
import os
#enter location of csv
csv_path="/home/mayank_s/saved_work/interplai/OneDrive_1_30-01-2021/oct 15 - oct 31 - orders.csv"
data = pd.read_csv(csv_path)

#creating another column for tme taken for metric/second
data['time taken for meters/second'] = data["f_location_to_client_distance"]/data['f_location_to_client_time']
index=data.groupby("territory").count().vertical_id


#select which feature list to be used
feature_list=['client_geo.0', 'client_geo.1', 'order_inserted_time', 'location_geo.0', 'location_geo.1', 'partner_assigned_time', 'partner_delivered_time_max', 'partner_accepted_time', 'f_location_to_client_distance', 'f_location_to_client_time', 'f_driver_avg_speed', 'f_total_time', 'driver_geo.0', 'driver_geo.1', 'driver_delivering_time', 'driver_delivered_time', 'time taken for meters/second']
# feature_list = list(data.columns)

#Enter for score matrix
score_dict={"Teritory":["Total Entry","Scores","score %"]}
score_matrix = {'client_geo.0': 1,
                'client_geo.1': 1,
                'order_inserted_time': 1,
                'location_geo.0': 1,
                'location_geo.1': 1,
                'driver_geo.0': 1,
                'driver_geo.1': 1,
                'partner_assigned_time': 0.6,
                'partner_delivered_time_max': 0.6,
                'partner_accepted_time': 0.4,
                'f_location_to_client_distance': 0.6,
                'f_location_to_client_time': 0.6,
                'f_driver_avg_speed': 0.4,
                'f_total_time': 0.4,
                'driver_delivering_time': 0.6,
                'driver_delivered_time': 0.6
                }

country_list=list(data['territory'].unique())

terlist=['5d5496c9962d7404c53b8902','5d61766418a1bd7c28da5823']

#looping through all the country name
for country_name in country_list:
    if not country_name in terlist:
        continue
    scores=0
    #total entries in for each country
    total_entries=index[country_name]
    mydata=data.copy()
    bblabel = []
    mydata.drop(mydata.loc[mydata['territory']!=country_name].index, inplace=True)
    df_numerics_only = mydata.select_dtypes(include=np.number)
    #finding total number of empty and 0 entry
    column_nan=df_numerics_only.isnull().sum()
    column_zero=df_numerics_only.isin(['0']).sum(axis=0)
    # df_after_removing_nan = df_numerics_only.replace([np.inf, -np.inf], np.nan)
    df_after_removing_nan = df_numerics_only.replace(np.nan, 0)
    for column_name in df_after_removing_nan.columns:
        if not column_name in feature_list:
            continue
        # print(column_name)
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
        # weight  for  specific features
        if column_name in score_matrix:
            weight_val=score_matrix[column_name]
            #calculate factor based on the weight score
            factor=((total_entries-(nan_val+zero_val))/total_entries)*weight_val
            scores=scores+factor

            # scores=scores+(((total_entries-(nan_val+zero_val))/total_entries)*weight_val)
            print(country_name,column_name, factor)
        score_per = (scores/11.8)*100
        dec_plc=3 #no of decimal place in order to represent in csv
        data_label = [column_name, round(mean,dec_plc), round(median,dec_plc), round(mode,dec_plc), round(max,dec_plc), round(min,dec_plc),nan_val,zero_val]
        bblabel.append(data_label)

    score_dict[country_name]=[total_entries, round(scores,4), round(score_per,4)]

    columns = ['column_name', 'mean', 'median', 'mode', 'max', 'min','total_nan','total_zero']
    df = pd.DataFrame(bblabel, columns=columns)
    #base folder path
    base_path="territory"
    pdf_filename=base_path+"/"+country_name+"_"+str(total_entries)+".csv"
    # check if path exist
    if not os.path.exists(base_path):
        # shutil.rmtree(g_args.out_dir)
        os.makedirs(base_path)
    df.to_csv(pdf_filename,index=True)

df_rank=pd.DataFrame(score_dict).T
df_rank.to_csv(base_path+'/Ranking_teritory.csv',index=True)