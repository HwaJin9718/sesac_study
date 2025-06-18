
# 뒤집힌 문자열 (입문_LV.0)
# 문제 설명
# 문자열 my_string이 매개변수로 주어집니다. 
# my_string을 거꾸로 뒤집은 문자열을 return하도록 solution 함수를 완성해주세요.
# my_string = "jaron" return ="noraj" / my_string = "bread" return ="daerb"


def solution(my_string):

    result = []
    num = len(my_string)

    for i in range(num):
        result.append(my_string[num-1-i])

    answer = ''.join(map(str, result))
    return answer

