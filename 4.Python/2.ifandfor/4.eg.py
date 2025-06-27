numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 여기를 순회하며 짝수만 고르시오
for num in numbers:
    if num % 2 == 0:
        print(f"숫자 {num}은 짝수 입니다.")
    elif num % 2 == 1:
        print(f"숫자 {num}은 홀수 입니다.")

print('-' * 5)

# 위 내용을 함수로 만들면
def getEvenNumbers(numbers):

    even_numbers = []

    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)

    return even_numbers

even = getEvenNumbers(numbers)
print("짝수는:", even)
print(f"짝수는: {even}")

print('-' * 5)

# 다음 목록에서 성적이 A인 학생만 반환하시오
students = {
    '김철수' : 70,
    '이영희' : 82,
    '박민수' : 88,
    '최지은' : 75,
    '장현우' : 93,
    '서민정' : 67,
    '정우성' : 99,
    '한지민' : 76,
    '오세훈' : 61,
    '송지효' : 85,
}

def getGrade(score):
    scoreInt = int(score)

    if scoreInt >= 90:
        grade = "A학점"
    elif scoreInt >= 80:
        grade = "B학점"
    elif scoreInt >= 70:
        grade = "C학점"
    else:
        grade = "F학점"
    return grade

def getAGrade(students):
    studentAGrade = []
    for name, score in students.items: # 이름 name , 점수 score
        if getGrade(score) == 'A학점':
            studentAGrade.append(name)
    return studentAGrade

student = getAGrade(students)
print(f"A등급인 학생은 {student}")

