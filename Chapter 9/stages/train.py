import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle
import numpy as np

df = pd.read_csv("/Users/mislam/Desktop/airflow-examples/dags/stages/data/data.csv")
X = df['x'].to_numpy().reshape(-1, 1)
print(X)
y = df['y']
model = LogisticRegression(random_state=0).fit(X, y)

with open('/Users/mislam/Desktop/airflow-examples/dags/stages/model_location/model.pkl','wb') as f:
    pickle.dump(model,f)

