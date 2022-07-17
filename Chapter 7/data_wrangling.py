import pandas as pd

df = pd.DataFrame({"X": [5, 6, "Seven"], "Y": [2, None, 5]})
print(df)

from sklearn.linear_model import LinearRegression
X = df['X']
y = df['Y']
model = LinearRegression().fit(X, y)
