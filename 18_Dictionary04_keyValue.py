# Key, Value 가져오기

student = {'name':'홍길동', 'major':'정통과', 'score':3.5}

print(student.items())  # dict_items([('name', '홍길동'), ('major', '정통과'), ('score', 3.5)])
print(student.keys())   # dict_keys(['name', 'major', 'score'])
print(student.values()) # dict_values(['홍길동', '정통과', 3.5])

print(list(student.items()))    # [('name', '홍길동'), ('major', '정통과'), ('score', 3.5)]
print(list(student.keys()))     # ['name', 'major', 'score']
print(list(student.values()))   # ['홍길동', '정통과', 3.5]
