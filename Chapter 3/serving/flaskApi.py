import json
import pickle
from sklearn import tree
import numpy as np

from flask import Flask, jsonify, request
from flask import abort


class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

app = Flask(__name__)

@app.route("/predict-with-params", methods=['POST'])
def predict_loading_params():
    with open("dt.pkl", "rb") as file:
        model: tree.DecisionTreeClassifier = pickle.load(file)
        # Loading params from param store
        param_file = open("../state_store/dt_params.pkl", "rb")
        params = pickle.load(param_file)
        print(params)
        model.__dict__ = params
        X = json.loads(request.data)
        print(X)
        print(X.shape)
        response = model.predict(X)
        return json.dumps(response, cls=NumpyEncoder)

@app.route("/predict-with-full-model", methods=['POST'])
def predict_with_full_model():
    with open("dt.pkl", "rb") as file:
        model: tree.DecisionTreeClassifier = pickle.load(file)
        X = json.loads(request.data)
        print(X)
        if len(X) == 0 or len(X[0]) != 3:
            message = f"""
The request feature dimension does not match the expected dimension.
The input length of {X[0]} is {len(X[0])} but the model expects the length to be 3. 
"""
            abort(400, message)
        response = model.predict(X)
        return json.dumps(response, cls=NumpyEncoder)

app.run()