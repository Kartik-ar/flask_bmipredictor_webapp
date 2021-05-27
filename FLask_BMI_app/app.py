from flask import Flask, request, render_template
import joblib
import math


mind = joblib.load('BMI.pkl')
app = Flask('BMI_predictor_app')

@app.route('/form')
def dashboard():
    return render_template("app.html")

@app.route('/sheet')
def stylesheet():
    return render_template("app.css")
    
@app.route('/bmical', methods=['GET', 'POST'])
def BMIcal():
    if request.method == 'GET':
        heightf = request.args.get("height_feet")
        heighti = request.args.get("height_inches")
        weight = request.args.get("Weight")
    ht = (float(heightf) + float(heighti)/10)
    print(ht)
    height = float(float(heightf) + float(heighti)/10)/3.281
    print(height)
    pred = mind.predict([[height,weight]])
    test = [float(height) + 0.30 , float(weight) + 3.00]
    print(test)
    predb = mind.predict([[float(height)+0.30 , float(weight)+1.00]])
    BMI = math.trunc(pred[0])
    BMIp = math.trunc(predb[0])
    print(predb)
    print(pred)
    return render_template('result.html', result = [ ht, weight, BMI, BMIp]  )
     
app.run(host="0.0.0.0", debug=True)