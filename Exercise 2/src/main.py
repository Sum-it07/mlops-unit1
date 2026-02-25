
#Data Loading using pandas
from pathlib import Path
import pandas as pd

base_dir = Path(__file__).resolve().parent
data_path = base_dir.parent / 'data' / 'data.csv'
model_dir = base_dir.parent / 'model'
model_path = model_dir / 'model.pkl'

data=pd.read_csv(data_path)
df=pd.DataFrame(data)
print("Data Loaded: ")
print(df)

#Splitting data into training and testing
from sklearn.model_selection import train_test_split
x=df[['f1','f2']]
y=df['output']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.4,random_state=100)

#Training Logistic Regression model
from sklearn.linear_model import LogisticRegression
logReg=LogisticRegression()
logReg.fit(x_train,y_train)

y_predict=logReg.predict(x_test)
print(y_predict)

#Printing model Accuracy
from sklearn import metrics
print("Model Accuracy: ",metrics.accuracy_score(y_test,y_predict))


#Saveing trained model using joblib
from joblib import Parallel, delayed
import joblib

model_dir.mkdir(parents=True, exist_ok=True)
joblib.dump(logReg, model_path)

model=joblib.load(model_path)
print("predection using saved model: ",model.predict(x_test))