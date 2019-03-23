INPUT_TYPE=image_tensor
PIPELINE_CONFIG_PATH=data/training/ssd_mobilenet_v2_coco.config
TRAINED_CKPT_PREFIX=data/models/model_1/model.ckpt-2266
EXPORT_DIR=data/models/model_1_graph
python models/research/s
object_detection/export_inference_graph.py \
    --input_type=${INPUT_TYPE} \
    --pipeline_config_path=${PIPELINE_CONFIG_PATH} \
    --trained_checkpoint_prefix=${TRAINED_CKPT_PREFIX} \
    --output_directory=${EXPORT_DIR}


