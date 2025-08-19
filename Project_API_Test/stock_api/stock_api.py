# 주식 시세 정보 데이터

from dotenv import load_dotenv
from flask import Flask, request, redirect, url_for, jsonify, session
import requests
import os
import json

load_dotenv()

app=Flask(__name__)
app.secret_key = os.getenv("SESSION_SECRET")

KIS_REAL_CLIENT_ID=os.getenv("KIS_REAL_API_KEY")
KIS_REAL_CLIENT_SECRET=os.getenv("KIS_REAL_SECRET_KEY")
KIS_VIRTUAL_CLIENT_ID=os.getenv("KIS_VIRTUAL_API_KEY")
KIS_VIRTUAL_CLIENT_SECRET=os.getenv("KIS_VIRTUAL_SECRET_KEY")

virtual_token = ''
real_token = ''

# access token 발급
# https://apiportal.koreainvestment.com/apiservice-apiservice?/oauth2/tokenP
@app.route('/api/kis/access/virtual')
def virtual_access_kis():

    global virtual_token

    # KIS 인증 토큰 요청
    url = 'https://openapivts.koreainvestment.com:29443/oauth2/tokenP'

    headers = {'Content-Type' : 'application/json; charset=UTF-8'}

    body = {
        'grant_type' : 'client_credentials', 
        'appkey' : KIS_VIRTUAL_CLIENT_ID, 
        'appsecret' : KIS_VIRTUAL_CLIENT_SECRET
    }

    res = requests.post(url, headers=headers, data=json.dumps(body)).json()

    virtual_token = res.get('access_token')

    return jsonify({'result': res})


@app.route('/api/kis/access/real')
def real_access_kis():

    global real_token

    # KIS 인증 토큰 요청
    url = 'https://openapi.koreainvestment.com:9443/oauth2/tokenP'

    headers = {'Content-Type' : 'application/json; charset=UTF-8'}

    body = {
        'grant_type' : 'client_credentials', 
        'appkey' : KIS_REAL_CLIENT_ID, 
        'appsecret' : KIS_REAL_CLIENT_SECRET
    }

    res = requests.post(url, headers=headers, data=json.dumps(body)).json()

    real_token = res.get('access_token')

    return jsonify({'result': res})


# 주식 전체 조회
# https://apiportal.koreainvestment.com/apiservice-category
@app.route('/api/kis/get/stocks')
def get_stocks():
    return


# 주식 개별 조회
# https://apiportal.koreainvestment.com/apiservice-apiservice?/uapi/domestic-stock/v1/quotations/search-stock-info
@app.route('/api/kis/get/stock/<stock_num>')
def get_stock(stock_num):

    # if not real_token:
    #     return jsonify({
    #         'error': '토큰이 없습니다. /api/kis/access/real 먼저 호출하세요.'
    #     })

    # KIS 인증 토큰 요청
    url = (
        f'https://openapi.koreainvestment.com:9443'
        f'/uapi/domestic-stock/v1/quotations/search-stock-info?'
        f'PRDT_TYPE_CD=300&PDNO={stock_num}'
    )

    headers = {
        'Content-Type' : 'application/json; charset=UTF-8',
        'authorization' : f'Bearer {real_token}',
        'appkey' : KIS_REAL_CLIENT_ID,
        'appsecret' : KIS_REAL_CLIENT_SECRET,
        'tr_id' : 'CTPF1002R',
        'custtype' : 'P'
    }

    res = requests.get(url, headers=headers).json()

    return jsonify({'result': res})


if __name__ == "__main__":
    app.run(debug=True)
