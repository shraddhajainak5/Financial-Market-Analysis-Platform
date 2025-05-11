from flask import Flask, send_file, request, jsonify
import requests
from datetime import datetime
from dateutil.relativedelta import relativedelta


app = Flask(__name__)


@app.route('/')
def linkfiles():
    return send_file('static/index.html')


@app.route('/displaythecontent', methods =["GET"])

def companydata():
    symbol = request.args.get('symbol')

    if symbol:
        api_key = 'cn8le99r01qocbpgkqggcn8le99r01qocbpgkqh0'
        api_url1 = f'https://finnhub.io/api/v1/stock/profile2?symbol={symbol}&token={api_key}'
        
        response1 = requests.get(api_url1)
        if (response1).status_code==200 :
            data1 = response1.json()
        
            return jsonify(data1)

    else:
        return jsonify(error="Error: No record has been found please enter a valid symbol"), 500
    
@app.route('/newscontent', methods =["GET"])

def newsdata():
    symbol = request.args.get('symbol')
    todaydate = datetime.today()
    datebefore = todaydate - relativedelta(days=30)
    fromdate = (datebefore).strftime('%Y-%m-%d')
    todate = (todaydate).strftime('%Y-%m-%d')
    if symbol:
        api_key = 'cn8le99r01qocbpgkqggcn8le99r01qocbpgkqh0'
    
        api_url2 = f'https://finnhub.io/api/v1/company-news?symbol={symbol}&from={fromdate}&to={todate}&token={api_key}'
       

        response2 = requests.get(api_url2)
        if (response2).status_code==200:
           
            data2 = response2.json()
            return jsonify(data2)
    
    else:
        return jsonify(error="Error: No record has been found please enter a valid symbol"), 500
    

@app.route('/summarycontent', methods =["GET"])

def summarydata():
    symbol = request.args.get('symbol')

    if symbol:
        api_key = 'cn8le99r01qocbpgkqggcn8le99r01qocbpgkqh0'
    
        
        api_url3 = f'https://finnhub.io/api/v1/quote?symbol={symbol}&token={api_key}'
        

        response3 = requests.get(api_url3)
        if (response3).status_code==200:
           
            data3 = response3.json()
            return jsonify(data3)

    else:
        return jsonify(error="Error: No record has been found please enter a valid symbol"), 500


@app.route('/recommendationcontent', methods =["GET"])

def recommendationdata():
    symbol = request.args.get('symbol')

    if symbol:
        api_key = 'cn8le99r01qocbpgkqggcn8le99r01qocbpgkqh0'       
        
        api_url4 =f'https://finnhub.io/api/v1/stock/recommendation?symbol={symbol}&token={api_key}'

        response4 = requests.get(api_url4)
        if (response4).status_code==200:
           
            data4 = response4.json()
            return jsonify(data4)

    else:
        return jsonify(error="Error: No record has been found please enter a valid symbol"), 500

@app.route('/chartcontent', methods =["GET"])

def chartdata():
    symbol = request.args.get('symbol')
    todaydate = datetime.today()
    datebefore = todaydate - relativedelta(months=6)-relativedelta(day=1)
    fromdate = int(datetime.combine(datebefore, datetime.min.time()).timestamp())*1000
    todate = int((todaydate).timestamp())*1000

    if symbol:
        api_key = '_M_5pzU5MgDL_3ve3Eg80EBalnSwdta7'       
        
        api_url5 =f'https://api.polygon.io/v2/aggs/ticker/{symbol}/range/1/day/{fromdate}/{todate}?adjusted=true&sort=asc&limit=120&apiKey=_M_5pzU5MgDL_3ve3Eg80EBalnSwdta7'
        response5 = requests.get(api_url5)
        if (response5).status_code==200:
           
            data5 = response5.json()
            return jsonify(data5)
    
    else:
        return jsonify(error="Error: No record has been found please enter a valid symbol"), 500


if __name__ == '__main__':
    app.run(debug=True)
