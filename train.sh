#!/bin/bash

python models/research/object_detection/model_main.py train --logtostderr --train_dir=data/training/ --pipeline_config_path=data/training/ssd_mobilenet_v2_coco.config

