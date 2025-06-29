print("01. 파이썬 시작하기 1~10")

# 001 print 기초
# 화면에 Hello World 문자열을 출력하세요.
print("Hello World")

# 002 print 기초
# 화면에 Mary's cosmetics을 출력하세요. (중간에 '가 있음에 주의하세요)
print("Mary's cosmetics")

# 003 print 기초
# 화면에 아래 문장을 출력하세요. (중간에 "가 있음에 주의하세요.)
# 신씨가 소리질렀다. "도둑이야".
print('신씨가 소리질렀다. "도둑이야".')

# 004 print 기초
# 화면에 C:\Windows를 출력하세요.
print("C:\Windows")

# 005 print 탭과 줄바꿈
# 다음 코드를 실행해보고 \t와 \n의 역할을 설명해보세요.
print("안녕하세요.\n만나서\t\t반갑습니다.")
# 정답: \n -> 줄바꿈, \t -> 탭탭(띄어쓰기)

# 006 print 여러 데이터 출력
# print 함수에 두 개의 단어를 입력한 예제입니다. 아래 코드의 출력 결과를 예상해봅시다.
print ("오늘은", "일요일")
# 정답: 오늘은 일요일

# 007 print 기초
# print() 함수를 사용하여 다음과 같이 출력하세요.
# naver;kakao;sk;samsung
print("naver;kakao;sk;samsung")
# 정답 : print("naver", "kakao", "sk", "samsung", sep=";")

# 008 print 기초
# print() 함수를 사용하여 다음과 같이 출력하세요.
# naver/kakao/sk/samsung
print("naver", "kakao", "sk", "samsung", sep="/")

# 009 print 줄바꿈
# 다음 코드를 수정하여 줄바꿈이 없이 출력하세요. (힌트: end='') print 함수는 두 번 사용합니다. 세미콜론 (;)은 한줄에 여러 개의 명령을 작성하기 위해 사용합니다.
print("first", end='');print("second")

# 010 연산 결과 출력
# 5/3의 결과를 화면에 출력하세요.
print(5/3)

# ========================================================
print("02. 파이썬 변수 11~20")

# 011 변수 사용하기
# 삼성전자라는 변수로 50,000원을 바인딩해보세요. 삼성전자 주식 10주를 보유하고 있을 때 총 평가금액을 출력하세요.
samsung = 50000
print(samsung * 10)

# 012 변수 사용하기
# 다음 표는 삼성전자의 일부 투자정보입니다. 변수를 사용해서 시가총액, 현재가, PER 등을 바인딩해보세요.
# 항목 / 값
# 시가총액 / 298조
# 현재가 / 50,000원
# PER / 15.79
# 정답 : 시가총액 = 298000000000000; 현재가 = 50000; PER = 15.79

# 013 문자열 출력
# 변수 s와 t에는 각각 문자열이 바인딩 되어있습니다.
# >> s = "hello"
# >> t = "python"
# 두 변수를 이용하여 아래와 같이 출력해보세요.
# 실행 예:
# hello! python
s = "hello"; t = "python"
print(f"{s}! {t}")

# 014 파이썬을 이용한 값 계산
# 아래 코드의 실행 결과를 예상해보세요.
# >> 2 + 2 * 3 
# 정답 : 8

# 015 type 함수
# type() 함수는 데이터 타입을 판별합니다. 변수 a에는 128 숫자가 바인딩돼 있어 type 함수가 int (정수)형임을 알려줍니다.
# >> a = 128
# >> print (type(a))
# <class 'int'>
# 아래 변수에 바인딩된 값의 타입을 판별해보세요.
# >> a = "132"
a = "132"
print(type(a)) # <class 'str'>

# 016 문자열을 정수로 변환
# 문자열 '720'를 정수형으로 변환해보세요.
# >> num_str = "720"
num_str = "720"
print(int(num_str))

# 017 정수를 문자열 100으로 변환
# 정수 100을 문자열 '100'으로 변환해보세요.
num = 100
print(str(num))

# 018 문자열을 실수로 변환
# 문자열 "15.79"를 실수(float) 타입으로 변환해보세요.
print(float("15.79"))

# 019 문자열을 정수로 변환
# year라는 변수가 문자열 타입의 연도를 바인딩하고 있습니다. 이를 정수로 변환한 후 최근 3년의 연도를 화면에 출력해보세요.
year = "2020"
int_year = int(year)
print(f"{int_year - 3}, {int_year - 2}, {int_year - 1}")

