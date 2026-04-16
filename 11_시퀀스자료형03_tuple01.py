## Tuple

# •tuple는 일련번호로 구분되는 순서에 따라 데이터가 정렬된 목록 형태의 자료형
# •tuple은 문자열, 정수, 실수 등 모든 자료형을 섞어서 저장할 수 있음
# •list와 달리 내용을 변경 할수 없음(immutable)
# •()를 사용함


student = ('전정국', '인공지능학과', 3, 175.3, 3.5, True)
print(student)
print(student[0])
# student[0] = '정국' # 에러 immutable

car = ('Tesla', 'model3', 'red', 500)
print(car)

