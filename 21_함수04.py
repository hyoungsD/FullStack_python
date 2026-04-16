# 가변 매개변수가 있는 함수, *를 사용

# def 함수이름(매개변수1, *매개변수2):
#     코드
#     return 반환값

def hello4(greeting, *names):
    for name in names:
        print(greeting, name)

hello4('안녕', "진", "슈가", "제이홉", "RM", "지민")
# 안녕 진
# 안녕 슈가
# 안녕 제이홉
# 안녕 RM
# 안녕 지민

# 가변 매개변수는 하나만 사용 가능
# 가변 매개변수는 매개변수중 마지막에만 위치 가능