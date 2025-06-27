name = "Alice"
print(name)

print("Hello,", name)
print("Hello," + name) # 콤마(,) 는 띄어쓰기를 하지 않아도 사이에 자동으로 띄어쓰기를 해줌
print("Hello," + name) # 플러스(+)는 띄어쓰기 안해줌, 그냥 str을 덧셈 연산한것
print("Hello," + name + "!!")

print("Hello, {}!!".format(name))
print("Hello, {}!! {}??".format(name, name))

name1 = "Bob"
name2 = "Charlie"
print("Hello, {}!! {}??".format(name1, name2))
print("Hello, {0}!! {1}??".format(name, name))
print("Hello, {1}!! {0}??".format(name, name))

print("Hello, %s!!" % name) # %s 는 문자열을 출력하는 곳
print("Hello, %s!! %s??" % (name1, name2))

# 위에 다양한 것을 거쳐서 지금 가장 많이 쓰는 건
# f-스트링 표기법 (JS에서 `${변수} 백틱안에 포멧팅하듯이`)

print(f"Hello, {name}!!")
print(f"Hello, {name1}!! {name2}!!")