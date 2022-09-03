from datetime import datetime, timedelta
from airflow import DAG

from airflow.operators.bash import BashOperator
with DAG(
    'dummy_ml_pipeline',
    default_args={
        'depends_on_past': False,
        'email': ['airflow@example.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=5)
    },
    description='A dummy machine learning pipeline',
    schedule_interval="0/5 * * * *",
    start_date=datetime(2022, 1, 1),
    catchup=False,
    tags=['ml_pipeline'],
) as dag:
    init_data_directory = BashOperator(
        task_id='init_data_dir',
        bash_command='python3 /Users/mislam/Desktop/airflow-examples/dags/stages/init_data_dir.py',
    )

    data_collection_source1 = BashOperator(
        task_id='data_collection_1',
        bash_command='python3 /Users/mislam/Desktop/airflow-examples/dags/stages/data_collector_source1.py',
    )

    data_collection_source2 = BashOperator(
        task_id='data_collection_2',
        bash_command='python3 /Users/mislam/Desktop/airflow-examples/dags/stages/data_collector_source2.py',
    )

    data_combiner = BashOperator(
        task_id='data_combiner',
        bash_command='python3 /Users/mislam/Desktop/airflow-examples/dags/stages/data_combiner.py',
    )

    training = BashOperator(
        task_id='training',
        bash_command='python3 /Users/mislam/Desktop/airflow-examples/dags/stages/train.py',
    )

    init_data_directory >> [data_collection_source1, data_collection_source2] >> data_combiner >> training
