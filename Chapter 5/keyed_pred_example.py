import pandas as pd
from sklearn.linear_model import LinearRegression

Features = ["#Bedroom", "#Bathroom"]

def train(X: pd.DataFrame, y: pd.Series):
    X = X.loc[:, Features]
    model = LinearRegression()
    model.fit(X, y)
    return model

def predict_single(model: LinearRegression, x, key):
    y = model.predict(x)
    pred = pd.DataFrame({"y": [y], "key": [key]})
    return pred

def predict_batch(model: LinearRegression, X: pd.DataFrame):
    X = X.sample(frac=1)
    keys = X["key"]
    response = pd.DataFrame()
    for index, row in X.iterrows():
        pred = predict_single(model, [[row[Features[0]], row[Features[1]]]], keys[index])
        response = response.append(pred, ignore_index=True)
    return response

if __name__ == "__main__":
    X = pd.DataFrame({"#Bedroom": [5, 5, 4, 4, 3], "#Bathroom": [4, 3, 3, 2, 2]})
    Y = pd.Series([500, 450, 400, 350, 300])
    model = train(X, Y)
    X['key'] = pd.Series(["1", "2", "3", "4", "5"])
    response = predict_batch(model, X)
    print("Final response: ")
    print(response)


