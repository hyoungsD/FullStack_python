r1 = range(1, 10, 1)    # 1~9까지 1씩 증가하는 범위
print(r1)

r2 = range(10, 20, 2)   # 10~20까지 2씩 증가하는 범위
print(r2)

r3 = range(10, 1)   # start=10, stop=1, step=1로 인식되어 범위가 만들어지지 않는다.
print(r3)

r4 = range(10, 0, -1)   # 10 ~ 1까지 1씩 감소하는 범위
print(r4)

r5 = range(10, 0, -2)   # 10 ~ 1까지 2씩 감소하는 범위
print(r5)
