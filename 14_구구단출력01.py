# 원하는 단수를 입력받아 for루프를 이용해서 출력하시요.

dan = int(input('원하는 단수를 입력하세요.'))

for i in range(1, 10):
    print( '{}x{}={}'.format(dan, i, dan * i) )


