#전역 변수 변경을 시도하는 프로그램 2

rate = 20

def salePrice(price):
    global rate
    rate = 30
    result = price * (1 - rate/100)
    return result

print(salePrice(50000))
print(rate)

