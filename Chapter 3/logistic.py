from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
X, y = load_iris(return_X_y=True)
model = LogisticRegression(random_state=0, max_iter=200)
model.fit(X, y)
print(model.get_params())
res = model.predict(X[:2, :])
print(res)
