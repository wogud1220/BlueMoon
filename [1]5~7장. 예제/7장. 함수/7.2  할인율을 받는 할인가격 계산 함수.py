# 가격과 할인율을 매개변수로 받는 할인 가격 계산 함수
def salePrice(price, rate): 
    result = price * (1 - rate/100)
    return result 

print(salePrice(48000, 30))
print(salePrice(120000, 20))
