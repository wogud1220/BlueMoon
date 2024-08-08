def sigma(start = 0 , end = 100):
    sum = 0
    for i in range(start, end+1):
        sum += i
    return sum

print(sigma())