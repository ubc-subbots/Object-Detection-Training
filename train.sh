#!/bin/bash

python models/research/object_detection/model_main.py --logtostderr --model_dir=data/models/model_1 --pipeline_config_path=data/training/ssd_mobilenet_v2_coco.config --num_train_steps=50000 --sample_1_of_n_examples=1 --alsologtostderr

