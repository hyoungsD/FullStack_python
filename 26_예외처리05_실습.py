
# test11.txt 파일을 읽기모드로 여는데 예외가 발생했을때 
# '파일을 여는중 예외가 발생했습니다.' 라고 출력하는 코드를작성하시오.


try :
    f = open('test11.txt', 'r')
    text = f.read()
    print(text)
    f.close()
except :
    print('파일을 여는중 예외가 발생했습니다')

