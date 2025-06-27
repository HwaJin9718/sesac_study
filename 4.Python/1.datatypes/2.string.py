str = "Hello, World!"
str2 = "  Welcome to sesac class  "
print(str)

# 쓰고싶은 기능을 개발자들이 파이썬 라이브러리 함수들로 만들어 놨음 -> python.org 사이트에서 확인 가능
print(str.lower())
print(str.upper())
print(str.capitalize()) # 문장의 시작만 대문자로
print(str2.title()) # 문장의 단어 단어 마다 대문자로
print(str2.strip()) # 앞뒤 불필요한 공백 제거
print(str2.lstrip()) # 앞 불필요한 공백 제거
print(str2.rstrip()) # 뒤 불필요한 공백 제거
print(str.split()) # 문장을 단어 단위로 짜른다
print(str2.split()) # 문장을 단어 단위로 짜른다

words = str2.split()
print(words[0])
print(words[2])
print(words[2].upper())

print(",".join(words)) # 콤마(,)로 조인
print(" ".join(words)) # 띄어쓰기로 조인
print("-".join(words)) # 빼기(-)로 조인

print(str.startswith("Hello")) # true
print(str.startswith("hello")) # false