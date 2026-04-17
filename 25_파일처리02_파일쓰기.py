# file 쓰기

text = '안녕하세요.\n 파이썬입니다.\n 반갑습니다.'
with open('test1.txt', 'w') as f:
    f.write(text)

texts = ["안녕하세요.","파이썬입니다.","반갑습니다."]
with open('test1.txt', 'a') as f:
    f.writelines(texts)


texts = ["안녕하세요.","파이썬입니다.","반갑습니다."]
with open('test1.txt', 'a') as f:
    for text in texts :
        f.writelines(text)
        f.writelines('\n')