from datetime import datetime, timedelta
from scripts.conn.pgtopg import PostgresToPostgresOperator

from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.operators.dummy_operator import DummyOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': '2021-04-25'
}

dag = DAG(
    dag_id='load_data',
    default_args= default_args,
    schedule_interval="@daily",
    dagrun_timeout=timedelta(minutes=2),
)

start = DummyOperator(
    task_id='start',
    dag=dag
)

extract_customer = PostgresToPostgresOperator(
    sql='scripts/sql/select_customer.sql',
    pg_table='report.purchase',
    src_postgres_conn_id='postgres_default',
    dest_postgress_conn_id='postgres_Y',
    task_id='extract_customer',
    dag=dag
)

start >> extract_customer