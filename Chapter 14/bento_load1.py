import bentoml
from sklearn.ensemble import RandomForestRegressor
regr: RandomForestRegressor = bentoml.sklearn.load_model("dummyregressionmodel:dudusucwz6ej6ktz")
print(regr)