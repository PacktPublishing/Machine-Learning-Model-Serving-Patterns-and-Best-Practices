import numpy as np
import random

def predict_phase_one_model(x):
    print("The value of x is", x)
    if x < 0.5:
        return True
    else:
        return False

def predict_phase_two_model():
    print("Phase two model is called")
    prediction = np.random.choice(["Class A", "Class B", "Class C"])
    return prediction

if __name__=="__main__":
    phase_one_prediction = predict_phase_one_model(random.uniform(0, 1))
    if phase_one_prediction == True:
        response = predict_phase_two_model()
        print(response)
    else:
        print("Phase two model is not called")



