from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def fetch_task():
    print("Fetching stock prices...")

def insert_task():
    print("Inserting into database...")

with DAG(
    dag_id="hello_airflow_stub",
    start_date=datetime(2025, 8, 22),
    schedule="@daily",
    catchup=False,
) as dag:

    fetch = PythonOperator(
        task_id="fetch_prices_task",
        python_callable=fetch_task,
    )

    insert = PythonOperator(
        task_id="insert_into_db_task",
        python_callable=insert_task,
    )

    fetch >> insert