# 020 파이썬 계산
# 에이컨이 월 48,584원에 무이자 36개월의 조건으로 홈쇼핑에서 판매되고 있습니다. 총 금액은 계산한 후 이를 화면에 출력해보세요. (변수사용하기)
amount = 48584
installment = 36
print(amount * installment)

# ========================================================
print("03. 파이썬 문자열 21~50")

# 021 문자열 인덱싱
# letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.
# >> letters = 'python'
# 실행 예 : p t
letters = 'python'
print(f"{letters[0]} {letters[2]}")

# 022 문자열 슬라이싱
# 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.
# >> license_plate = "24가 2210"
# 실행 예: 2210
license_plate = "24가 2210"
print(license_plate[len(license_plate) - 4:])

# 023 문자열 인덱싱
# 아래의 문자열에서 '홀' 만 출력하세요.
# >> string = "홀짝홀짝홀짝"
# 실행 예: 홀홀홀
string = "홀짝홀짝홀짝"
def get_char(strings):
    result = []
    for char in strings:
        if char == "홀":
            result.append(char)
    return result

print(''.join(get_char(string)))
print(string[::2]) # 자열 슬라이싱을 이용한 방법

# 024 문자열 슬라이싱
# 문자열을 거꾸로 뒤집어 출력하세요.
# >> string = "PYTHON"
# 실행 예: NOHTYP
string = "PYTHON"
print(string[::-1])

# 025 문자열 치환
# 아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하세요.
# >> phone_number = "010-1111-2222"
# 실행 예 : 010 1111 2222
phone_number = "010-1111-2222"
print(phone_number.replace("-", " "))

# 026 문자열 다루기
# 25번 문제의 전화번호를 아래와 같이 모두 붙여 출력하세요.
# 실행 예 : 01011112222
print(phone_number.replace("-", ""))

# 027 문자열 다루기
# url 에 저장된 웹 페이지 주소에서 도메인을 출력하세요.
# >> url = "http://sharebook.kr"
# 실행 예: kr
url = "http://sharebook.kr"
# print(url[-2:])
print(url.split('.')[-1])

# 028 문자열은 immutable
# 아래 코드의 실행 결과를 예상해보세요.
# >> lang = 'python'
# >> lang[0] = 'P'
# >> print(lang)
# 정답 : TypeError: 'str' object does not support item assignment : 문자열은 assignment 메서드를 지원하지 않음

# 029 replace 메서드
# 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.
# >> string = 'abcdfe2a354a32a'
# 실행 예: Abcdfe2A354A32A
string = 'abcdfe2a354a32a'
print(string.replace('a', 'A'))

# 030 replace 메서드
# 아래 코드의 실행 결과를 예상해보세요.
# >> string = 'abcd'
# >> string.replace('b', 'B')
# >> print(string)
# 정답 : abcd , 문자열은 변경할 수 없는 자료형, 문자열을 replace 진행 시 원본은 그대로 둔채 변경된 문자열을 반환, 지금 출력한건 원본 데이터이기 떄문에 abce가 나옴

# 031 문자열 합치기
# 아래 코드의 실행 결과를 예상해보세요.
# >> a = "3"
# >> b = "4"
# >> print(a + b)
# 정답 : 34, 문자열이 +에 의해서 합쳐지는 것

# 032 문자열 곱하기
# 아래 코드의 실행 결과를 예상해보세요.
# >> print("Hi" * 3)
# 정답 : HiHiHi

# 033 문자열 곱하기
# 화면에 '-'를 80개 출력하세요.
# 실행 예: --------------------------------------------------------------------------------
print("-" * 80)

# 034 문자열 곱하기
# 변수에 다음과 같은 문자열이 바인딩되어 있습니다.
# >>> t1 = 'python'
# >>> t2 = 'java'
# 변수에 문자열 더하기와 문자열 곱하기를 사용해서 아래와 같이 출력해보세요.
# 실행 예: python java python java python java python java
t1 = 'python'; t2 = 'java'
print((t1 + ' ' + t2 + ' ') * 4)

