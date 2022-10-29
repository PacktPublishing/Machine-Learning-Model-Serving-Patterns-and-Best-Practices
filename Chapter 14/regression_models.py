import bentoml
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor
from sklearn.datasets import make_regression
X, y = make_regression(n_features=4, n_informative=2,
                       random_state=0, shuffle=False)
rf = RandomForestRegressor(max_depth=3, random_state=0)
rf.fit(X, y)
rf_model = bentoml.sklearn.save_model(
    name = "rf",
    model = rf
)
print(rf_model)

boost = AdaBoostRegressor(random_state=0)
boost.fit(X, y)
boost_model = bentoml.sklearn.save_model(
    name = "boost",
    model = boost
)

print(boost_model)