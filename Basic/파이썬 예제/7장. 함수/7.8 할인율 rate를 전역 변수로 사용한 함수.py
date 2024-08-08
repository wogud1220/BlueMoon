# 할인 가격 계산 함수를 활용하는 프로그램
rate = 20  

# 할인율을 전역 변수로 사용한 할인 가격 계산 
def salePrice(price): 
    result = price * (1 - rate/100)
    return result

original = int(input("가격을 입력하세요:"))
print("원래 가격:", original)
print(rate, "% 할인 가격:", salePrice(original))
rate = 30
print(rate, "% 할인 가격:", salePrice(original))