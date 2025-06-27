# 딕셔너리라고 부름
# key: value 로 구분
# JSON의 공식 문법은 쌍따옴표(")로 감싸진 키-벨류
# Dict의 공식 문법은 싱글따옴표(')로 감싸진 키-벨류
my_dict = {"name": "Alice", "age": 25, "location": "Seoul"}
print(my_dict)

print(my_dict["name"])
print(my_dict["age"])

user1 = {"name": "Bob", "age": 30, "location": "Busan"}
print(user1["name"])
print(user1["age"])
print(user1["location"])

user1["age"] = 31
print(user1["age"])
print(user1)

user1["car"] = "현대 K5"
print(user1)

user1["car"] = "" # 값을 지웠지만 삭제된 건 아님

# 특정 키값을 지우는 키워드가 del 키워드
del user1["car"]
print(user1)

# 주요 키워드로 변수명, 함수명 하면 안됨!! 주요 키워드는 다 외워야 함
# del = 5
# print = "hello, print"
# print(print)
# for = 5

print(user1.keys()) # 모든 키
print(user1.values()) # 모든 값만
print(user1.items()) # key-value 쌍으로 출력

user_item = user1.items() # 튜플에 담김
useritem_list = list(user_item)
print(useritem_list)
print(useritem_list[1])

# 리스트와 튜플과 딕셔너리를 구분할 줄 알고 자유롭게 다룰줄 알면 됨
# [], (), {}
