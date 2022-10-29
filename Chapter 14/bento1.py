import bentoml
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression
X, y = make_regression(n_features=4, n_informative=2,
                       random_state=0, shuffle=False)
regr = RandomForestRegressor(max_depth=3, random_state=0)
regr.fit(X, y)
saved_model = bentoml.sklearn.save_model(
    name = "DummyRegressionModel",
    model = regr
)

print(saved_model)