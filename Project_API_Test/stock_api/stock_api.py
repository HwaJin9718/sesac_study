# 주식 시세 정보 데이터

from dotenv import load_dotenv
from flask import Flask, request, redirect, url_for, jsonify
import requests
import os
import json

load_dotenv()

app=Flask(__name__)
app.secret_key = os.getenv("SESSION_SECRET")

KIS_CLIENT_ID=os.getenv("KIS_API_KEY")
KIS_CLIENT_SECRET=os.getenv("KIS_SECRET_KEY")


@app.route('/api/kis/access')
def access_kis():

    # KIS 인증 토큰 요청
    url = 'https://openapivts.koreainvestment.com:29443/oauth2/tokenP'

    headers = {'Content-Type' : 'application/json; charset=UTF-8'}

    body = {
        'grant_type' : 'client_credentials', 
        'appkey' : KIS_CLIENT_ID, 
        'appsecret' : KIS_CLIENT_SECRET
    }

    res = requests.post(url, headers=headers, data=json.dumps(body)).json()

    return jsonify({'result': res})


if __name__ == "__main__":
    app.run(debug=True)
