def precision(y_true, y_pred):
    tp = 0
    fp = 0
    size = len(y_true)
    Positive = 1
    Negative = 0
    for i in range(0, size):
        if y_true[i] == Positive:
            if y_pred[i] == Positive:
                tp = tp + 1
        else:
            if y_pred[i] == Positive:
                fp = fp + 1

    return tp/ (tp + fp)

y_pred = [0, 1, 0, 0]
y_true = [0, 1, 1, 1]
precision = precision(y_true, y_pred)
print(precision)
