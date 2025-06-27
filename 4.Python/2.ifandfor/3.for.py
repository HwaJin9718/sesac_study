for i in range(5):
    print(i)

print("-" * 5)

for i in [0, 1, 2, 3, 4]:
    print(i)

print("-" * 5)

for i in range(1, 10): # range는 끝값은 포함하지 않는다, 10은 포함하지 않는다
    print(i)

print("-" * 5)

for i in range(1, 10, 2): # 1부터 10까지 2씩 건너뛴다
    print(i)

print("-" * 5)

for i in range(1, 10, 3): # 1부터 10까지 3씩 건너뛴다
    print(i)

print("-" * 5)

fruits = ['apple', 'banana', 'cherry']
for f in fruits:
    print(f)

print("-" * 5)

for index, fruit in enumerate(fruits): # enumerate 는 index 와 값을 같이 준다!!
    print(index, fruit)

print("-" * 5)

for i, f in enumerate(fruits): # 지금 시대는 이거(f)보다는 위에처럼 길고 설명/이해하기 좋은게 잘 작성한 변수
    print(i, f)

print("-" * 5)

str = "Hello, World!"
for char in str:
    print(char)

print("-" * 5)

count_o = 0
for char in str:
    if char == 'o':
        count_o += 1 # count_o = count_o + 1

print(f"{str} 문장 내의 o의 갯수는 {count_o} 개 입니다.")

count_l = 0
for char in str:
    if char == 'l':
        count_l += 1

print(f"{str} 문장 내의 o의 갯수는 {count_l} 개 입니다.")
