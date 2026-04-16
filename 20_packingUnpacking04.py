# unpacking


# Item은 넣지 않고 Key만
student = {'name': '홍길동', 'major': '정보통신', 'grade': 3}

a, b, c = student
print(a, b, c)  # name major grade


set1 = {1, 2, 3, 4}
a, *b, c = set1
print(a, b, c)  # 1 [2, 3] 4

