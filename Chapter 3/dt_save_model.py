from sklearn import tree
import pickle

X = [[0, 0, 2], [1, 1, 3], [3, 1, 3]]
Y = [0, 1, 2]

"""
X = [[8, 4, 2], [5, 1, 3], [5, 1, 3]]
Y = [2, 1, 0]
"""
model = tree.DecisionTreeClassifier()
model.fit(X, Y)
with open("models/dt.pkl", "wb") as file:
    pickle.dump(model, file)
print(model.predict([[1, 1, 6]]))

params = model.__dict__

with open("state_store/dt_params.pkl", "wb") as param_file:
    pickle.dump( params, param_file )

