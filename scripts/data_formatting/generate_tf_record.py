# Written By: Michael Milic
# Date: Nov 15th, 2018
# Description:  This script will take the csv input file and from it will create generate a tf records file. 

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

import os
import io
import argparse
import pandas as pd
import tensorflow as tf

from PIL import Image
from object_detection.utils import dataset_util
from collections import namedtuple, OrderedDict

parser = argparse.ArgumentParser(description='This script will take the csv input file and from it will create generate a tf records file.')
parser.add_argument('--csv_input',  required=True, help='Path to the CSV input')
parser.add_argument('--output_path', required=True, help='Path to output TFRecord')
parser.add_argument('--train_or_test', required=True, help='Enter train or test depending on whether you are looking in folder train_labels or test_labels')

args = parser.parse_args()

# this function checks takes a row label as input, and returns true if the row label is 'Gate'
def class_text_to_int(row_label):
    if row_label == 'Gate':
        return 1
    else:
        None


def split(df, group):
    data = namedtuple('data', ['filename', 'object'])
    gb = df.groupby(group)
    return [data(filename, gb.get_group(x)) for filename, x in zip(gb.groups.keys(), gb.groups)]

#
def create_tf_records_images(group, path):
    with tf.gfile.GFile(os.path.join(path, '{}'.format(group.filename)), 'rb') as fid:
        encoded_jpg = fid.read()
    encoded_jpg_io = io.BytesIO(encoded_jpg)
    image = Image.open(encoded_jpg_io)
    width, height = image.size

    filename = group.filename.encode('utf8')
    image_format = b'jpg'
    xmins = []
    xmaxs = []
    ymins = []
    ymaxs = []
    classes_text = []
    classes = []

    for index, row in group.object.iterrows():
        xmins.append(row['xmin'] / width)
        xmaxs.append(row['xmax'] / width)
        ymins.append(row['ymin'] / height)
        ymaxs.append(row['ymax'] / height)
        classes_text.append(row['class'].encode('utf8'))
        classes.append(class_text_to_int(row['class']))

    tf_record_image = tf.train.Example(features=tf.train.Features(feature={
        'image/height': dataset_util.int64_feature(height),
        'image/width': dataset_util.int64_feature(width),
        'image/filename': dataset_util.bytes_feature(filename),
        'image/source_id': dataset_util.bytes_feature(filename),
        'image/encoded': dataset_util.bytes_feature(encoded_jpg),
        'image/format': dataset_util.bytes_feature(image_format),
        'image/object/bbox/xmin': dataset_util.float_list_feature(xmins),
        'image/object/bbox/xmax': dataset_util.float_list_feature(xmaxs),
        'image/object/bbox/ymin': dataset_util.float_list_feature(ymins),
        'image/object/bbox/ymax': dataset_util.float_list_feature(ymaxs),
        'image/object/class/text': dataset_util.bytes_list_feature(classes_text),
        'image/object/class/label': dataset_util.int64_list_feature(classes),
    }))
    return tf_record_image


def main():
    writer = tf.python_io.TFRecordWriter(args.output_path)
    os.chdir('../../data')
    path = ''
    if args.train_or_test == 'train':
        path = os.path.join(os.getcwd(), 'train_images')
    if args.train_or_test == 'test':
        path = os.path.join(os.getcwd(), 'test_images')
    examples = pd.read_csv(args.csv_input)
    grouped = split(examples, 'filename')
    for group in grouped:
        tf_record_image = create_tf_records_images(group, path)     # changed function name to match the actual (create_tf_example to create_tf_records_images)
        writer.write(tf_record_image.SerializeToString()) 

    writer.close()
    output_path = os.path.join(os.getcwd(), args.output_path)
    print('Successfully created the TFRecords: {}'.format(output_path))


if __name__ == '__main__':
    main()
