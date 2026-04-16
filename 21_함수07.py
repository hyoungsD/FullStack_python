## 매개변수명의 기본값
# def 함수이름(매개변수=기본값):
#     return 반환값


def function1(first=1, second=3, third=5):
    return first + second + third
print(function1())                  # 1 3 5
print(function1(1, 2, 3))           # 1 2 3
print(function1(1, 2))              # 1 2 5
print(function1(1))                 # 1 3 5
print(function1(first=1))           # 1 3 5
print(function1(second=5))          # 1 5 5
print(function1(first=1, third=5))  # 1 3 5
print(function1(first=1, second=5)) # 1 5 5


# 기본값이 없으면 생략 불가
def function2(first, second, third=5 ):
    return first + second + third
print(function2(1, 2, 3))                       # 1 2 3
print(function2(1, 2))                          # 1 2 5
print(function2(first=1, second=2, third=10))   # 1 2 10
print(function2(1, second=5))                   # 1 5 5
print(function2(second=5, first=2))             # 2 5 5