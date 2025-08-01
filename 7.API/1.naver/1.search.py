import urllib.request # request보다 파싱이 편해서 사용
import json

# 발급받은 ID/Secret 을 입력
client_id = "" 
client_secret = ""

text = "Python 개발"
encText = urllib.parse.quote(text)

# url = 'https://openapi.naver.com/v1/search/blog?query=' + text # 띄어쓰기가 들어가짐
url = 'https://openapi.naver.com/v1/search/blog?query=' + encText

print(url)

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)

response = urllib.request.urlopen(request)
print(response)
rescode = response.getcode()
print(rescode)

if rescode == 200:
    response_body = response.read()
    print(response_body.decode('utf-8'))
