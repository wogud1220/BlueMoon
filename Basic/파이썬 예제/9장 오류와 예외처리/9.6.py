try:
   x = int(input('나눌 숫자를 입력하세요: '))
   result = 10 / x
except ZeroDivisionError: # 숫자를 0으로 나눌 때 실행됨
   print('숫자를 0으로 나눌 수 없습니다.')
except ValueError: 	# 범위를 벗어난 인덱스에 접근했을 때 실행됨
   print('입력한 값은 정수가 아닙니다.')
else: 
    print(result)
