## range를 이용한 tuple 생성


range1 = range(10)
tuple1 = tuple(range1)
print(tuple1)   # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

range2 = range(-5, 15, 2)
print(tuple(range2))    # (-5, -3, -1, 1, 3, 5, 7, 9, 11, 13)

