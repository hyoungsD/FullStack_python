# try-except-else-finally

str1 = input('젯수를 입력하시오.')
str2 = input('피젯수를 입력하시오.')
try:
    num1 = int(str1)
    num2 = int(str2)
    result = num1 / num2
except Exception as e:
    print('excpetion:', e)
else :
    print('{}/{} = {}'.format(num1, num2, num1/num2))
finally :
    print('처리가 완료되었습니다.')

