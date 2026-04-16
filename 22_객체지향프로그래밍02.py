## 클래스의 정의
class Person:
    def hello(self):
        print('Hello')

person = Person()
person.hello()  # Hello
person1 = Person()
person1.hello() # Hello


## 속성 정의
# self가 반드시 들어가야함
class Person:
    def __init__(self):
        self.hi = 'Hello'
    def hello(self):
        print(self.hi)
person = Person()
person.hello()  # Hello
print(person.hi)    #Hello

