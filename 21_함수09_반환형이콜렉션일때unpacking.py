## 반환형이 콜렉션일때 unpacking

# packing을 사용한 다중 반환값
# def 함수이름():
#     코드
#     return 반환값1, 반환값2, 반환값3

def function():
    return 1, "Hello", True

a, b, c = function()
print(a, b, c)  # 1 Hello True
a = function()
print(a)    # (1, 'Hello', True) : Tuple로 반환


# List 반환했을 때
def ret_list():
    return [1, 2]
l = ret_list()  # [1, 2] : List로 반환
print(l)
n1, n2 = ret_list()
print(n1, n2)   # 1 2
n1, _ = ret_list()
print(n1) # 1


# Tuple 반환했을 때
def ret_tuple():
    return (1, 2)
t = ret_tuple()
print(t)
n1, n2 = ret_tuple()
print(n1, n2)
n1,_ = ret_tuple()
print(n1)


