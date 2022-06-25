import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/predict_batch", methods=['POST'])
def predict_loading_params():
    df = pd.read_csv("predictions/predictions.csv")
    predictions = []
    for index, row in df.iterrows():
        product = row['products']
        score = row['scores']
        predictions.append((product, score))
    predictions.sort(key = lambda a : a[1], reverse = True)
    return jsonify(predictions)

app.run()