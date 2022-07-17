from sklearn.linear_model import SGDClassifier

X = [[1, 1], [1, 1], [2, 2], [2, 2]]
y = [0, 0, 1, 1]
model = SGDClassifier()
model.fit(X, y)
res = model.predict([[1, 1], [2, 2]])
print(res)
model.partial_fit(
    [[1, 1], [1, 1], [1, 1]],
    [1 , 1, 1])
res = model.predict([[1, 1], [2, 2]])
print(res)
