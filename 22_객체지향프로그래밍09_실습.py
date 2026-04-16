
# 사각형을 관리하는 클래스를 정의하라.
# 가로, 세로를 저장하는 속성을 정의하라.
# 가로, 세로로 면적을 반환하는 메소드를 정의하라
# 가로, 세로를 각각 두배로 만드는 메서드를 정의하라


class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def double(self):
        self.width *= 2
        self.height *= 2

rect = Rectangle(10, 20)
print(rect.area())
rect.double()
print(rect.width, rect.height)
