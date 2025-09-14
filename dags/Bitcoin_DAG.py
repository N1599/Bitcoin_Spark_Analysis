from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
import papermill as pm



default_args = {
    "start_date" : datetime.now()
}

def run_bitcoin_notebook():
     input_path = "/opt/airflow/dags/Bitcoin_Analysis.ipynb"
     output_path = "/opt/airflow/dags/Bitcoin_Analysis_output.ipynb"

     pm.execute_notebook(
          input_path,
          output_path,
     )


with DAG(
        "Bitcoin_Price_Analysis_Job",
        schedule_interval = None,
        default_args = default_args,
        catchup=False,
        tags = ["bitcoin"]

) as dag:
    
    run_task = PythonOperator(
        task_id = "run_bitcoin_notebook" , 
        python_callable = run_bitcoin_notebook,
    )

    