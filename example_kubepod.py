import airflow
from airflow import DAG
from datetime import datetime, timedelta
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils.dates import days_ago

default_args = {
            'owner': 'airflow',
            'depends_on_past': False,
            'start_date': days_ago(1),
            'email': ['airflow@example.com'],
            'email_on_failure': False,
            'email_on_retry': False
}

dag = DAG (
            dag_id='kube_dag_sample',
            default_args=default_args,
            schedule_interval=timedelta(minutes=60),
            catchup=False
)

start = DummyOperator(task_id='start', dag=dag)

trial = KubernetesPodOperator(namespace='default',
                     image="alpine",
                     cmds=["/bin/sh", "-ec", "sleep 1000"],
                     name="trial-task",
                     task_id="trial-task",
                     is_delete_operator_pod=False,
                     dag=dag
                     )

trial.set_upstream(start)

