
# Written By: Jodi Gunawan
# Date: Nov 15th, 2018
# Description:  This script creates csv file from xml input file under the file train_labels

import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET
import argparse

parser = argparse.ArgumentParser(description='This script creates csv file from xml input file under the file train_labels')
parser.add_argument('--train_or_test', required=True, help='Enter train or test depending on whether you are looking in folder train_labels or test_labels')

args = parser.parse_args()

def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():
    os.chdir('../../data')
    if args.train_or_test == 'train':
        for directory in ['train_labels']:
            image_path = os.path.join(os.getcwd(), format(directory))
            xml_df = xml_to_csv(image_path)
            xml_df.to_csv('{}.csv'.format(directory), index=None)
            print('Successfully converted xml to csv.')

    if args.train_or_test == 'test':
        for directory in ['test_labels']:
            image_path = os.path.join(os.getcwd(),format(directory))
            xml_df = xml_to_csv(image_path)
            xml_df.to_csv('data/{}.csv'.format(directory), index=None)
            print('Successfully converted xml to csv.')

if __name__ == '__main__':
    main()
