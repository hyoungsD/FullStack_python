## 아이템 값가져오기

student = {'name':'홍길동', 'major':'정통과', 'score': 3.5}
print(student['name'])  # 홍길동
print(student['score']) # 3.5

scores = {1:3.5, 2:4.0, 3:4.3, 4:4.2}
print(scores[1])    # 3.5
print(scores[2])    # 4.0


# 아이템 수정, 추가
student['major'] = '정보통신과'
print(student)  # {'name': '홍길동', 'major': '정보통신과', 'score': 3.5}
student['grade'] = 4
print(student)  # {'name': '홍길동', 'major': '정보통신과', 'score': 3.5, 'grade': 4}
scores[2] = '4.5'
print(scores)   # {1: 3.5, 2: '4.5', 3: 4.3, 4: 4.2}
scores[5] = '5.0'
print(scores)   # {1: 3.5, 2: '4.5', 3: 4.3, 4: 4.2, 5: '5.0'}


# 아이템 삭제
del student['name']
print(student)  # {'major': '정보통신과', 'score': 3.5, 'grade': 4}
del scores[1]
print(scores)   # {2: '4.5', 3: 4.3, 4: 4.2, 5: '5.0'}
