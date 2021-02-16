import argparse
import os
import random
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
        'ann_arbor_security_dataset.csv': [args.sec, "H"],
    }
    dec_plc = args.precision
    ###################################################################################################################
    # hard_coded text value
    new_list = []
    new_list.append(["C"])
    new_list.append([args.av])
    # cap=np.random.randint(low=50,high=100,size=args.AV)
    new_list.append(np.random.randint(low=50, high=100, size=(args.av)))
    new_list.append([" "])
    Total_target = (args.sec)
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
        school_list = []
        for val in csv_dict.keys():
            file_path = os.path.join(args.input_path, val)
            data = pd.read_csv(file_path)
            unique_series = list(data['ratings'].unique())
            ###############################33333
            samples = csv_dict[val]
            random_vals = random.sample(unique_series, int(samples[0]))
            for rv in random_vals:
                features = data.loc[data['ratings'] == rv]
                sample_frame = features.sample(n=1)
                # feature_input = sample_frame.iloc[:, :].values
                features = sample_frame.iloc[:, :].values.squeeze()
                _, lat, lng, name, ratings, categories = features
                data_label = ([round(lat, dec_plc), round(lng, dec_plc)])
                bblabel.append(data_label)

    ts = time.time()
    st = datetime.fromtimestamp(ts).strftime('%d_%m_%Y_%H_%M_%S_%f')
    text_file_name = "SEC_C_" + str(st) + ".txt"
    print("processing file : ", text_file_name)
    text_file_path = os.path.join(args.output_path, text_file_name)

    write_txt((new_list + bblabel), text_file_path)
    # writing summart
    summary_file_path = os.path.join(args.output_path, "summary_capacity.txt")
    write_summary(text_file_name, summary_file_path)


def parse_args():
    """Parse input arguments."""
    parser = argparse.ArgumentParser(description='Borgwarner csv to txt conversion..')
    # parser.add_argument('--sec', type=int, help="security", default=8)
    # parser.add_argument('--av', type=int, help="No of av", default=2)
    parser.add_argument('--sec', type=int, help="security", required=True)
    parser.add_argument('--av', type=int, help="No of av", required=True)
    parser.add_argument('--count', type=int, help="No of txt files generation", default=1)
    parser.add_argument('--precision', type=int, help="precision", default=5)
    parser.add_argument('--input_path', help="path to PD csv files",
                        default="/home/mayank_s/saved_work/interplai/dataset/capacity")
    parser.add_argument('--output_path', help="Path to generete txt files",
                        default='/home/mayank_s/saved_work/interplai/dataset/output')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()
    print("\nStarting conversion... \n")
    print('Reading parameters \n Security: {rh} \n'.format(rh=args.sec))
    main(args)
