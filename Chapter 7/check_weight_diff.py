import keras
import numpy as np

model1: keras.models.Sequential = keras.models.load_model("keras_mnist")
W1 = model1.get_weights()

model2: keras.models.Sequential = keras.models.load_model("keras_mnist2")
W2 = model2.get_weights()
diff = W2[0] - W1[0]

print("Printing diff")
print(diff[0][0][0])

