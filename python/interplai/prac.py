import csv
import pandas as pd
# columns = ['column_name', 'mean', 'median']
my_dict = {'1': 'aaa', '2': 'bbb', '3': 'ccc'}
my_dict = {'1': ['aaa','kkk'], '2': ['bbb','hhf'], '3': ['ccc','jjj']}
vo=pd.DataFrame(my_dict).T
vo.to_csv('cool.csv',index=False)
# with open('test.csv', 'w') as f:
#     for key in my_dict.keys():
#         f.write("%s,%s\n"%(key,my_dict[key]))