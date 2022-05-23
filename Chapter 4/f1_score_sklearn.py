from sklearn import metrics
y_pred = [0, 1, 0, 0]
y_true = [0, 1, 1, 1]

F1 = metrics.f1_score(y_true, y_pred)
print(F1) # Prints 0.5

y_pred = [1, 1, 1, 1, 1]
y_true = [0, 0, 0, 0, 1]

F1 = metrics.f1_score(y_true, y_pred)
print(F1) # Prints 0.33333333333333337
