# Convert CSV to txt
## Dependencies

* python > 3.5
* numpy
* pandas


###1. For Pickup/Drop:

~~~
 python Borg_conv_csv_txt_pd.py --rs 2 --rh 1 --pr 2 --rt 1 --sm 2 --ems 1 --av 2 --count 1 --input_path "Path of all PD csv" --output_path "path to generate all txt files"
~~~

rs : Ride sharing 

rh : Ride Hailing

pr : Parcel

rt : Resturant

sm : Supermarket (Grocery)

ems : emergency service

av: No of AV's

count : No of random text files to be generated'
(default = 1)

###2. For School Bus (capacity):

~~~
 python Borg_conv_csv_txt_sb.py --sb 3 --av 2 --count 1 --input_path "Path of all capacity csv" --output_path "path to generate all txt files"
~~~


sb : No of entries 

av: No of AV's

count : No of random text files to be generated'
(default = 1)

###3. For Security (capacity:

~~~
 python Borg_conv_csv_txt_sec.py --sec 10 --av 2 --count 1 --input_path "Path of all capacity csv" --output_path "path to generate all txt files"
~~~


sb : No of entries 

av: No of AV's

count : No of random text files to be generated'
(default = 1)