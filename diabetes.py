import pandas as pd
import numpy as np
import sklearn
from keras.models import Sequential
from keras.layers import Dense
import sys
a = sys.argv[1]
# a = a[1:-1]
a = a.split(',')
# print a
df = pd.read_csv('diabetes.csv')
df.head()
from sklearn.model_selection import train_test_split
features = list(df.columns.values)
features.remove('Outcome')
# print(features)
X = df[features]
y = df['Outcome']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
zero_fields = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
def impute_zero_field(data, field):
    nonzero_vals = data.loc[data[field] != 0, field]
    avg = np.sum(nonzero_vals) / len(nonzero_vals)
    k = len(data.loc[ data[field] == 0, field])
    data.loc[ data[field] == 0, field ] = avg
for field in zero_fields:
    impute_zero_field(X_train, field)
def check_zero_entries(data, fields):
    for field in fields:
        print('field %s: num 0-entries: %d' % (field, len(data.loc[ data[field] == 0, field ])))
X_train = X_train.values
y_train = y_train.values
X_test  = X_test.values
y_test  = y_test.values
NB_EPOCHS = 100
BATCH_SIZE = 16
model = Sequential()
model.add(Dense(12, input_dim=8, init='uniform', activation='relu'))
model.add(Dense(8, init='uniform', activation='relu'))
model.add(Dense(1, init='uniform', activation='sigmoid' ))
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
y_train = y_train.reshape(-1,1)
model.fit(X_train,y_train,validation_data=(X_test, y_test),nb_epoch=NB_EPOCHS,batch_size=BATCH_SIZE,verbose=0)
print str(model.predict_classes(np.array([a])))[2:-2]
