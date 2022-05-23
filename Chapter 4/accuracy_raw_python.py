def accuracy_score(y_true, y_pred, normalize = True):
    score = 0
    size = len(y_pred)
    for i in range(0, size):
        if y_pred[i] == y_true[i]:
            score = score + 1
    if normalize:
        return score/size
    else:
        return score

y_pred = [0, 2, 1, 3]
y_true = [0, 1, 2, 3]
acc1 = accuracy_score(y_true, y_pred)
print(acc1)
acc2 = accuracy_score(y_true, y_pred, normalize=False)
print(acc2)
