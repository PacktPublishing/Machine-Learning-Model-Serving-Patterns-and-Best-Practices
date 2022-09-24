import pandas as pd

df = pd.DataFrame({"climate": ["Sunny", "Rainy", "Cloudy"]})
print("Initial data")
print(df.head())
df2 = pd.get_dummies(df)
print("Data after one hot encoding")
print(df2)