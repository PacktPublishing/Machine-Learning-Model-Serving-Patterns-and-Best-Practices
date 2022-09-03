import pandas as pd

df1 = pd.DataFrame({"x": [5, 5, 5, 3, 4, 5], "y": [2, 2, 2, 1, 1, 1]})

df1.to_csv("/Users/mislam/Desktop/airflow-examples/dags/stages/data/data2.csv")
