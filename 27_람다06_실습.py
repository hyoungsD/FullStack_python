
# 1부터 10 사이의 정수를 가진 리스트에서 
# 짝수만 나오게 필터링한 결과 리스트의 
# 모든 원소의 곱을 구하는 코드를
# lambda, filter, reduce 함수를 사용해서 작성하시요.

from functools import reduce

nums = range(1, 11)

fresult = filter(lambda nums: nums % 2 == 0, nums)
fresult = result = reduce(lambda x, y: x * y, fresult)

# result = reduce(lambda x, y: x * y, filter(lambda nums: nums % 2 == 0, nums))

print(result)   # 3840
