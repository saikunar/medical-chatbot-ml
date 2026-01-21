import pandas as pd 
from sklearn.linear_model import LogisticRegression
import pickle
#load dataset 
df = pd.read_csv("medical_data.csv")
x = df.drop ("disease", axis=1) 
y = df["disease"]
model = LogisticRegression(max_iter=1000)
model.fit(x, y)
#save model
pickle.dump(model,open("disease_model.pkl","wb"))
print("Model trained and saved successfully.")
