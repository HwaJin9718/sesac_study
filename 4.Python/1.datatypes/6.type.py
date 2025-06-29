x = 5
y = "hello"
z = [1, 2, 3]

print(type(x))
print(type(y))
print(type(z))

# 각각의 변수 타입은 클래스로 만들어져 있고, 그 안에 있는 함수를 통해서 세부 클래스의 함수들이 동작한다
# print(y.upper())
# print(x.upper())

print(isinstance(x, int)) # x는 int로 만들어 진거야?
print(isinstance(y, int)) # y는 int로 만들어 진거야?
print(isinstance(y, str)) # y는 str로 만들어 진거야?

print(isinstance(x, (int, float))) # x는 int나 float로 만들어 진거야?
print(isinstance(y, (str, list))) # y는 str나 list로 만들어 진거야?

print('-' * 10)

# 클래스 A 만들어짐
class A:
    pass # 아무것도 안해도 괜찮아

class B(A): # B extends A (A를 상속받음)
    pass

class C:
    pass

b = B() # b = new B(), b라는 변수를 B라는 클래스로 찍어냄
print(isinstance(b, A)) # True
print(isinstance(b, B)) # True
print(isinstance(b, C)) # False

a = A()
print(isinstance(a, A)) # True
print(isinstance(a, B)) # False
print(isinstance(a, C)) # False
