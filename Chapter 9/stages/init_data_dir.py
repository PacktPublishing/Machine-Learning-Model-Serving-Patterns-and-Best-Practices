import os

if not os.path.exists("/Users/mislam/Desktop/airflow-examples/dags/stages/data"):
    os.mkdir("/Users/mislam/Desktop/airflow-examples/dags/stages/data")
    print("The directory data is created")

if not os.path.exists("/Users/mislam/Desktop/airflow-examples/dags/stages/model_location"):
    os.mkdir("/Users/mislam/Desktop/airflow-examples/dags/stages/model_location")
    print("The directory model_location is created")