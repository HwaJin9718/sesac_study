# 데이터베이스
# 딕셔너리를 여러개 가지고 있는 리스트
users = [
    {"name": "Alice", "age": 25, "location": "Seoul", "car": "BMW"},
    {"name": "Bob", "age": 30, "location": "Busan", "car": "Mercedes"},
    {"name": "Charlie", "age": 35, "location": "Daegu", "car": "Audi"},
    {"name": "Charlie", "age": 40, "location": "Suwon", "car": "Audi"},
    {"name": "Bob", "age": 40, "location": "Jeju", "car": "Mercedes"},
]

# 사용자 이름을 기반으로, 해당 사용자의 정보를 가져오는 코드 구현하기

# for u in users:
#     print(u)

def find_user(name):
    for u in users:
        if u["name"] == name:
            return u

def find_users(name):
    result = []
    for u in users:
        if u["name"] == name:
            result.append(u)
    return result

def find_users_caseinsensitive(name):
    result = []
    for u in users:
        if u["name"].lower() == name.lower(): # DB 내용도, 사용자의 입력도 모두다 소문자로 바꿔서 비교

            result.append(u)
    return result

# print(find_user("Alice"))
# print(find_user("Charlie"))
# print(find_user("David"))
# print(find_user("Bob")) # 40세의 Bob이 나오지 않음
# print(find_users("Bob")) # 40세의 Bob까지 나옴

# print(find_users_caseinsensitive("bob"))
# print(find_users_caseinsensitive("BOB"))


def find_user2(name, age):
    for u in users:
        if u["name"] == name and u["age"] ==age:
        # if (u["name"] == name) & (u["age"] ==age): # 이것도 쓸수 있는데 위 표현이 가장 파이썬 스러움
        # if u["name"] == name & u["age"] ==age: # 괄호()를 넣지 않으면 파이썬의 연산자 우선순위 때문에 연산이 틀려질 수 있음 or 오류가 나거나
            return u

print(find_user2('Alice', 25))
print(find_user2('Bob', 30))
print(find_user2('bob', 40))

print('--- find_user3 할차례 ---')

def find_user3(name=None, age=None):
    result = []

    for u in users:
        if name:
            if u["name"] == name:
                if age:
                    if u["age"] == age: # 둘다 매치된 상황
                        result.append(u)
                else: # 이름은 메치가 됐고 나이는 신경쓰지 않는 경우
                    result.append(u)
        # 이름이 없고, 나이만 있는 경우
        elif age:
            if u["age"] == age:
                result.append(u)
        else:
            result.append(u)

    return result

print(find_user3(name='Bob'))
print(find_user3(age=40))
print(find_user3('Bob', 40))
print(find_user3(age=40, name="Bob"))

print('--- 간단한 버전 재구현 ---')

def find_user3_simple(name=None, age=None):
    result = []

    for u in users:
        if name is not None and age is not None:
            # 이름도 있고 나이도 있음
            if u["name"] == name and u["age"] == age:
                result.append(u)
        elif name is not None:
            # 이름만 있음
            if u["name"] == name:
                result.append(u)
        elif age is not None:
            # 나이만 있음
            if u["age"] == age:
                result.append(u)
        else: # 둘다 없으면, 모든 사용자 반환
            result.append(u)
    
    return result

print(find_user3_simple(name='Bob'))
print(find_user3_simple(age=40))
print(find_user3_simple('Bob', 40))
print(find_user3_simple(age=40, name="Bob"))

print('--- 더 간단한 버전 재구현 ---')

def find_user3_simplest(name=None, age=None):
    return [u         for u in users         if (name is None or u["name"] == name) and (age is None or u["age"] == age)]



print(find_user3_simplest(name='Bob'))
print(find_user3_simplest(age=40))
print(find_user3_simplest('Bob', 40))
print(find_user3_simplest(age=40, name="Bob"))
