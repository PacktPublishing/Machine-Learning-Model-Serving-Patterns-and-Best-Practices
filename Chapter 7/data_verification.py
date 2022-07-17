
from sklearn.linear_model import SGDClassifier
import numpy as np

X = [[1, 1], [1, 1], [2, 2], [2, 2]]
y = [0, 0, 1, 1]
model = SGDClassifier()
model.fit(X, y)
res = model.predict([[1, 1], [2, 2]])
print(res)



def should_use_in_partial_fit(model, X, y):
    preds = model.predict(X)
    equal = np.array(y) == np.array(preds)
    if(equal.all()):
        model.partial_fit(X, y)
        return model
    else:
        print("Data label seems wrong. Please manually verify")
        print("Not updating the model with this data. Returning the old model.")
        return model

X_new = [[1, 1], [1, 1], [1, 1]]
y_new = [1 , 1, 1]
model = should_use_in_partial_fit(model, X_new, y_new)
res = model.predict([[1, 1], [2, 2]])
print(res)
