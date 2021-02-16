1. observed "inf " values in "f_driver_avg_speed" : converted to 0 as of now
2. few feature parameter "f_location_to_client_time","f_driver_avg_speed","f_d_speed", has large amount of 0 values but while considering the mean mode median those were not considered so need to check on this
3. for mean and other parameter, removed 0 for specific column rather than complete dataframe. need to check if this correct approach
4. mode is giving more than one values as of now accepted just one
5. "time taken for meters/second" does not seem to be right as many time parameter are 0