from flask import Flask, render_template, request
from joblib import load
app = Flask(__name__)
model=load('C:\\Users\\kandula sai bhaskar\\Desktop\\Updated Code\\floods.save', 'rb')
sc=load('C:\\Users\\kandula sai bhaskar\\Desktop\\Updated Code\\transform.save')
@app.route('/',methods=['GET'])
def home():
    return render_template("home.html")
    
@app.route('/flood_predict',methods=['GET'])
def flood_predicts_page():
    return render_template("flood_predict.html")
@app.route('/data_predict',methods=['POST'])
def predict():
    temp=request.form['cloudCover']
    Hum=request.form['annualRainfall']
    db=request.form['janFebRainfall']
    ap=request.form['marchMayRainfall']
    aal=request.form['juneSeptRainfall']

    data=[[float(temp),float(Hum),float(db),float(ap),float(aal)]]
    prediction=model.predict(sc.transform(data))
    output=prediction[0]
    print(output)
    if(output==0):
        return render_template('noChance.html')
    else:
        return render_template('chance.html',prediction='possibility of server flood') 
if __name__ == "__main__":
    app.run()