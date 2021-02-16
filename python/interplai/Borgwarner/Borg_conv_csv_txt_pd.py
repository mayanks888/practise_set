import argparse
import os
import time
from datetime import datetime

import numpy as np
import pandas as  pd


def write_txt(list_val, txt_file_path):
    with open(txt_file_path, 'w') as f:
        for row in list_val:
            bb = tuple(row)
            f.write(",".join([str(a) for a in bb]) + '\n')
    f.close()


def write_summary(list_val, txt_file_path):
    with open(txt_file_path, 'a') as f:
        f.write('\n' + str(list_val))
    f.close()


def main(args):
    csv_dict = {
        'ann_arbor_ride_hailing_dataset.csv': [args.rh, "H"],
        'ann_arbor_ride_sharing_dataset.csv': [args.rs, "S"],
        "ann_arbor_orders_restaurants_dataset.csv": [args.rt, "S"],
        "ann_arbor_orders_supermarkets_dataset.csv": [args.sm, "S"],
        "ann_arbor_orders_parcels_dataset.csv": [args.pr, "S"],
        'ann_arbor_ems_dataset.csv': [args.ems, "H"]
    }
    dec_plc = args.precision
    ###################################################################################################################
    # hard_coded text value
    new_list = []
    new_list.append(["PD"])
    new_list.append([args.av])
    # cap=np.random.randint(low=50,high=100,size=args.AV)
    new_list.append(np.random.randint(low=50, high=100, size=(args.av)))
    new_list.append([" "])
    Total_target = (args.rh + args.rs + args.rt + args.sm + args.pr + + args.ems) * 2
    new_list.append([Total_target])
    new_list.append([5])
    new_list.append([2.25])
    new_list.append([" "])
    new_list.append([50.00, 50.00])
    new_list.append([0.00, 0.00])
    new_list.append([100.00, 100.00])
    new_list.append([100.00, 0.00])
    new_list.append([0.00, 100.00])
    new_list.append([" "])
    ###################################################################################################################
    for counter in range(int(args.count)):
        bblabel = []
        for val in csv_dict.keys():
            # if val == "ann_arbor_ems_dataset":
            file_path = os.path.join(args.input_path, val)
            data = pd.read_csv(file_path)
            samples = csv_dict[val]
            sample_frame = data.sample(n=int(samples[0]))
            feature_input = sample_frame.iloc[:, :].values
            if val == "ann_arbor_ems_dataset.csv":
                for features in feature_input:
                    hospital_lat, hospital_lng, patient_lat, patient_lng = features[-6], features[-5], features[-2], \
                                                                           features[-1]
                    patient_no = 1
                    data_label = [round(patient_lat, dec_plc), round(patient_lng, dec_plc), "P", samples[1],
                                  patient_no]
                    bblabel.append(data_label)
                    data_label = [round(hospital_lat, dec_plc), round(hospital_lng, dec_plc), "D", samples[1],
                                  patient_no]
                    bblabel.append(data_label)
            else:
                for features in feature_input:
                    timestamp, date, distance, venue_name, venue_ratings, venue_category, \
                    venue_lat, venue_lng, passenger_num, passenger_lat, passenger_lng = features
                    data_label = [round(venue_lat, dec_plc), round(venue_lng, dec_plc), "P", samples[1], passenger_num]
                    bblabel.append(data_label)
                    data_label = [round(passenger_lat, dec_plc), round(passenger_lng, dec_plc), "D", samples[1],
                                  passenger_num]
                    bblabel.append(data_label)

    ts = time.time()
    st = datetime.fromtimestamp(ts).strftime('%d_%m_%Y_%H_%M_%S_%f')
    text_file_name = "PD_" + str(st) + ".txt"
    print("processing file : ", text_file_name)
    text_file_path = os.path.join(args.output_path, text_file_name)
    write_txt((new_list + bblabel), text_file_path)

    ###########################
    # writing summart
    summary_file_path = os.path.join(args.output_path, "summary_pd.txt")
    write_summary(text_file_name, summary_file_path)


def parse_args():
    """Parse input arguments."""
    parser = argparse.ArgumentParser(description='Borgwarner csv to txt conversion..')
    ##########################################################################
    # parser.add_argument('--rh', type=int, help="ride_hailing", default=1)
    # parser.add_argument('--rs', type=int, help="ride_sharing", default=1, )
    # parser.add_argument('--pr', type=int, help="parcel", default=1)
    # parser.add_argument('--sm', type=int, help="supermarket", default=1)
    # parser.add_argument('--rt', type=int, help="resturant", default=1)
    # parser.add_argument('--ems', type=int, help="ems", default=1)
    # parser.add_argument('--av', type=int, help="No of av", default=3)
    #############################################################################3
    parser.add_argument('--rh', type=int, help="ride_hailing", required=True)
    parser.add_argument('--rs', type=int, help="ride_sharing", required=True)
    parser.add_argument('--pr', type=int, help="parcel", required=True)
    parser.add_argument('--sm', type=int, help="supermarket", required=True)
    parser.add_argument('--rt', type=int, help="restuarant", required=True)
    parser.add_argument('--ems', type=int, help="ems", required=True)
    parser.add_argument('--av', type=int, help="No of av", required=True)
    ##########################################################################
    parser.add_argument('--count', type=int, help="No of txt files generation", default=1)
    parser.add_argument('--precision', type=int, help="precision", default=5)
    parser.add_argument('--input_path', help="path to PD csv files",
                        default="/home/mayank_s/saved_work/interplai/dataset/pd")
    parser.add_argument('--output_path', help="Path to generete txt files",
                        default='/home/mayank_s/saved_work/interplai/dataset/output')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()
    print("\nStarting conversion... \n")
    print(
        'Reading parameters \n Ride Hailing: {rh} \n Ride Sharing: {rs} \n Parcel: {pr} \n Supermarket: {sm}\n Resturant: {rt}\n ems: {ems}  \n Total generated txt files: {tf}'
            .format(rh=args.rh, rs=args.rs, pr=args.pr, sm=args.sm, rt=args.rt, ems=args.ems, tf=args.count))
    main(args)
