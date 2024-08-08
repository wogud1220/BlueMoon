# 전역변수 값 수정 시도

rate = 20

def salePrice(price):
    rate = 30
    result = price * (1 - rate/100)
    return result

print(salePrice(50000))
print(rate)