from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor
from sklearn.datasets import make_regression
import numpy as np
X, y = make_regression(n_features=2, random_state=0, shuffle=False, n_samples=20)
model = RandomForestRegressor(max_depth=2)
model.fit(X, y)

Xt = np.array([0, 0])
if len(Xt.shape) != 2:
    print(f"Shape {Xt.shape} is not correct ")
else:
    print(model.predict(Xt))

Xt = np.array([["Zero", "Zero"]])
Xt = np.array([["0", "0"]])
try:
    Xt = Xt.astype(np.float64)
    print("Floating point data", Xt)
    print(model.predict(Xt))
except:
    print("Data type is not correct!")

