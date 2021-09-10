from flask import Flask,render_template,url_for,request,redirect,flash

import pickle
import numpy as np
import sklearn
import pandas as pd

app = Flask(__name__)
app.secret_key = 'dont tell any one'



model = pickle.load(open('regression_model.pkl','rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/contact',methods = ["GET","POST"])
def contact():

    return render_template("contact.html")

@app.route('/projects')
def projects():
    return render_template("projects.html")



@app.route('/airquality')
def airquality():
    return render_template("airquality.html")

@app.route('/check',methods = ["POST"])
def check():
    values = [int(x) for x in request.form.values()]
    array_values = np.array([values])
    prediction = model.predict(array_values)
    prediction=abs(prediction)
    roundvalues = round(prediction[0], 1)
    if roundvalues <= 50:
        pred = 'good'
    elif roundvalues >50 and roundvalues <100:
        pred = 'Unhealthy for Sensitive Groups'
    elif roundvalues >100 and roundvalues<1500:
        pred = 'Unhealthy'
    elif roundvalues >1500:
        pred = 'Hazardous'

    return render_template("airquality.html", msg = 'the air quality index is {} which is {}'.format(roundvalues,pred))









if __name__ == '__main__':
    app.run(debug=True)