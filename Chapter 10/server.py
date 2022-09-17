from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor
import pickle
model1: RandomForestRegressor = pickle.load(open("rfreg.pb", "rb"))
model2: AdaBoostRegressor = pickle.load(open("adaboostreg.pb", "rb"))

def predict_model1(X):
    response = model1.predict(X)
    print("Response from model 1 is", response)
    return response

def predict_model2(X):
    response = model2.predict(X)
    print("Response from model 2 is", response)
    return response
def predict(X):
    response1 = predict_model1(X)
    response2 = predict_model2(X)
    response = (response1 + response2)/2
    print("Final response is ", response)

predict([[0, 0]])

