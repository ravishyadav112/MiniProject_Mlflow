import mlflow
import dagshub
dagshub.init(repo_owner='ravishyadav112', repo_name='MiniProject_Mlflow', mlflow=True)

# mlflow.set_tracking_uri("https://github.com/ravishyadav112/MiniProject_Mlflow.git")

with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)