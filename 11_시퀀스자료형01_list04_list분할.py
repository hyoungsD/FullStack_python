# list 분할

numbers = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 10]


numbers1 = numbers[0:4]
print(numbers1)         # [0, 10, 20, 30]
print(numbers[:4])      # 앞에 0 생략 [0, 10, 20, 30]
print(numbers[7:11])    # [70, 80, 90, 10]
print(numbers[7:])      # 뒤에 len 생략 [70, 80, 90, 10]
print(numbers[:])       # 생략 : 처음부터 끝까지    [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 10]
