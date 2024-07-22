import pandas as pd
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from scripts.data_ingestion import Data_Ingestion
from scripts.data_transformation import Data_Transformation
from scripts.model_trainer import Model_Trainer
from scripts.visualization import Visualizer

def ingest_data(**kwargs):
    data_ingestion = Data_Ingestion()
    df = data_ingestion.initiate_data_ingestion(num_users=50, num_posts=100)
    kwargs['ti'].xcom_push(key='df', value=df.to_json())

def transform_data(**kwargs):
    df = pd.read_json(kwargs['ti'].xcom_pull(key='df'))
    data_transformation = Data_Transformation()
    pca_features, user_activity = data_transformation.initiate_data_transformation(df)
    kwargs['ti'].xcom_push(key='pca_features', value=pca_features)
    kwargs['ti'].xcom_push(key='user_activity', value=user_activity.to_json())

def train_model(**kwargs):
    pca_features = kwargs['ti'].xcom_pull(key='pca_features')
    user_activity = pd.read_json(kwargs['ti'].xcom_pull(key='user_activity'))
    model_trainer = Model_Trainer()
    model_trainer.initiate_model_trainer(pca_features, user_activity)

def visualize_data(**kwargs):
    pca_features = kwargs['ti'].xcom_pull(key='pca_features')
    user_activity = pd.read_json(kwargs['ti'].xcom_pull(key='user_activity'))
    data_visualizer = Visualizer()
    data_visualizer.visualize(pca_features, user_activity)

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2021, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG('data_pipeline', default_args=default_args, schedule_interval=timedelta(days=1)) as dag:
    ingest = PythonOperator(
        task_id='ingest_data',
        python_callable=ingest_data,
        provide_context=True,
    )

    transform = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data,
        provide_context=True,
    )

    train = PythonOperator(
        task_id='train_model',
        python_callable=train_model,
        provide_context=True,
    )
    
    visualize = PythonOperator(
        task_id='visualize_data',
        python_callable=visualize_data,
        provide_context=True,
    )

    ingest >> transform >> train >> visualize