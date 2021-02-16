import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
feature_list=['client_geo.0', 'client_geo.1', 'order_inserted_time', 'location_geo.0', 'location_geo.1', 'partner_assigned_time', 'partner_delivered_time_max', 'partner_accepted_time', 'f_location_to_client_distance', 'f_location_to_client_time', 'f_driver_avg_speed', 'f_total_time', 'driver_geo.0', 'driver_geo.1', 'driver_delivering_time', 'driver_delivered_time', 'time taken for meters/second']
# feature_list=['client_geo.0', 'client_geo.1', 'order_inserted_time', 'location_geo.0', 'location_geo.1', 'partner_assigned_time', 'partner_delivered_time_max', 'partner_accepted_time', 'f_location_to_client_distance', 'f_location_to_client_time', 'f_driver_avg_speed', 'f_total_time', 'driver_geo.0', 'driver_geo.1', 'driver_delivering_time', 'driver_delivered_time']
# feature_list=['client_geo.0', 'client_geo.1', 'location_geo.1', 'partner_assigned_time', 'partner_delivered_time_max', 'partner_accepted_time', 'f_location_to_client_distance', 'f_location_to_client_time', 'time taken for meters/second']
# feature_list=['client_geo.0', 'client_geo.1']

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
# feature_name='time taken for meters/second'
feature_name='client_geo.0'
feature_name='f_location_to_client_distance'

fig, axs = plt.subplots(5,4, figsize=(15, 6), facecolor='w', edgecolor='k')
fig.subplots_adjust(hspace = .5, wspace=.001)
axs = axs.ravel()

for i,feature_name in enumerate(feature_list):
    #######################################
    df_filter = df_after_removing_nan[df_after_removing_nan[feature_name] != 0]
    index=df_filter[feature_name].values
    ###################################
    i=i+1
    ar =index
    x_val=np.arange(0,index.size)
    # axs[i]= plt.scatter(x_val, ar)
    axs[i].contourf(np.random.rand(10, 10), 5, cmap=plt.cm.Oranges)
    axs[i].set_title(str(feature_name))

    # plt.subplot(5, 4, i + 1), plt.scatter(x_val, ar)
    # plt.title(feature_name,pad=15)
    #################################
# plt.subplots_adjust(bottom=0.1, right=0.8, top=0.9)
# plt.subplots_adjust(hspace = .5, wspace=.001)
# plt.tight_layout()
plt.show()
plt.savefig('graph.png', dpi = 300)