# 035 문자열 출력
# 변수에 다음과 같이 문자열과 정수가 바인딩되어 있을 때 % formatting을 사용해서 다음과 같이 출력해보세요.
# name1 = "김민수" 
# age1 = 10
# name2 = "이철희"
# age2 = 13
# 이름: 김민수 나이: 10
# 이름: 이철희 나이: 13
name1 = "김민수" ; age1 = 10; name2 = "이철희"; age2 = 13
print("이름: %s 나이: %d \n이름: %s 나이: %d" % (name1, age1, name2, age2))

# 036 문자열 출력
# 문자열의 format( ) 메서드를 사용해서 035번 문제를 다시 풀어보세요.
print("이름: {0} 나이: {2} \n이름: {1} 나이: {3}".format(name1, name2, age1, age2))

# 037 문자열 출력
# 파이썬 3.6부터 지원하는 f-string을 사용해서 035번 문제를 다시 풀어보세요.
print(f"이름: {name1} 나이: {age1} \n이름: {name2} 나이: {age2}")

# 038 컴마 제거하기
# 삼성전자의 상장주식수가 다음과 같습니다. 컴마를 제거한 후 이를 정수 타입으로 변환해보세요.
# 상장주식수 = "5,969,782,550"
str = "5,969,782,550"
int_str = int(str.replace(',', ''))
print(int_str)

# 039 문자열 슬라이싱
# 다음과 같은 문자열에서 '2020/03'만 출력하세요.
# 분기 = "2020/03(E) (IFRS연결)"
str = "2020/03(E) (IFRS연결)"
str_split = str.split('(')
print(str_split[0])
print(str[:7]) # 문자열 슬라이싱으로 풀었을 떄

# 040 strip 메서드
# 문자열의 좌우의 공백이 있을 때 이를 제거해보세요.
data = "   삼성전자    "
print(data.strip())

# 041 upper 메서드
# 다음과 같은 문자열이 있을 때 이를 대문자 BTC_KRW로 변경하세요.
ticker = "btc_krw"
print(ticker.upper())

# 042 lower 메서드
# 다음과 같은 문자열이 있을 때 이를 소문자 btc_krw로 변경하세요.
ticker = "BTC_KRW"
print(ticker.lower())

# 043 capitalize 메서드
# 문자열 'hello'가 있을 때 이를 'Hello'로 변경해보세요.
str = "hello"
print(str.capitalize())

# 044 endswith 메서드
# 파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx'로 끝나는지 확인해보세요.
file_name = "보고서.xlsx"
print(file_name.endswith("xlsx"))

# 045 endswith 메서드
# 파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx' 또는 'xls'로 끝나는지 확인해보세요.
file_name = "보고서.xlsx"
print(file_name.endswith(("xlsx", "xls")))

# 046 startswith 메서드
# 파일 이름이 문자열로 저장되어 있을 때 startswith 메서드를 사용해서 파일 이름이 '2020'로 시작하는지 확인해보세요.
file_name = "2020_보고서.xlsx"
print(file_name.startswith("2020"))

# 047 split 메서드
# 다음과 같은 문자열이 있을 때 공백을 기준으로 문자열을 나눠보세요.
a = "hello world"
print(a.split())

# 048 split 메서드
# 다음과 같이 문자열이 있을 때 btc와 krw로 나눠보세요.
ticker = "btc_krw"
print(ticker.split('_'))

# 049 split 메서드
# 다음과 같이 날짜를 표현하는 문자열이 있을 때 연도, 월, 일로 나눠보세요.
date = "2020-05-01"
print(date.split('-'))

# 050 rstrip 메서드
# 문자열의 오른쪽에 공백이 있을 때 이를 제거해보세요.
data = "039490     "
print(data.rstrip())

# ========================================================
print("04. 파이썬 리스트 51~70")

# ========================================================
print("05. 파이썬 튜플 71~80")

# ========================================================
print("06. 파이썬 딕셔너리 81~100")

# ========================================================
print("07. 파이썬 분기문 101~130")

# ========================================================
print("08. 파이썬 반복문 131~200")

# ========================================================
print("09. 파이썬 함수 201~240")

# 201 - "비트코인" 문자열을 화면에 출력하는 print_coin() 함수를 정의하라.
def print_coin():
    print("비트코인")

# 202 - 201번에서 정의한 함수를 호출하라.
print_coin()

# 203 - 201번에서 정의한 print_coin 함수를 100번호출하라.
for i in range(100):
    print_coin()

