
# list는 일련번호로 구분되는 순서에 따라 데이터가 정렬된 목록 형태의 자료형
# 리스트는 문자열, 정수, 실수 등 모든 자료형을 섞어서 저장할 수 있음
# 리스트의 값은 변경가능(mutable)

scores = [30, 50, 90, 89, 56, 87, 45]
print(scores)
items = [1, 3, 'Hello', 5.6, False, 89, 'World!']
print(items)



# 개별데이터를 조회할 때는 index를 사용
# index의 범위는 0 부터 list의 길이-1
# 범위를 벗어나면 오류
# -index는 역순

scores = [30, 50, 90, 89, 56, 87]
score0 = scores[0]
print(score0)   # 30
print(scores[5])    # 87
print(scores[0])    # 30
print(scores[-1])   # 87
print(scores[-3])   # 89


# 개별데이터의 값을 바꿀때는 index를 사용
# -index는 역순
# 범위를 벗어나면 오류

scores[1] = 100
print(scores)   # [30, 100, 90, 89, 56, 87]
scores[3] = 200
print(scores)   # [30, 100, 90, 200, 56, 87]

scores[-1] = 300
print(scores)   # [30, 100, 90, 200, 56, 300]

# scores[6] = 400 # IndexError: list assignment index out of range



scores.append(99)
scores.append('Hello')
print(scores) # [30, 100, 90, 200, 56, 300, 99, 'Hello']

scores.insert(1, 33)
scores.insert(2, 'World')
print(scores)   # [30, 33, 'World', 100, 90, 200, 56, 300, 99, 'Hello']



