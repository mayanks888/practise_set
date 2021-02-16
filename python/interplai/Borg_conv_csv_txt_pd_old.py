import argparse
import os

import pandas as  pd


def write_txt1(list_val):
    # txt_file_name=txt_file_name+".txt"
    txt_file_name = "new2.txt"
    # txt_file_path=save_path+"/"+txt_file_name
    with open(txt_file_name, 'w') as f:
        for row in list_val:
            venue_lat, venue_lng, P_D, S_H, passenger_num = row
            bb = ((venue_lat), (venue_lng), (P_D), (S_H), (passenger_num))
            f.write(" ".join([str(a) for a in bb]) + '\n')



def write_txt2(list_val):
    # txt_file_name=txt_file_name+".txt"
    txt_file_name = "new3.txt"
    # txt_file_path=save_path+"/"+txt_file_name
    with open(txt_file_name, 'w') as f:
        for row in list_val:
            bb=tuple(row)
            f.write(",".join([str(a) for a in bb]) + '\n')

    f.close()

def main(args):

    # base_path =
    file_list = ['ann_arbor_ride_hailing_dataset.csv',
                 'ann_arbor_ride_sharing_dataset.csv',
                 "ann_arbor_orders_restaurants_dataset.csv", \
                 "ann_arbor_orders_supermarket_dataset.csv", \
                 "ann_arbor_orders_parcels_dataset.csv",
                 ]
    # list2=

    # csv_dict['ann_arbor_ride_hailing_dataset.csv']
    # csv_dict = {
    #     "brand": "Ford",
    #     "model": "Mustang",
    #     "year": 1964
    # }
    csv_dict = {
    'ann_arbor_ride_hailing_dataset.csv':args.rh,
    'ann_arbor_ride_sharing_dataset.csv':args.rh,
    "ann_arbor_orders_restaurants_dataset.csv":args.rt,
    "ann_arbor_orders_supermarket_dataset.csv":args.sm,
    "ann_arbor_orders_parcels_dataset.csv":args.pr
    }
    # score_dict[teritory_name]=[mycountry[0],total_entries, round(scores,4), round(score_per,4)]

    file_path = os.path.join(args.input_path, file_list[-1])
    samples = 5
    dec_plc = 2
    bblabel = []
    for val in csv_dict.keys():
        data = pd.read_csv(file_path)
        samples=csv_dict[val]
        sample_frame = data.sample(n=samples)
        feature_input = sample_frame.iloc[:, :].values
        # print(feature_input)
        for features in feature_input:
            # print(features)
            timestamp, date, distance, venue_name, venue_ratings, venue_category, \
            venue_lat, venue_lng, passenger_num, passenger_lat, passenger_lng = features
            data_label = [round(venue_lat, dec_plc), round(venue_lng, dec_plc), "P", "S", passenger_num]
            bblabel.append(data_label)
            data_label = [round(passenger_lat, dec_plc), round(passenger_lng, dec_plc), "D", "S", passenger_num]
            bblabel.append(data_label)

    print(bblabel)
    new_list=[]
    new_list.append(["PD"])
    new_list.append([2])
    new_list.append([50,100])
    new_list.append([" "])
    new_list.append([12])
    new_list.append([5])
    new_list.append([2.25])
    new_list.append([" "])
    new_list.append([50.00,50.00])
    new_list.append([0.00,0.00])
    new_list.append([100.00,100.00])
    new_list.append([100.00,0.00])
    new_list.append([0.00,1000.00])
    new_list.append([" "])
    1
    write_txt2(new_list+bblabel)


def parse_args():
    """Parse input arguments."""
    parser = argparse.ArgumentParser(description='Borgwarner csv to txt conversion..')
    parser.add_argument('--rh', help="ride_hailing",default=2)
    parser.add_argument('--rs', help="ride_sharing",default=2)
    parser.add_argument('--pr', help="parcel",default=2)
    parser.add_argument('--sm', help="supermarket",default=2)
    parser.add_argument('--rt', help="resturant",default=2)
    # parser.add_argument('--rh', help="ride_hailing",default=2)
    # parser.add_argument('--rs', help="ride_sharing")
    # parser.add_argument('--pr', help="parcel")
    # parser.add_argument('--sm', help="supermarket")
    # parser.add_argument('--rt', help="resturant")
    parser.add_argument('--count', help="No of txt files generation",default=1)
    # parser.add_argument('--output_path', help="Output folder")
    parser.add_argument('--input_path', help="path to PD csv files",
                        default="/home/mayank_s/saved_work/interplai/dataset/pd")
    parser.add_argument('--output_path', help="Path to generete txt files",
                        default='/home/mayank-s/PycharmProjects/Datasets/aptive/object_detect/j')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()
    print("\nStarting conversion... \n")
    # print('Reading parameters: {pt} \n'.format(pt=args.input_path))
    main(args)

# write_txt(bblabel)
