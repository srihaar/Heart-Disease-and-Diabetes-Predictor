import os,sys
import random
from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app)


@app.route('/',methods=['GET','POST'])
def hello():
    # print param
    return jsonify({'name' : 2})

@app.route('/heart',methods=['GET','POST'])
def predict():
    # print request.form
    # name = request.form
    # data = name['data']
    post = request.get_json()

    params = ["age", "sex", "cp", "trestbps", "chol","fbs", "restecg","thalach","exang", "oldpeak","slope", "ca", "thal"]
    list1 = [0]*13
    list1[0]= post.get(params[0])
    list1[1] = post.get(params[1])
    list1[2] = post.get(params[2])
    list1[3] = post.get(params[3])
    list1[4] = post.get(params[4])
    list1[5] = post.get(params[5])
    list1[6] = post.get(params[6])
    list1[7] = post.get(params[7])
    list1[8] = post.get(params[8])
    list1[9] = post.get(params[9])
    list1[10] = post.get(params[10])
    list1[11] = post.get(params[11])
    list1[12] = post.get(params[12])
    list1 = ','.join(list1)
    l = os.system('python -W ignore heart_analysis.py '+list1)
    return jsonify({'output':l})

@app.route('/diabetes',methods=['GET','POST'])
def predict1():
    post = request.get_json()
    list1 = [0]*8
    list1[0]= post.get('preg')
    list1[1] = post.get('plas')
    list1[2] = post.get('diast')
    list1[3] = post.get('serum')
    list1[4] = post.get('body')
    list1[5] = post.get('pede')
    list1[6] = post.get('tricep')
    list1[7] = post.get('age')
    list1 = ','.join(list1)
    l = os.system('python -W ignore diabetes.py '+ list1)
    return jsonify({'output':l})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
