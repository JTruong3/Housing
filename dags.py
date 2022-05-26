from airflow import DAG
from airflow.operators.bash_operator import BashOperator
import datetime as dt
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'Jason',
    'start_date': days_ago(0),
    'email': ['123@gmail.com'],
    'email_on_failure':False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': dt.timedelta(minutes = 5),
}

dag = DAG('housing_data_dag',
            default_args= default_args,
            description = 'Housing data extraction pipeline',
            schedule_interval = dt.timedelta(days = 1),)

t1 = BashOperator(
    task_id = 't1',
    bash_command = 'python3 /Users/jasontruong/Downloads/Learn/Rental/Housing/webscrape/seleniumWebscrape.py',
    dag = dag
)

t2 = BashOperator(
    task_id = 't2',
    bash_command = 'echo "yes"',
    dag = dag
)

t1 >> t2

