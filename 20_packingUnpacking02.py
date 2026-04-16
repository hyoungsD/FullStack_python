# unpacking

nums = [1, 2, 3, 4, 5]

num1, num2, num3, num4, num5 = nums
print(num1, num2, num3, num4, num5)


# *가 있는 것에 나머지 내용을 List로 넣음

num1, num2, *num3 = nums
print(num1, num2, num3) # 1 2 [3, 4, 5]

*num1, num2, num3 = nums
print(num1, num2, num3)  # [1, 2, 3] 4 5
