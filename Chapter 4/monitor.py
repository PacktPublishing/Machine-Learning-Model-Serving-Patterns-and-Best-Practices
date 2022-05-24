import matplotlib.pyplot as plt
import numpy as np
import math

MSE = np.array([0, 4000, 7000, 11000, 15000, 23000])
MAE = np.array([0, 200, 300, 500, 700, 1000])
MAPE = np.array([0, 3, 8, 12, 20, 30])
RMSE = np.array([0, math.sqrt(4000), math.sqrt(7000),
                 math.sqrt(11000), math.sqrt(15000), math.sqrt(23000)])

MSE_Thresholds = np.array([5000, 5000, 5000, 5000, 5000, 5000])

fig, ax = plt.subplots(2, 2)
fig.suptitle("Model monitoring dashboard")
ax[0, 0].plot(MSE)
ax[0, 0].plot(MSE_Thresholds, 'r--', label="MSE Threshold")
ax[0, 0].legend()
ax[0, 0].set(xlabel="Index of Month", ylabel="MSE")

ax[0, 1].plot(MAE)
ax[0, 1].set(xlabel="Index of Month", ylabel="MAE")

ax[1, 0].plot(MAPE)
ax[1, 0].set(xlabel="Index of Month", ylabel="MAPE")

ax[1, 1].plot(RMSE)
ax[1, 1].set(xlabel="Index of Month", ylabel="RMSE")

plt.show()


MSE_Threshold = 5000
if MSE[-1] >= MSE_Threshold:
    print("Performance has dropped beyond the accepted threshold")

