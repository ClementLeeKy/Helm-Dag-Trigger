import airflow
from airflow import DAG
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator

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
            schedule_interval='@once',
            catchup=False
)

with dag as dag:
        t1 = KubernetesPodOperator(
                namespace='airflow-config',
                image="alpine",
                cmds=["/bin/sh", "-ec", "sleep 1000"],
                name="pod1",
                task_id='pod1',
                image_pull_policy="Always",
                is_delete_operator_pod=False,
                hostnetwork=False 
)


