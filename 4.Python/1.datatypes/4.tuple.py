# 튜플 = 리스트와 동일하나, 데이터의 변경을 할 수 없음
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[-1])

# my_tuple[2] = 5 # 이건 오류 발생, 튜플 데이터는 수정 불가!!
# 만약 수정을 꼭 해야한다면 타입을 바꾸거나 복제본을 만들어서 쓰거나

my_list = list(my_tuple) # 튜플을 리스트로 변환 (복제본이 생김)
my_list[2] = 5
print(my_list)
print(my_tuple)

my_tuple2 = tuple(my_list) # 이러면 복제본이 생기는 것!
# my_tuple2[2] = 10 # 이건 튜플 데이터이기 때문에 오류 발생

# 튜플안에 데이터를 여러개의 변수로 나누어 담을 수 있음
# 튜플 언패킹

a, b, c = (1, 2, 3)
print(a)
print(b)
print(c)

a, b, _ = (1, 2, 3) # 값을 받아오는데 안쓸 변수는 _(언더바)로 표기, 파이썬의 관행!
print(a)
print(b)
# print(c)

a, _, c = (1, 2, 3) # 값을 받아오는데 안쓸 변수는 _(언더바)로 표기, 파이썬의 관행!
print(a)
# print(b)
print(c)