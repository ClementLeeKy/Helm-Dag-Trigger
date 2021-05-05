from airflow import DAG
from datetime import datetime, timedelta
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.operators.dummy_operator import DummyOperator

default_args = {
            'owner': 'airflow',
            'start_date': airflow.utils.dates.days_ago(1),
            'email': ['airflow@example.com'],
            'email_on_failure': False,
            'email_on_retry': False
}

dag = DAG (
            'kube_dag_sample',
            default_args=default_args,
            schedule_interval='59 * * * *',
            catchup=False
)

start = DummyOperator(task_id='start', dag=dag)

trial = KubernetesPodOperator(namespace='airflow-config',
                     image="alpine",
                     cmds=["/bin/sh", "-ec", "sleep 1000"],
                     name="minishift-pod",
                     task_id="minishift-pod",
                     is_delete_operator_pod=False,
                     dag=dag
                     )

trial.set_upstream(start)


                       



