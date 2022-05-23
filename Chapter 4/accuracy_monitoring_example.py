from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import numpy as np

predictions = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
actual_jan = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
actual_feb = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
actual_mar = [0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
actual_apr = [0, 0, 1, 1, 1, 1, 1, 1, 0, 0]
actual_may = [0, 0, 0, 1, 1, 1, 0, 1, 0, 0]
actual_jun = [0, 0, 0, 0, 0, 1, 0, 1, 0, 0]
actual_jul = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

acc_jan = accuracy_score(actual_jan, predictions)
acc_feb = accuracy_score(actual_feb, predictions)
acc_mar = accuracy_score(actual_mar, predictions)
acc_apr = accuracy_score(actual_apr, predictions)
acc_may = accuracy_score(actual_may, predictions)
acc_jun = accuracy_score(actual_jun, predictions)
acc_jul = accuracy_score(actual_jul, predictions)

errors = np.array([acc_jan, acc_feb, acc_mar, acc_apr, acc_may, acc_jun, acc_jul])
plt.plot(errors)
plt.ylabel("Accuracy")
plt.xlabel("Index of Month")
plt.show()

