from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import numpy as np

predictions = [350, 430, 550, 300]
actual_jan = [350, 430, 550, 300]
actual_feb = [360, 445, 570, 305]
actual_mar = [370, 460, 590, 310]
actual_apr = [380, 475, 610, 315]
actual_may = [390, 500, 630, 325]
actual_june = [410, 515, 650, 330]
actual_july = [430, 530, 670, 340]

mse_jan = mean_squared_error(actual_jan, predictions)
mse_feb = mean_squared_error(actual_feb, predictions)
mse_mar = mean_squared_error(actual_mar, predictions)
mse_apr = mean_squared_error(actual_apr, predictions)
mse_may = mean_squared_error(actual_may, predictions)
mse_june = mean_squared_error(actual_june, predictions)
mse_july = mean_squared_error(actual_july, predictions)

errors = np.array([mse_jan, mse_feb, mse_mar, mse_apr, mse_may, mse_june, mse_july])
plt.plot(errors)
plt.ylabel("MSE")
plt.xlabel("Index of Month")
plt.show()
