## list 축약표현


# [{표현식} for {변수} in iterable]
list1 = list(range(1, 10))

list2 = list(map(lambda x : x**2, list1))    # map, lambda
print(list2)    # [1, 4, 9, 16, 25, 36, 49, 64, 81]

list3 = [x**2 for x in list1]   # 축약표현
print(list3)    # [1, 4, 9, 16, 25, 36, 49, 64, 81]

list4 = [x**2 for x in range(1, 10)]    # 축약표현
print(list4)    # [1, 4, 9, 16, 25, 36, 49, 64, 81]


# [{표현식} for {변수} in iterable if 조건문]
# 조건이 참인것만 필터링됨

# 조건문에 따라 5보다 큰 값만 필터링
list5 = [x**2 for x in list1 if x > 5]
print(list5)    # [36, 49, 64, 81]

# 조건문에 따라 짝수 값만 필터링
list6 = [x**2 for x in range(1, 10) if x % 2 == 0]
print(list6)    # [4, 16, 36, 64]
