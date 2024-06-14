try:
    x = int(input('나눌 숫자를 입력하세요: '))
    print(10 / x)  
except ZeroDivisionError as e: 
    print('숫자를 0으로 나눌 수 없습니다.', e)
except ValueError as e:
    print('입력한 값은 정수가 아닙니다.', e)
