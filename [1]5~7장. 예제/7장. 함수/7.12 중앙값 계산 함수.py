def mean(x):
    return sum(x) / len(x)

# 중간값 계산 함수
def median(x):
    n = len(x)
    x = sorted(x)
    mid = n // 2
    if n % 2 ==1:
        return x[mid]
    else:
        low = mid-1
        high = mid
        return (x[low]+x[high])/2

    
incomes = [8800, 3500, 5600, 7500, 3900, 6000, 5200, 4100, 9000, 6500]

print("mean = ", mean(incomes))
print("median = ", median(incomes))