from sklearn import metrics
# y_pred = [0, 1, 0, 0]
# y_true = [0, 1, 1, 1]

y_pred = [1, 1, 1, 1, 1]
y_true = [0, 0, 0, 0, 1]
recall = metrics.recall_score(y_true, y_pred)
print(recall)

