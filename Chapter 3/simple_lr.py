import numpy as np
from sklearn.linear_model import LinearRegression
import pickle
X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
y = np.dot(X, np.array([1, 2])) + 3
reg = LinearRegression().fit(X, y)
reg.score(X, y)
print(reg.coef_)
print(reg.intercept_)
print(reg.predict(np.array([[3, 5]])))
file = "model_params.json"
with open(file, "w") as fp:
    pickle.dump(reg,fp)