## input()

# 사용자의 입력을 받을때 사용
# 입력값은 문자열로 반환
# input("프롬프트 문자열")


age = input('나이를 입력하시오')
print(age)

num = 3
diff = input('변화량을 입력하시오')
# print(num + diff) # 에러
#TypeError: unsupported operand type(s) for +: 'int' and 'str'

print(num + int(diff))
