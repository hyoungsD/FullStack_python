
# 학생 클래스를 정의하라.
# 학년, 반, 이름의 세 가지 속성을 가진다.
# 속성은 생성자를 통해서 설정된다.
# '몇학년 몇반 누구입니다.' 라고 출력하는 intro 메소드를 정의하라.

class Student():
    def __init__(self, grade, ban, name):
        self.grade = grade
        self.ban = ban
        self.name = name
    def intro(self):
        print('{}학년 {}반 {}입니다'.format(self.grade, self.ban, self.name))

student1 = Student(2, 3, '홍길동')
student1.intro()
student2 = Student(4, 1, '진')
student2.intro()
student3 = Student(3, 8, '엄홍도')
student3.intro()
