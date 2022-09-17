from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor
from sklearn.datasets import make_regression
import pickle
X, y = make_regression(n_features=2, random_state=0, shuffle=False, n_samples=20)
print(X)
print(y)
model1 = RandomForestRegressor(max_depth=2)
model1.fit(X, y)
print(model1.predict([[0, 0]]))
pickle.dump(model1, open("rfreg.pb", "wb"))
model2 = AdaBoostRegressor(n_estimators=5)
model2.fit(X, y)
print(model2.predict([[0, 0]]))
pickle.dump(model2, open("adaboostreg.pb", "wb"))




