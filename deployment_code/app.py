from flask import Flask, render_template, request, Markup
import pickle
import os
import numpy as np
from collections import Counter

app = Flask(__name__)

fetal_bw_m1 = pickle.load(open('fetal_bw_m1.sav', 'rb'))
fetal_bw_m2 = pickle.load(open('fetal_bw_m2.sav', 'rb'))

fetal_hc_m1 = pickle.load(open('fetal_hc_1', 'rb'))
fetal_hc_m2 = pickle.load(open('fetal_hc_2', 'rb'))
fetal_hc_m3 = pickle.load(open('fetal_hc_3', 'rb'))
fetal_hc_m4 = pickle.load(open('fetal_hc_4', 'rb'))

sc = pickle.load(open("StandardScalerObj", 'rb'))

@app.route("/")
@app.route("/index.html")
def index():
    return render_template("index.html")

@app.route("/fetal_birthweight.html")
def fetalbw():
    return render_template("fetal_birthweight.html")

@ app.route('/fetalbwprediction', methods=['POST'])
def fetalbwprediction():
    if request.method == 'POST':
        gagef = float(request.form['gage'])
        magef = float(request.form['mage'])
        mheightf = float(request.form['mheight'])
        mweightf = float(request.form['mweight'])
        smokef = str(request.form['smoke'])
        parityf = str(request.form['parity'])

        if smokef == "Yes":
            smokef = 1
        else:
            smokef = 0

        if parityf == "Yes":
            parityf = 1
        else:
            parityf = 0

        data = np.array([[gagef,parityf,magef,mheightf,mweightf,smokef]])
        y_pred1 = fetal_bw_m1.predict(data)
        y_pred2 = fetal_bw_m2.predict(data)
        y_pred = [np.round((1*i+5*j)/6.0,3) for i,j in zip(y_pred1,y_pred2)]
        final_prediction = np.array(y_pred)[0]
        return render_template('fetal_birthweight_result.html', prediction=final_prediction)

@ app.route('/fetalhealthclassifydirect', methods=['POST'])
def fetalhealthclassifydirect():
    if request.method == 'POST':
        valform = str(request.form['val'])
        vals = valform.split(",")
        data = [float(val) for val in vals]
        data = np.array([data])
        data = sc.transform(data)
        yp1 = fetal_hc_m1.predict(data)
        yp2 = fetal_hc_m2.predict(data)
        yp3 = fetal_hc_m3.predict(data)
        yp4 = fetal_hc_m4.predict(data)
        l = [yp1[0], yp2[0], yp3[0], yp4[0]]
        l = Counter(l)
        l = {k: v for k, v in sorted(l.items(), key=lambda item: item[1], reverse=True)}
        print(l)
        y_pred = list(l.keys())[0]
        return render_template('fetal_hc_result.html', prediction=y_pred)

@ app.route('/fetalhealthclassify', methods=['POST'])
def fetalhealthclassify():
    if request.method == 'POST':
        v1 = float(request.form['bval'])
        v2 = float(request.form['vv1'])
        v3 = float(request.form['vv2'])
        v4 = float(request.form['vv3'])
        v5 = float(request.form['vv4'])
        v6 = float(request.form['vv5'])
        v7 = float(request.form['vv6'])
        v8 = float(request.form['vv7'])
        v9 = float(request.form['vv8'])
        v10 = float(request.form['vv9'])
        v11 = float(request.form['vv10'])
        v12 = float(request.form['vv11'])
        v13 = float(request.form['vv12'])
        v14 = float(request.form['vv13'])
        v15 = float(request.form['vv14'])
        v16 = float(request.form['vv15'])
        v17 = float(request.form['vv16'])
        v18 = float(request.form['vv17'])
        v19 = float(request.form['vv18'])

        data = np.array([[v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,
                          v11,v12,v13,v14,v15,v16,v17,v18,v19]])
        data = sc.transform(data)
        yp1 = fetal_hc_m1.predict(data)
        yp2 = fetal_hc_m2.predict(data)
        yp3 = fetal_hc_m3.predict(data)
        yp4 = fetal_hc_m4.predict(data)
        l = [yp1[0], yp2[0], yp3[0], yp4[0]]
        l = Counter(l)
        l = {k: v for k, v in sorted(l.items(), key=lambda item: item[1], reverse=True)}
        y_pred = list(l.keys())[0]
        return render_template('fetal_hc_result.html', prediction=y_pred)

@app.route("/fetalhc_opt.html")
def fetalhc():
    return render_template("fetalhc_opt.html")

@app.route("/fetal_healthclassification.html")
def fetalhc1():
    return render_template("fetal_healthclassification.html")

@app.route("/fetal_hc_direct.html")
def fetalhc2():
    return render_template("fetal_hc_direct.html")

if __name__ == '__main__':
    app.run(debug=True)