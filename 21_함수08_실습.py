# 점수를 입력받아 평점을 구하는 함수를 만드시오.
# calcGrade(95)를 실행하면 ‘A’를 반환하는 식으로 만드시오.

def calcGrade(score):
    if score >= 90:
        result = 'A'
    elif score >= 80:
        result = 'B'
    elif score >= 70:
        result = 'C'
    elif score >= 60:
        result = 'D'
    else:
        esult = 'F'
    return result
print(calcGrade(89))
print(calcGrade(95))
print(calcGrade(77))
print(calcGrade(50))
