from datetime import datetime, timedelta
from textwrap import dedent

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "depends_on_past": False,
    "email": ["airflow@example.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG(
    "tutorial",
    default_args=default_args,
    description="A simple tutorial DAG",
    schedule=timedelta(minutes=1),
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=["example"],
)

t1 = BashOperator(
    task_id="print_date",
    bash_command="date",
    dag=dag,
)

t2 = BashOperator(
    task_id="echo_hello",
    bash_command="echo 'hello'",
    dag=dag,
)

t1 >> t2

