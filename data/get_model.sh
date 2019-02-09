#!/bin/bash

# The current directory
CURR_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

#Check if virtual environment is already created
if [ ! -d $CURR_DIR/ssd_mobilenet_v2_coco_2018_03_29 ]; then
    wget http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v2_coco_2018_03_29.tar.gz
fi

