from flask import Flask,render_template,request
import requests,json
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
 
@app.route('/get_weather',methods=['POST'])
def get_weather():
    city=request.form['city']
    print("City is : ",city)
    url="http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=13f855955e1f0cd65acd02eb09eedfa5"
    response=json.loads(requests.get(url).text)
    data=dict()
    data['city']=city
    if response['cod']!="404":
        data['status']=200
        data['weather']=response['weather'][0]['main']+" - "+response['weather'][0]['description']
        data['temp']=response['main']['temp']-273.15
    else:
        data['status']=404
    return render_template('home.html',data=data)

if __name__ == '__main__':
    app.run(debug=True,port=8000)