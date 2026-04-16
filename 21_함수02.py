
## 매개변수가 없는 함수
# def 함수이름():
#     코드
def hello():
    print('Hello World!')
hello() # 함수 호출


## 매개변수가 있는 함수
# def 함수이름(매개변수):
#     코드
def hello1(name):
    print('Hello World!', name)
hello1('홍길동')
hello1('트와이스')    # 함수호출


## 매개변수가 복수인 함수
# def 함수이름(매개변수1, 매개변수2):
#     코드
def add(num1, num2):
    print(num1 + num2)
add(2, 3)
add(3.5, 3.14)
add('Hello ', 'World!')
