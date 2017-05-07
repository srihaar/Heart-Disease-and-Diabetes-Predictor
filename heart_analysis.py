import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os
import sklearn

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
for x in xrange(0,len(l)):
    l[x] = int(l[x])
data = pd.read_csv('heart_disease.csv',header=None,names=["age", "sex", "cp", "trestbps", "chol","fbs", "restecg",
                   "thalach","exang", "oldpeak","slope", "ca", "thal", "num"])
data.loc[data['num']>=1,'num'] = 1
p = data['num'].value_counts()
xvalues = []
yvalues = []
for i in xrange(len(p)):
    xvalues.append(i),yvalues.append(p[i])
data = data.dropna()
X_values  = data[["age", "sex", "cp", "trestbps", "chol","fbs", "restecg",
                   "thalach","exang", "oldpeak","slope", "ca", "thal"]]
y_values = data[['num']]
X_train,X_test,y_train,y_test = train_test_split(X_values,y_values,test_size=0.3)
sc = StandardScaler()
X_train_std = sc.fit_transform(X_train)
X_test_std = sc.fit_transform(X_test)
clf = LogisticRegression(C=0.01)
clf.fit(X_train_std,y_train)

