y = [10, 20, 30] 
try:
    index = int(input('인덱스를 입력하세요: '))
    x = int(input('나눌 숫자를 입력하세요: '))
    print(y[index] / x)
except ZeroDivisionError as e: 
    print('숫자를 0으로 나눌 수 없습니다: ', e) 
except IndexError as e:
    print('잘못된 인덱스입니다: ', e)
except ValueError as e: 	 
    print('입력한 값은 정수가 아닙니다.')
finally:			 
    print('try 문 수행 완료')
