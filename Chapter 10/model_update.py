def load_model(filename):
    print("Loading the model:", filename)

def predict_model_current(X):
    model = load_model("model_update/model_current/model.txt")
    print("Current model is predicting for ", X)
    return "dummy_pred_current"

def predict_model_new(X):
    model = load_model("model_update/model_new/model.txt")
    print("New model is predicting for ", X)
    return "dummy_pred_new"

def predict(evaluation_period, X):
    if evaluation_period == True:
        pred_current = predict_model_current(X)
        pred_new = predict_model_new(X)
        file = open("evaluation_data.csv", "a")
        file.write(f"{pred_current}, {pred_new}")
        return pred_current
    else:
        return predict_model_current(X)
