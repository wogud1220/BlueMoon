# 가격과 할인율을 매개변수로 받아 할인 가격을 출력하는 함수 
def sigma(start = 0 , end = 100): 
    sum = 0 
    for i in range(start, end+1): 
        sum += i 
    return sum 

print(sigma()) 
print(sigma(10))
print(sigma(1, 200))
