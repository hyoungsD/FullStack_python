
## 속성 정의와 초기화

class Person:
    def __init__(self, n, a):
        self.name = n
        self.age = a
    def hello(self):
        print('Hello {}'.format(self.name))
        print('당신은 {}살입니다'.format(self.age))

person = Person('홍길동', 20)   # Hello 홍길동
person.hello()  # 당신은 20살입니다
