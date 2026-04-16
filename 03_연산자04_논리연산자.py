# not (ex. no a : a가 True이면 False, False 이면 True 반환 )
# and (ex. a and b : a와 b 모두 True일때 True, 하나라도 False 이면 False)
# or (ex. a or b : a와 b 중 하나라도True일때 True, 둘다 False 이면 False)

print(True and True)    # True
print(True and False)   # False
print(True or False)    # True
print(False or False)   # False
print(not False)        # True
print(5<6 and True)     # True
num1 = 3   
num2 = 5
print(not(num1 > num2)) # True
print(num1 == num2)     # False