# 204 - "비트코인" 문자열을 100번 화면에 출력하는 print_coins() 함수를 정의하라.
def print_coins():
    for i in range(100):
        print("비트코인")

# 205
# 아래의 에러가 발생하는 이유에 대해 설명하라.
# hello()
# def hello():
#     print("Hi")
# 실행 예 : NameError: name 'hello' is not defined
# 정답 : 함수 호출 위치, hello()라는 함수가 생성되기 전 함수를 호출하여 NameError 발생

# 206 - 아래 코드의 실행 결과를 예측하라.
# def message() :
#     print("A")
#     print("B")
# message()
# print("C")
# message()
# 정답 : A B C A B (각 단어당 한줄씩 차지함)

# 207 - 아래 코드의 실행 결과를 예측하라. (읽기 어려운 코드의 예입니다.)
# print("A")
# def message() :
#     print("B")
# print("C")
# message()
# 정답 : A C B (각 단어당 한줄씩 차지함)

# 208 - 아래 코드의 실행 결과를 예측하라. (읽기 어려운 코드의 예입니다.)
# print("A")
# def message1() :
#     print("B")
# print("C")
# def message2() :
#     print("D")
# message1()
# print("E")
# message2()
# 정답 : A C B E D (각 단어당 한줄씩 차지함)

# 209 - 아래 코드의 실행 결과를 예측하라.
# def message1():
#     print("A")
# def message2():
#     print("B")
#     message1()
# message2()
# 정답 : B A (각 단어당 한줄씩 차지함)

# 210 - 아래 코드의 실행 결과를 예측하라.
# def message1():
#     print("A")
# def message2():
#     print("B")
# def message3():
#     for i in range (3) :
#         message2()
#         print("C")
#     message1()
# message3()
# 정답 : B C B C B C A (각 단어당 한줄씩 차지함)

# 211 - 함수의 호출 결과를 예측하라.
# def 함수(문자열) :
#     print(문자열)
# 함수("안녕")
# 함수("Hi")
# 정답 : 안녕 Hi (각 단어당 한줄씩 차지함)

# 212 - 함수의 호출 결과를 예측하라.
# def 함수(a, b) :
#     print(a + b)
# 함수(3, 4)
# 함수(7, 8)
# 정답 : 7 15 (각 단어당 한줄씩 차지함)

# 213 - 아래와 같은 에러가 발생하는 원인을 설명하라.
# def 함수(문자열) :
#     print(문자열)
# 함수()
# TypeError: 함수() missing 1 required positional argument: '문자열'
# 정답 : 함수를 호출 시 문자열이라는 필수 인자값이 필요하나 입력되지 않아서 오류 발생

# 214 - 아래와 같은 에러가 발생하는 원인을 설명하라.
# def 함수(a, b) :
#     print(a + b)
# 함수("안녕", 3)
# TypeError: must be str, not int
# 정답 : 숫자와 문자는 더할 수 없어서 type 오류 발생

# 215 - 하나의 문자를 입력받아 문자열 끝에 ":D" 스마일 문자열을 이어 붙여 출력하는 print_with_smile 함수를 정의하라.
def print_with_smile(string):
    print(f"{string} :D")

# 216 - 215에서 정의한 함수를 호출하라. 파라미터는 "안녕하세요"로 입력하라.
print_with_smile("안녕하세요")

# 217 - 현재 가격을 입력 받아 상한가 (30%)를 출력하는 print_upper_price 함수를 정의하라.
def print_upper_price(price):
    print(price + (price * 0.3))

# 218 - 두 개의 숫자를 입력받아 두 수의 합을 출력하는 print_sum 함수를 정의하라.
def print_sum(a,b):
    print(a + b)

# 219 - 두 개의 숫자를 입력받아 합/차/곱/나눗셈을 출력하는 print_arithmetic_operation 함수를 작성하라.
# print_arithmetic_operation(3, 4)
# 3 + 4 = 7
# 3 - 4 = -1
# 3 * 4 = 12
# 3 / 4 = 0.75
def print_arithmetic_operation(a, b):
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    print(f"{a} / {b} = {a / b}")

# 220 - 세 개의 숫자를 입력받아 가장 큰수를 출력하는 print_max 함수를 정의하라. 단 if 문을 사용해서 수를 비교하라.
def print_max(a, b, c):                             
    max_num = a
    if b > max_num:
        max_num = b
    if c > max_num:
         max_num = c

    return print(max_num)

