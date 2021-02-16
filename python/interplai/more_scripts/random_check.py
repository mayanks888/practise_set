import numpy as np
import pandas as pd
import matplotlib.pyplot as pp

bblabel=[]
#enter location of csv
csv_path="/home/mayank_s/saved_work/interplai/OneDrive_1_30-01-2021/oct 15 - oct 31 - orders.csv"
data = pd.read_csv(csv_path)
data['time taken for meters/second'] = data["f_location_to_client_distance"]/data['f_location_to_client_time']
# column_names = data.columns
df_numerics_only = data.select_dtypes(include=np.number)
#changing all inf to 0
df_numerics_only=df_numerics_only.replace([np.inf, -np.inf], 0)
column_nan=df_numerics_only.isnull().sum()
column_zero=df_numerics_only.isin(['0']).sum(axis=0)
# df_after_removing_nan = df_numerics_only.replace([np.inf, -np.inf], np.nan)
df_after_removing_nan = df_numerics_only.replace(np.nan, 0)
############################################################
feature_name='time taken for meters/second'
# feature_name='client_geo.0'
# feature_name='f_location_to_client_distance'

#######################################
df_filter = df_after_removing_nan[df_after_removing_nan[feature_name] != 0]
index=df_filter[feature_name].values


#############################333
ar =index
# pp.plot(ar)
x_val=np.arange(0,index.size)
pp.scatter(x_val,ar)
# pp.xlim(0,10)
# pp.ylim(0, 20)
pp.title(feature_name)
pp.show()

#################################


for _ in range(10):
    pyindex=np.random.choice(index, size=100, replace=False)
    mean=pyindex.mean()
    print(mean)
    x_val = np.arange(0, pyindex.size)
    pp.scatter(x_val, pyindex)
    # pp.xlim(0,10)
    # pp.ylim(0, 20)
    pp.title(feature_name)

    pp.show()


