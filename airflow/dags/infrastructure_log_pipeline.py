from datetime import datetime, timedelta

from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator


default_args = {
    "retries": 2,
    "retry_delay": timedelta(minutes=1),
}


with DAG(
    dag_id="infrastructure_log_monitoring_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    default_args=default_args,
    tags=["infrastructure", "data-engineering"],
) as dag:

    ingest_data = BashOperator(
        task_id="ingest_data",
        bash_command="cd /opt/airflow/project && python src/ingest.py",
        env={
            "DB_HOST": "host.docker.internal",
        },
        append_env=True,
    )

    validate_data = BashOperator(
        task_id="validate_data",
        bash_command="cd /opt/airflow/project && python src/validate_data.py",
    )

    transform_data = BashOperator(
        task_id="transform_data",
        bash_command="cd /opt/airflow/project && python src/transform_data.py",
    )

    load_to_postgresql = BashOperator(
        task_id="load_to_postgresql",
        bash_command="cd /opt/airflow/project && python src/load_processed.py",
        env={
            "DB_HOST": "host.docker.internal",
        },
        append_env=True,
    )

    data_quality = BashOperator(
        task_id="data_quality",
        bash_command="cd /opt/airflow/project && python src/data_quality.py",
    )

    ingest_data >> validate_data >> transform_data >> load_to_postgresql >> data_quality