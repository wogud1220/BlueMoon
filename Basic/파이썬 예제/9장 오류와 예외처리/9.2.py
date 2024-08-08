try:
    x = int(input('나눌 숫자를 입력하세요: '))
    print(10 / x)  
except ZeroDivisionError: 
    print('숫자를 0으로 나눌 수 없습니다.')
