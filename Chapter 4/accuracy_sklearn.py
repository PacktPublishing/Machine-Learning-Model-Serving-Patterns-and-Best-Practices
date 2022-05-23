from sklearn.metrics import accuracy_score
y_pred = [0, 2, 1, 3]
y_true = [0, 1, 2, 3]
acc1 = accuracy_score(y_true, y_pred)
print(acc1)
acc2 = accuracy_score(y_true, y_pred, normalize=False)
print(acc2)
