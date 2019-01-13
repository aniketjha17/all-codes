import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#importing the datas and converting it into array:-
dataset=pd.read_csv('Social_Network_Ads.csv')
X=dataset.iloc[:,[1,2,3]].values
Y=dataset.iloc[:,4].values

#implementing categorical variable
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
lab_X=LabelEncoder()
X[:,0]=lab_X.fit_transform(X[:,0])
onehotencoder=OneHotEncoder(categorical_features=[0])
X=onehotencoder.fit_transform(X).toarray()

#avoiding the categorical reduncy
X=X[:,1:]

#spliting the data set into test and train
from sklearn.cross_validation import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.25,random_state=10)

#making the dataset in a particular range
from sklearn.preprocessing import StandardScaler
sc_X=StandardScaler()
X_train=sc_X.fit_transform(X_train)
X_test=sc_X.transform(X_test)

#applying logistic regression
from sklearn.linear_model import LogisticRegression
cl=LogisticRegression(random_state=0)
cl.fit(X_train,Y_train)

cl.score(X_test,Y_test)
y_pred=cl.predict(X_test)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(Y_test,y_pred)