## for ~ in 구문
# input 함수를 이용해서 입력받은 횟수만큼 반복

str_count = input('반복할 횟수를 입력하세요: ')
count = int(str_count)

for i in range(count):
    print('Hello, wrold!', i)


# for 루프를 중첩해서 사용
fruits = ('apple', 'orange', 'grape')
for i in range(10):
    for fruit in fruits:
        print(i, fruit)
