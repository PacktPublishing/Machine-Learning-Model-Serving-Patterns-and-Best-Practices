from flask import Flask, request
import numpy as np
import json
from sklearn.linear_model import SGDRegressor

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

X = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1],
    [2, 2, 2],
    [2, 2, 2],
    [2, 2, 2]
     ]
y = [1, 1, 1, 2, 2, 2]
model = SGDRegressor()
model.fit(X, y)
print("Initial coefficients")
print(model.coef_)
print("Initial intercept")
print(model.intercept_)

app = Flask(__name__)

def update_model(Xn, yn):
    print("Updating the model")
    model.partial_fit(Xn, yn)
    print("New coefficients now")
    print(model.coef_)
    print("New intercept now")
    print(model.intercept_)


@app.route("/predict-online", methods=['POST'])
def predict_online():
    predictions = []
    X = json.loads(request.data)
    print("Input data is ", X)
    predictions = model.predict(X)
    update_model(X, predictions)
    return json.dumps(predictions, cls=NumpyEncoder)

if __name__ == "__main__":
    app.run()