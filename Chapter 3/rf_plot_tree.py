from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.tree import DecisionTreeRegressor

X, y = make_regression(n_features=2, random_state=0, shuffle=False, n_samples=100)
model = RandomForestRegressor(max_depth=2, n_estimators=10)
model.fit(X, y)
print(model.predict([[0, 0]]))
print("Total estimators", len(model.estimators_))
root: DecisionTreeRegressor = model.estimators_[0]

print(root)

print(model.decision_path([[0, 0]])[0])
print(root.decision_path([[0, 0]]))

feature_labels= ["X"]
target_labels= ["Y"]
fig, axes = plt.subplots(nrows = 1,ncols = 1,figsize = (8,8), dpi=1200)
tree.plot_tree(model.estimators_[1],
               feature_names = feature_labels,
               class_names=target_labels,
               filled = True)
fig.savefig('rf_trees2.png')


