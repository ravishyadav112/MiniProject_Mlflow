Mlflow-miniproject
==============================
Set up a CookieCutter 
Create a Virtual Environment
Create a repository in github
Connect Dagshub with github 
check dagshub is working on not by run this code >
 python notebooks/dagshub_setup.py

 Now my mlflow is working 
 
first we are doing the random experiment or we can say that the baseline_model 
After that we are checking all the model with bow and tdf like logistics model with both bow vs tfidf similarly with all the model
After that those who gives the best accuracy we choose that model 

##By run exp1_bow_vs_tfidf.py  and saw in mlflow ,we clearly know that logistrics regression works well with these data so we run our 3 rd experiment (i.e. exp3_lor_bow_hp.py) to get the best parameter in logistics regression through hyper parameter tuning 


After knowing the best model now we create the dvc pipeline

Initialize the dvc 
dvc init 

Initially we store the data in temp file After that we store the data in aws s3
dvc remote add -d myremote C:\Users\ASUS\AppData\Local\Temp

DVC Pipeline -> Data ingestion -> Data preprocessing -> Feature enginnering -> model Building-> evaluation

C0oJc1AHJxcxVjH6DHpVKWQa+TFzGQfw2JKvnQ2f