# 221 = 입력된 문자열을 역순으로 출력하는 print_reverse 함수를 정의하라.
# print_reverse("python")
# nohtyp
def print_reverse(string):
    print(string[::-1])

# 222 - 성적 리스트를 입력 받아 평균을 출력하는 print_score 함수를 정의하라.
# print_score ([1, 2, 3])
# 2.0
def print_score(score):
    result = 0
    for i in score:
        result = result + i
    return print(result / (len(score)))

# 223 - 하나의 리스트를 입력받아 짝수만 화면에 출력하는 print_even 함수를 정의하라.
# print_even ([1, 3, 2, 10, 12, 11, 15])
# 2
# 10
# 12
def print_even(list):
    for i in list:
        if i % 2 == 0:
            print(i)

# 224 - 하나의 딕셔너리를 입력받아 딕셔너리의 key 값을 화면에 출력하는 print_keys 함수를 정의하라.
# print_keys ({"이름":"김말똥", "나이":30, "성별":0})
# 이름
# 나이
# 성별
def print_keys(dict): # 내가 쓴거
    print(dict.keys)

def print_keys(dict): # 답이라고 하는거
    for key in dict.keys:
        print(key)

# 225 - my_dict에는 날짜를 키값으로 OHLC가 리스트로 저장돼 있다.
# my_dict = {"10/26" : [100, 130, 100, 100],
#            "10/27" : [10, 12, 10, 11]}
# my_dict와 날짜 키값을 입력받아 OHLC 리스트를 출력하는 print_value_by_key 함수를 정의하라.
# print_value_by_key  (my_dict, "10/26")
# [100, 130, 100, 100]
def print_value_by_key(my_dict, date):
    print(my_dict[date])

# 226 - 입력 문자열을 한 줄에 다섯글자씩 출력하는 print_5xn(string) 함수를 작성하라.
# print_5xn("아이엠어보이유알어걸")
# 아이엠어보
# 이유알어걸
def print_5xn(string):
    # print(string[::5])
    for i in range(0, len(string), 5):
        print(string[i:i+5])

# 227 - 문자열과 한줄에 출력될 글자 수를 입력을 받아 한 줄에 입력된 글자 수만큼 출력하는 print_mxn(string) 함수를 작성하라.
# printmxn("아이엠어보이유알어걸", 3)
# 아이엠
# 어보이
# 유알어
# 걸
def print_mxn(string, num):
    for i in range(0, len(string), num):
        print(string[i:i+num])

# 228 - 연봉을 입력받아 월급을 계산하는 calc_monthly_salary(annual_salary) 함수를 정의하라. 회사는 연봉을 12개월로 나누어 분할 지급하며, 이 때 1원 미만은 버림한다.
# calc_monthly_salary(12000000)
# 1000000
def calc_monthly_salary(annual_salary):
    month = int(annual_salary / 12)
    print(month)

# 229 - 아래 코드의 실행 결과를 예측하라.
def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)
my_print(a=100, b=200)
# 정답 : 왼쪽: 100 오른쪽: 200 (각 항목당 한줄씩)

# 230 - 아래 코드의 실행 결과를 예측하라.
def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)
my_print(b=100, a=200)
# 정답 : 왼쪽: 200 오른쪽: 100 (각 항목당 한줄씩)

# 231 - 아래 코드를 실행한 결과를 예상하라.
# def n_plus_1 (n) :
#     result = n + 1
# n_plus_1(3)
# print (result)
# 정답 : 에러 발생, 함수 내에 있는 result 값에 함수 밖에서 접근 불가!

# 232 - 문자열 하나를 입력받아 인터넷 주소를 반환하는 make_url 함수를 정의하라.
# make_url("naver")
# www.naver.com
def make_url(string):
    print(f"www.{string}.com")

# 233 - 문자열을 입력받아 각 문자들로 구성된 리스트로 반환하는 make_list 함수를 정의하라.
# make_list("abcd")
# ['a', 'b', 'c', 'd']
def make_list(string):
    list = []
    for i in string:
        list.append(i)
    return list

def make_list (string) :
    return list(string)

