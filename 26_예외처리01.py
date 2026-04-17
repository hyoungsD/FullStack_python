# try-except


str1 = input('피젯수를 입력하시오')
str2 = input('젲수를 입력하시오')

try:
    num1 = int(str1)
    num2 = int(str2)
    result = num1 / num2
    print('{}/{} = {}'.format(num1, num2, num1/num2))
except:
    print('입력값을 확인하시오')



try:
    num1 = int(str1)
    num2 = int(str2)
    result = num1 / num2
    print('{}/{} = {}'.format(num1, num2, num1/num2))
except Exception as e:
    print('exception: ', e)

