import tensorflow as tf

for example in tf.python_io.tf_record_iterator("train.records"):
  result = tf.train.Example.FromString(example)
  print(result.features.feature['label'].int64_list.value)
  print(result.features.feature['Gate'].bytes_list.value)
