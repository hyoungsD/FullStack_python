# try-except

# ZeroDivisionError : 0으로 나눌때 발생
# IndexError : list의 Index의 범위를 벗어날때 발생
# ValueError : 유효하지않은 값이 매개변수로 전달될때 발생
# TypeError : 유효하지않은 Type이 매개변수로 전달될때 발생
# NameError : 존재하지않은 변수를 사용할때 발생
# FileNotFoundError : 존재하지 않은 파일을 열때 발생

str1 = input('피젯수를 입력하시오.')
str2 = input('젯수를 입력하시오.')

try:
    num1 = int(str1)
    num2 = int(str2)
    result = num1 / num2
    print('{}/{} = {}'.format(num1, num2, num1/num2))
except ValueError:
    print('숫자를 입력하시오')
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다')
except Exception as e:
    print('exception: ', e)
