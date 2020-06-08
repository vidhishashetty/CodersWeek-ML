
from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

loaded_model = pickle.load(open('finalized_model.sav', 'rb'))

@app.route('/')
def hello_world():
    return render_template("shopping.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
     l=[]
     Xnew=[]
     l.append(int(request.form.get("gender")))
     l.append(int(request.form.get("age")))
     l.append(int(request.form.get("EstimatedSalary")))
     Xnew.append(l)

     ynew = loaded_model.predict(Xnew) 


     if (ynew[0]==0):
        return render_template('shopping.html',pred='Customer is likely to NOT PURCHASE',bhai="hai")
     if (ynew[0]==1):
        return render_template('shopping.html',pred='Customer is likely to PURCHASE',bhai="how")
if __name__ == '__main__':
      app.run()