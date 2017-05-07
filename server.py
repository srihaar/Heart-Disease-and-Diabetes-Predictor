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
    return jsonify({'name' : 2})

@app.route('/heart',methods=['GET','POST'])
def predict():
    # print request.form
    # name = request.form
    # data = name['data']
    params = ["age", "sex", "cp", "trestbps", "chol","fbs", "restecg","thalach","exang", "oldpeak","slope", "ca", "thal"]
    list1 = [0]*13
    list1[0]= request.args.get(params[0])
    list1[1] = request.args.get(params[1])
    list1[2] = request.args.get(params[2])
    list1[3] = request.args.get(params[3])
    list1[4] = request.args.get(params[4])
    list1[5] = request.args.get(params[5])
    list1[6] = request.args.get(params[6])
    list1[7] = request.args.get(params[7])
    list1[8] = request.args.get(params[8])
    list1[9] = request.args.get(params[9])
    list1[10] = request.args.get(params[10])
    list1[11] = request.args.get(params[11])
    list1[12] = request.args.get(params[12])
    list1 = ','.join(list1)
    l = os.system('python -W ignore heart_analysis.py '+list1)
    return jsonify({'output':l})

@app.route('/diabetes',methods=['GET','POST'])
def predict1():
    list1 = [0]*8
    list1[0]= request.args.get('preg')
    list1[1] = request.args.get('plas')
    list1[2] = request.args.get('diast')
    list1[3] = request.args.get('serum')
    list1[4] = request.args.get('body')
    list1[5] = request.args.get('pede')
    list1[6] = request.args.get('tricep')
    list1[7] = request.args.get('age')
    list1 = ','.join(list1)
    l = os.system('python -W ignore diabetes.py '+ list1)
    return jsonify({'output':l})


if __name__ == '__main__':
    app.run()
