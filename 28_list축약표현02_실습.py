## 축약표현으로 다음의 리스트를 만드시오.
# 1. 1~10까지 숫자의 제곱을 포함하는 리스트
# 2. 1~20까지의 짝수를 포함하는 리스트
# 3. 1~20까지의 숫자중 3의 배수를 포함하는 리스트
# 4. 1~20까지의 숫자중 5의 배수의 제곱을 포함하는 리스트

list1 = [x**2 for x in range(1, 11)]
print(list1)

list2 = [x for x in range(1, 21) if x % 2 == 0]
print(list2)

list3 = [x for x in range(1, 21) if x % 3 == 0]
print(list3)

list4 = [x**2 for x in range(1, 21) if x % 5 == 0]
print(list4)
