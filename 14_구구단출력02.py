# 전체구구단을 이중 for루프를 이용해서 출력하시오.

for dan in range(2, 10):
    print('==={}단==='.format(dan))
    for i in range(1, 10):
        print('{} x {} = {}'.format(dan, i, dan*i))
