# 파일 읽기

f = open('test.txt', 'r')   # r: read, w: write, a: append, r+: read and write
text = f.read()
print(text)
f.close()

# 한줄씩 읽기
with open('test.txt', 'r+') as f:   # 읽어온 것을 f로 저장
    text = f.read()
    print(text)


with open('test.txt', 'r+') as f:
    lines = f.readlines()
    for line in lines:
        print(line, end="")

with open('test1.txt', 'r') as f:
    print(f.readline(), end="")
    print(f.readline(), end="")
    print(f.readline(), end="")
    print(f.readline(), end="")

with open('test1.txt', 'r', encoding='utf8') as f:
    texts = f.readlines()
    for text in texts:
        if not text: break
        print(text, end='')