import tensorflow as tf
import tensorflow_datasets as tfds
import matplotlib.pyplot as plt
import numpy as np


(ds_train, ds_test), ds_info = tfds.load(
    'mnist',
    split=['train', 'test'],
    shuffle_files=True,
    as_supervised=True,
    with_info=True,
)

def normalize_img(image, label):
  """Normalizes images: `uint8` -> `float32`."""
  return tf.cast(image, tf.float32) / 255., label

ds_train = ds_train.map(
    normalize_img, num_parallel_calls=tf.data.AUTOTUNE)
ds_train = ds_train.cache()
print(ds_info.splits['train'].num_examples)
ds_train = ds_train.shuffle(ds_info.splits['train'].num_examples)
ds_train = ds_train.batch(128)
ds_train = ds_train.prefetch(tf.data.AUTOTUNE)

ds_test = ds_test.map(normalize_img)
ds_test = ds_test.batch(128)

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(8, activation='relu'),
  tf.keras.layers.Dropout(0.5),
  tf.keras.layers.Dense(10, activation='softmax')
])
model.compile(
    optimizer=tf.keras.optimizers.Adam(0.001),
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=[tf.keras.metrics.SparseCategoricalAccuracy()],
)

model.fit(
    ds_train,
    epochs=3,
    validation_data=ds_test,
)

predictions = model.predict(ds_test)
print(predictions[0])
model.summary()
W = model.variables
print(len(W))
print("Weights for input Layer to hidden layer")
print(W[0])
print("Shape of weights for input layer to hidden layer", W[0].shape)
print("Bias of the Hidden Layer")
print(W[1])
print("Shape of the bias of the hidden layer", W[1].shape)
print("Weights of the hidden to output layer")
print(W[2])
print("Shape of the weights of the hidden to output layer", W[2].shape)
print("Bias of the output layer")
print(W[3])
print("Shape of the bias of the output layer", W[3].shape)

# model.save('saved_model')

json = model.to_json()
print(json)