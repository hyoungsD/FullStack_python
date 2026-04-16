
# 두 수를 매개변수로 전달받아 몫과 나머지를 튜플로 반환하는 함수를 만드시오.
# divide(15, 4) 실행하면 (3, 3)을 반환하는 식으로 만드시오.


def divide(num1, num2):
    q = num1 // num2
    r = num1 % num2
    return (q, r)

print(divide(15, 4))

t = divide(25, 6)
print(t)
q, r = divide(25, 6)
print(q, r)
q, _ = divide(25, 6)
print(q)
