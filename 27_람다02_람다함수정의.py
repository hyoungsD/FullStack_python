
# 일반함수
def add(x, y):
    return x + y

# 람다함수
f = lambda x, y : x + y

print(add(1, 2))
print(f(1, 2))


f = lambda x : x if x % 3 == 0 else 0   # 3으로 나눈 나머지가 0이면 x 반환 아니면 0 반환
print(f(3))
print(f(4))
print(f(6))
