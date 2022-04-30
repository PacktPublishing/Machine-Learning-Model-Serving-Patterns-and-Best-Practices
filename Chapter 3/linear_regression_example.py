from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression
X, y = make_regression(n_features=2, random_state=0, shuffle=False, n_samples=100)
model = RandomForestRegressor(max_depth=2)
model.fit(X, y)
print(model.predict([[0, 0]]))


