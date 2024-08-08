def C(x):
    return 10 / x   # x가 0인 경우 오류 발생

def B(y):
    return C(y - 1)  # y가 1인 경우 오류 발생

def A( ):
    print(B(int(input())))

A( )