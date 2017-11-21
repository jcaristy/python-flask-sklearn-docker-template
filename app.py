#!flask/bin/python
from flask import Flask
from flask import session
from flask import request
import uuid
import pandas as pd
from sklearn import linear_model
import pickle





app = Flask(__name__)
app.config['SECRET_KEY'] = 'q3RD7Urbz72xGhsjJKv'



@app.route('/isAlive')
def index():
    return "true"



@app.route('/prediction/api/v1.0/citibykes', methods=['GET'])
def get_prediction():
    feature1 = float(request.args.get('day'))
    feature2 = float(request.args.get('hour'))
    loaded_model = pickle.load(open('model.pkl', 'rb'))
    prediction = loaded_model.predict([[feature1, feature2]])
    return str(prediction)



@app.route('/image')
def image():
    return "QQBQ"



if __name__ == '__main__':
    app.run(port=5000,host='0.0.0.0')        
    # app.run(debug=True)
