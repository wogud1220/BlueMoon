def C(x):
    return 10 / x 	

def B(y):
    return C(y - 1)

def A():
    try:
        print(B(int(input())))
    except ZeroDivisionError:
        print('0으로는 나눌 수 없습니다.')

A ()		# 함수 A 호출 
