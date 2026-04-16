## 비공개 속성 정의
# __추가

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age    # 비공개 속성
    def hello(self):
        print('Hello {}'.format(self.name))
        print('당신은 {}살입니다'.format(self.__age))

person = Person('홍길동', 20)
person.hello()
# print(person.__age) # 에러
# Person.__age == 100 # 에러


class Person1:
    def __init__(self, name, age):
        self.name = name
        if 0 <= age <= 20 : self.__age = age
        else: self.__age = 0
    def inc_age(self):
        self.__age += 1
    def info(self):
        print(self.__age)

person1 = Person1('홍길동', 20)
person1.inc_age()
person1.info()

person2 = Person1('오늘은', 30)
person2.inc_age()
person2.info()
