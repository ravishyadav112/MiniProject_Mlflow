import os
import mlflow

# Get token from environment
token = os.getenv("DAGSHUB_PAT")
if not token:
    raise EnvironmentError("❌ DAGSHUB_PAT not set")

repo_owner = "ravishyadav112"
repo_name = "MiniProject_Mlflow"

# ✅ Correct MLflow tracking URI
mlflow.set_tracking_uri(
    f"https://{repo_owner}:{token}@dagshub.com/{repo_owner}/{repo_name}.mlflow"
)

# Try creating a test experiment + run
mlflow.set_experiment("test-experiment")
with mlflow.start_run():
    mlflow.log_param("learning_rate", 0.01)
    mlflow.log_metric("accuracy", 0.95)

print("✅ Successfully logged run to DagsHub MLflow!")
