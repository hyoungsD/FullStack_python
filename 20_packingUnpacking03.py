# unpacking
# _는 생략

nums = (1, 2, 3)

num1, num2, num3 = nums
print(num1, num2, num3) # 1 2 3

num1, num2, _ = nums
print(num1, num2)   # 1 2

_, _, num3 = nums
print(num3) # 3

