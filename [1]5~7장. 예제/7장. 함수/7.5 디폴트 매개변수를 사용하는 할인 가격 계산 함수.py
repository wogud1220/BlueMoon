# 가격과 할인율을 매개변수로 받아 할인 가격을 출력하는 함수

def salePrice(price, rate=10): 
    result = price * (1 - rate/100)
    print("할인 가격:", result) 

salePrice(48000)
