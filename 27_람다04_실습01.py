# map과 lambda를 이용해서 1~10 list의 각 아이템에 5배를 가진 list를 만들고 출력하시오.

nums = list(range(1, 11))
result = list(map(lambda x: x * 5, nums))
print(result)   # [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]



