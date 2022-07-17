import keras
import numpy as np

model: keras.models.Sequential = keras.models.load_model("keras_mnist")
print(model.summary())


(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

x_test = x_test.astype("float32") / 255
x_test = x_test[0:10]
y_test = y_test[0:10]
y_test = keras.utils.to_categorical(y_test, 10)
# Make sure images have shape (28, 28, 1)
x_test = np.expand_dims(x_test, -1)

print(x_test.shape)
print(y_test.shape)

score = model.evaluate(x_test, y_test, verbose=1)
print("Test loss:", score[0])
print("Test accuracy:", score[1])


model.fit(x_test, y_test, batch_size=100, epochs=15, validation_split=0.1)
score = model.evaluate(x_test, y_test, verbose=0)
print("Test loss:", score[0])
print("Test accuracy:", score[1])
model.save("keras_mnist2", save_format="tf")
