## 맵(map) 함수와 람다
# 파이썬은 map() 이라는 내장함수를 제공하는데 열거가능한 자료형의 각 요소들에 대해서 매핑 함수를 적용한다

nums = [1, 2, 3, 4, 5]
def pow(x):
    return x ** 2
f = lambda x : x ** 2

# 같은 결과 [1, 4, 9, 16, 25]
print(list(map(pow, nums)))
print(list(map(f, nums)))
print(list(map(lambda x : x ** 2, nums)))


# 
nums1 = [1, 2, 3, 4, 5]
nums2 = [6, 7, 8, 9, 10]

print(list(map(lambda x, y : x * y, nums1, nums2))) # [6, 14, 24, 36, 50]
