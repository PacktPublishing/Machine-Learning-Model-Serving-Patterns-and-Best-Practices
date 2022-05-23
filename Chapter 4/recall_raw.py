def recall(y_true, y_pred):
    tp = 0
    fn = 0
    size = len(y_true)
    Positive = 1
    Negative = 0
    for i in range(0, size):
        if y_true[i] == Positive:
            if y_pred[i] == Positive:
                tp = tp + 1
            else:
                fn = fn + 1

    return tp/ (tp + fn)

# y_pred = [0, 1, 0, 0]
# y_true = [0, 1, 1, 1]

y_pred = [1, 1, 1, 1, 1]
y_true = [0, 0, 0, 0, 1]

recall = recall(y_true, y_pred)
print(recall)
