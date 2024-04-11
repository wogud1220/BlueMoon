# 인수들의 합을 계산하는 함수

def sum_times(n, *args):
    sum = 0
    for i in args:
        sum += i
    return n*sum

print(sum_times(2, 1, 2, 3, 4, 5))
print(sum_times(3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))