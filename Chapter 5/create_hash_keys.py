import pandas as pd

df = pd.DataFrame({"F1": [3, 4, 5, 6], "F2": [100, 200, 300, 400]})
print(df.head())
df['key'] = df.apply(lambda x: hash(tuple(x)), axis=1)
print(df.head())