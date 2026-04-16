## while 구문

age = 0
while age < 5:
    print('{}살입니다.'.format(age))
    age += 1

age = 0
num = 0
while age < 5 :
    while num < 10 :
        print('{}살입니다.'.format(age))
        num += 1
    num = 0
    age += 1

