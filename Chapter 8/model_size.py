import os
size = os.stat('mnist/saved_model.pb').st_size
print("Size of phase two model ", size)
size2 = os.stat('quantized_model/mnist_model_quant.tflite').st_size
print("Size of phase one model ", size2)
reduction = round(size/size2, 2)
print("Reduction of size is ", reduction, "times")