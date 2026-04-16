## 함수 호출시 매개변수명을 사용

# def 함수이름(매개변수):
#     코드
#     return 반환값


def function(first, second, third):
    return first + second + third

print(3, 5, 7)
print(function(first=3, second=5, third=7))
print(function(second=5, third=7, first=3))