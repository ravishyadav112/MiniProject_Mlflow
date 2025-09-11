from flask import Flask , render_template , redirect,request , url_for , session
import mlflow
import pickle
from preprocessing_utility import normalize_text
import os
import pandas as pd


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


##load the model 

def get_latest_model_version(model_name):
    client = mlflow.MlflowClient()
    latest_version = client.get_latest_versions(model_name, stages=["Production"])
    if not latest_version:
        latest_version = client.get_latest_versions(model_name, stages=["None"])
    return latest_version[0].version if latest_version else None

model_name = "my_model"
model_version = get_latest_model_version(model_name)

model_uri = f'models:/{model_name}/{model_version}'
model = mlflow.pyfunc.load_model(model_uri)





vectorizer = pickle.load(open('models/vectorizer.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template("index.html",result = None , text = "")

@app.route('/predict' , methods = ["POST"])
def analyse():
    

    ##clean the data
    text = request.form['text']

    # clean
    text = normalize_text(text)

    # Vectorise the data  >> bow
    features = vectorizer.transform([text])
    features_df = pd.DataFrame.sparse.from_spmatrix(features)
    features_df = pd.DataFrame(features.toarray(), columns=[str(i) for i in range(features.shape[1])])


    ##predict the data
    result = model.predict(features_df)



   
    return render_template("index.html", result=int(result[0]), text=text)



if __name__ == "__main__":
    app.run(debug=True)