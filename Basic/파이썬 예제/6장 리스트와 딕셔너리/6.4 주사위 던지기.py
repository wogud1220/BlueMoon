# 주사위를 100번, 1000번, 10000번 각각 던져서 주사위 눈이 나온 횟수를 출혁한다.

import random 
for n in [100, 1000, 10000]:
    print()
    print()
    count = [0, 0, 0, 0, 0, 0]
    print("# of throws : ", n) 
    for i in range(n): 
        eye = random.randint(1, 6) 
        count[eye - 1] = count[eye - 1] + 1 

    print(count) 
    for i in range(len(count)): 
        print("%4.1f" % float(count[i]/n*100),'% ', end=' ') 