# 234 - 숫자로 구성된 하나의 리스트를 입력받아, 짝수들을 추출하여 리스트로 반환하는 pickup_even 함수를 구현하라.
# pickup_even([3, 4, 5, 6, 7, 8])
# [4, 6, 8]
def pickup_even(numbers):
    even = []
    for num in numbers:
        if num % 2 == 0:
            even.append(num)
    return even

# 235 - 콤마가 포함된 문자열 숫자를 입력받아 정수로 변환하는 convert_int 함수를 정의하라.
# convert_int("1,234,567")
# 1234567
def convert_int(string):
    return int(string.replace(',', ''))

# 236 - 아래 코드의 실행 결과를 예측하라.
# def 함수(num) :
#     return num + 4
# a = 함수(10)
# b = 함수(a)
# c = 함수(b)
# print(c)
# 정답: 22

# 237 - 아래 코드의 실행 결과를 예측하라.
# def 함수(num) :
#     return num + 4
# c = 함수(함수(함수(10)))
# print(c)
# 정답: 22

# 238 - 아래 코드의 실행 결과를 예측하라.
# def 함수1(num) :
#     return num + 4
# def 함수2(num) :
#     return num * 10
# a = 함수1(10)
# c = 함수2(a)
# print(c)
# 정답: 140

# 239 - 아래 코드의 실행 결과를 예측하라.
# def 함수1(num) :
#     return num + 4
# def 함수2(num) :
#     num = num + 2
#     return 함수1(num)
# c = 함수2(10)
# print(c)
# 정답: 16

# 240 - 아래 코드의 실행 결과를 예측하라.
# def 함수0(num) :
#     return num * 2
# def 함수1(num) :
#     return 함수0(num + 2)
# def 함수2(num) :
#     num = num + 10
#     return 함수1(num)
# c = 함수2(2)
# print(c)
# 정답: 28

# ========================================================
print("10. 파이썬 모듈 241~250")

# 241 현재시간 - datetime 모듈을 사용해서 현재 시간을 화면에 출력해보세요.
import datetime
now = datetime.datetime.now()
print(now)

# 242 현재시간의 타입 - datetime 모듈의 now 함수의 리턴 값의 타입을 화면에 출력해보세요.
print(now, type(now))

# 243 timedelta - datetime 모듈의 timedelta를 사용해서 오늘로부터 5일, 4일, 3일, 2일, 1일 전의 날짜를 화면에 출력해보세요.
for day in range(5, 0, -1):
    print(now - datetime.timedelta(days=day))

# 244 strftime - 현재시간을 얻어온 후 다음과 같은 포맷으로 시간을 출력해보세요. strftime 메서드를 사용하세요.
# 18:35:01 
print(now.strftime("%H:%M:%S"))

# 245 strptime - datetime.datetime.strptime 메서드를 사용하면 문자열 형식의 시간을 datetime.datetime 타입의 시간 값으로 만들어줍니다. 
# "2020-05-04"의 문자열을 시간 타입으로 변환해보세요.
print(datetime.datetime.strptime("2020-05-04", "%Y-%m-%d"))

# 246 sleep 함수 - time 모듈, datetime 모듈을 사용해서 1초에 한 번 현재 시간을 출력하는 코드를 작성하세요.
# import time
# while True: # 무한 반복 코드
#     print(now)
#     time.sleep(1)

# 247 모듈 임포트 - 모듈을 임포트하는 4가지 방식에 대해 설명해보세요.
# 정답 : 1. import 모듈명 , 2. from 모듈명 import 함수명 , 3. from 모듈명 import * , 4. import 모듈명 as 별칭

# 248 os 모듈 - os 모듈의 getcwd 함수를 호출하여 현재 디렉터리의 경로를 화면에 출력해보세요.
from os import getcwd
path = getcwd()
print(path)

# 249 rename 함수 - 바탕화면에 텍스트 파일을 하나 생성한 후 os 모듈의 rename 함수를 호출하여 해당 파일의 이름을 변경해보세요.
from os import rename
# rename("D:/study/SeSAC/test2/test.txt", "D:/study/SeSAC/test2/modify.txt")

# 250 numpy - numpy 모듈의 arange 함수를 사용해서 0.0 부터 5.0까지 0.1씩 증가하는 값을 화면에 출력해보세요.
from numpy import arange
print(arange(0.0, 5.0, 0.1))

# ========================================================
print("11. 파이썬 클래스 251~290")

# ========================================================
print("12. 파일 입출력과 예외처리 291~300")