import pandas as pd

df1 = pd.read_csv("/Users/mislam/Desktop/airflow-examples/dags/stages/data/data1.csv")
df2 = pd.read_csv("/Users/mislam/Desktop/airflow-examples/dags/stages/data/data2.csv")
df = pd.concat([df1, df2], ignore_index=True)
print(df)
df.to_csv("/Users/mislam/Desktop/airflow-examples/dags/stages/data/data.csv")