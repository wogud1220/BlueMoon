# 팩토리얼 함수 

def fact(n): 
    if n == 0:
        return 1
    else: 
        return n * fact(n-1)

print(fact(4))
print(fact(20))
