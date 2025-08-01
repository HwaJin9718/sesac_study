import requests
import json
from dotenv import load_dotenv
import os
from tabulate import tabulate # pip install tabulate

load_dotenv() # .env 파일을 읽어서 거기있는 내용을 메모리에 둠(저장)

# 발급받은 ID/Secret 을 입력
client_id = os.getenv("NAVER_CLIENT_ID")
client_secret = os.getenv("NAVER_CLIENT_SECRET")

text = "한미 관세"
encText = requests.utils.quote(text)

url = 'https://openapi.naver.com/v1/search/news?query=' + encText

headers = {
    "X-Naver-Client-Id" : client_id,
    "X-Naver-Client-Secret" : client_secret
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    response_body = response.text
    # print(response_body)

    data = json.loads(response_body)

    selected_columns = [{"title", "link", "description"}]
    for item in data['items']:
        # print(item['title'], item['link'])
        selected_columns.append([item['title'], item['link'], item['description']])

    print(tabulate(selected_columns, headers="firstrow", tablefmt="list")) # tablefmt : 보기 편하게 포멧팅 해주는 것
