import random
truths = [10, 11, 12, 13]

def jumbled_prediction_without_keys(X):
    response = []
    for i in range(len(X)):
        response.append(truths[i])
    random.shuffle(response)
    return response

def jumbled_prediction_with_keys(X):
    response = []
    for i in range(len(X)):
        (key, x)  = X[i]
        response.append((key, truths[i]))
    random.shuffle(response)
    return response


if __name__ == "__main__":
    X1 = [[1], [2], [3], [4]]
    Y1 = jumbled_prediction_without_keys(X1)
    print("Predictions without keys ", Y1)
    X2 = [(0, 1), (1, 2), (2, 3), (3, 4)]
    Y2 = jumbled_prediction_with_keys(X2)
    print("Predictions with keys ", Y2)
    Y2.sort(key=lambda pred: pred[0])
    print("Ordering restored using keys ", Y2)
