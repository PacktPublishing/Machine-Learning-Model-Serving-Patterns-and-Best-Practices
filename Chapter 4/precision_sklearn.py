from sklearn import metrics
y_pred = [0, 1, 0, 0]
y_true = [0, 1, 1, 1]
precision = metrics.precision_score(y_true, y_pred)
print(precision)

