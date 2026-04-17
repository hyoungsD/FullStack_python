# 필터(filter) 함수와 람다

# 리스트에서 다룬 filter() 함수는 순환가능한 요소들을 함수에 넣어 그 리턴값이 참인 것만 묶어서 반환한다.

ages = [18, 19, 39, 12, 43, 13, 21, 25]

# 함수
def adult_func(age):
    if age >= 19:
        return True
    else:
        return False

for age in filter(adult_func, ages):
    print(age)

print()

# lambda
for age in filter(lambda age: age > 19, ages):
    print(age)

adult_ages = list(filter(lambda age: age > 19, ages))
print(adult_ages)

