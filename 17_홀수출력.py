# 홀수 출력
# for루프, continue, %(나머지 연산자)를 이용해서 0~10 사이의 홀수를 출력하라.

for i in range(11):   # 0 ~ 10
    if i % 2 == 0:    # 짝수이면
        continue      # 건너뛰기
    print(i)          # 홀수만 출력