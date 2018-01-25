from datetime import datetime 
from airflow import DAG 
from airflow.operators.dummy_operator import DummyOperator 
from airflow.operators import ZeppelinOperator 

dag = DAG(
	"zeppelin_note_dag", 
	description="scheduling a zepplin note from with airflow",
	schedule_interval="0 12 * * *", 
	start_date=datetime(2018, 1, 25), 
	catchup=False
	)

dummy_task = DummyOperator(task_id="dummy_task", dag=dag)
operator_task = ZeppelinOperator(note_id="2D3SJ1XAT", task_id="zep_note_operator", dag=dag)


dummy_task >> operator_task