import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os
import sklearn
# get_ipython().magic('matplotlib inline')
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from keras.models import Sequential
from keras.layers import Dense, Activation,Embedding,Bidirectional,LSTM
from keras.utils import np_utils
from keras.optimizers import SGD
from decimal import *


def one_hot_encode_object_array(arr):
    '''One hot encode a numpy array of objects (e.g. strings)'''
    uniques, ids = np.unique(arr, return_inverse=True)
    return np_utils.to_categorical(ids, len(uniques))

l = sys.argv[1]
l = l.split(',')
# print type(l[0])
for x in xrange(0,len(l)):
    l[x] = int(l[x])
# print l,type(l),type(l[0])
#
data = pd.read_csv('heart_disease.csv',header=None,names=["age", "sex", "cp", "trestbps", "chol","fbs", "restecg",
                   "thalach","exang", "oldpeak","slope", "ca", "thal", "num"])
# len(data),len(data.iloc[0])
data.loc[data['num']>=1,'num'] = 1
p = data['num'].value_counts()
# # p
xvalues = []
yvalues = []
for i in xrange(len(p)):
    xvalues.append(i),yvalues.append(p[i])
# # print xvalues[:3],yvalues[:3]
# # plt.bar(xvalues,yvalues)
data = data.dropna()
# # data.isnull().values.sum()
# # len(data)
X_values  = data[["age", "sex", "cp", "trestbps", "chol","fbs", "restecg",
                   "thalach","exang", "oldpeak","slope", "ca", "thal"]]
y_values = data[['num']]
X_train,X_test,y_train,y_test = train_test_split(X_values,y_values,test_size=0.3)
# # len(X_train),len(y_train)
# # len(X_test),len(y_test)
sc = StandardScaler()
X_train_std = sc.fit_transform(X_train)
X_test_std = sc.fit_transform(X_test)
clf = LogisticRegression(C=0.01)
clf.fit(X_train_std,y_train)
# # print clf.score(X_test_std,y_test)
# # l = [1,2,1,1,1,1,1,1,1,1,1,1,1]
print clf.predict(l)
# # clf = RandomForestClassifier(n_jobs=20)
# # clf.fit(X_train_std,y_train)
# # clf.score(X_test_std,y_test)
# # clf = SVC()
# # clf.fit(X_train_std,y_train)
# # clf.score(X_test_std,y_test)
# # y_train_ohe = y_train
# # y_test_ohe = y_test
# # print type(X_train),type(X_test),type(y_train),type(y_test)
# # model = Sequential()
# # model.add(Dense(32, activation='relu', input_dim=13))
# # model.add(Dense(1, activation='sigmoid'))
# # model.compile(optimizer='rmsprop',
# #               loss='binary_crossentropy',
# #               metrics=['accuracy'])
# # model.fit(X_train,y_train, epochs=100, batch_size=32)
# # model.evaluate(X_test,y_test,batch_size=32)
