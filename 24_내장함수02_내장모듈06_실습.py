## ramdom 모듈을 이용해서 두 가지 방법으로 lotto 발생 함수를 만드시오.

import random

# 1. while 루프와 randint 함수를 이용
set1 = set()
while len(set1) < 6 :
    set1.add(random.randint(1, 45))
print(set1)
result = sorted(set1)
print(type(result))
print(result)


# 2. shuffle 함수를 이용
list1 = list(range(1, 46))
random.shuffle(list1)
result = list1[0:6]
result.sort()
print(result)


# 3. sample 함수를 이용
list2 = list(range(1, 46))
result = random.sample(list2, 6)
result.sort()
print(result)

