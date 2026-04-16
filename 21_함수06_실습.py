# 두 수와 연산자(문자열형)를 입력받아서 사칙연산을 수행하는 함수를 만드시오.

def calc(num1, op, num2):
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        result = num1 / num2
    else : result = 0
    return result
print(calc(10, '+', 5))
print(calc(10, '-', 5))
print(calc(3,'*', 5))
print(calc(2.5, '/', 3.5))