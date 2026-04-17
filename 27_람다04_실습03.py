
# 1부터 10 사이의 정수를 가진 리스트에서 짝수만 나오게 필터링한 결과 리스트의 모든 원소에 대해 
# 제곱을 수행해서 리스트로 반환하는 코드를 필터와 맵과 람다를 이용해서 작성하시요.


nums = list(range(1, 11))
result = list(map(lambda x: x**2, filter(lambda nums: nums % 2 == 0, nums)))

print(result)   # [4, 16, 36, 64, 100]
