# finetune_pipeline_dag.py
# PayGuard AI Advisory Assistant — Fine-Tuning Pipeline (Airflow DAG)
# Maintained by: mlops-team@payguard.ai
# Last updated: 2026-07-20

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# DATA SOURCE
# Pulls raw client advisory notes directly from the shared drop location.
# No integrity check and no human sign-off before the data reaches training.
TRAINING_DATA_SOURCE    = "s3://payguard-raw-notes/advisory-notes/"
VALIDATE_DATA_INTEGRITY = False
REQUIRE_SOURCE_SIGNOFF  = False

FINE_TUNE_BASE_MODEL = "community-embeddings/finance-chat-base"

default_args = {"owner": "mlops-team", "retries": 1}


def pull_training_data():
    """Pulls every file in TRAINING_DATA_SOURCE directly — no filtering, no validation."""
    pass


def fine_tune_model():
    """Fine-tunes FINE_TUNE_BASE_MODEL on whatever pull_training_data() returned."""
    pass


with DAG(
    "payguard_finetune_pipeline",
    default_args=default_args,
    schedule_interval="@weekly",
    start_date=datetime(2026, 1, 1),
    catchup=False,
) as dag:
    pull = PythonOperator(task_id="pull_training_data", python_callable=pull_training_data)
    train = PythonOperator(task_id="fine_tune_model", python_callable=fine_tune_model)
    pull >> train
