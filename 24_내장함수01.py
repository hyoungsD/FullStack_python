## 내장함수
# https:/docs.python.org/3/library/functions.html

max_value = max(1, 30, 50)
print(max_value)    # 50
min_value = min(1, 30, 50)
print(min_value)    # 1
max_str = max('AAC', 'ABC', 'ACC')
print(max_str)  # ACC
min_str = min('AAC', 'ABC', 'ACC')
print(min_str)  # AAC


length = len('안녕하세요')
print(length)   # 5

result = eval('10+20+30+40') # 안의 문자열을 실행
print(result)   # 100

result = eval('not 40 > 50')
print(result)   # True

list = [2, 5, 5, 3, 8, 1]
result = sorted(list)
print(result)   # [1, 2, 3, 5, 5, 8]

str1 = '안녕하세요'
str_id = id(str1)
print(str_id)

list_id = id([1,2,3,4,5])
print(hex(list_id)) # 16진수로
print(oct(list_id))  # 8진수로

print(type(3.14))   # <class 'float'>
print(type([1,2,3,4,5]))    # <class 'list'>

print(abs(-5))  # 5

