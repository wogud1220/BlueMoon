scores = []
while True:
    num = input("숫자를 입력해주세요. 종료=[Enter] : ")
    
    if num == '':
        break
    
    scores.append(int(num))

n = len(scores)

if n == 0:
    print("숫자가 존재하지 않습니다.")
else:
    scores.sort()
    min = scores[0]
    
    print(scores)
    
    scores.sort(reverse = True)
    max = scores[0]
    
    if n % 2 == 1:
        median = scores[n//2]
    elif n % 2 == 0:
        median = (scores[n//2 - 1]+scores[n//2])/2

    print("최대값 :", max)
    print("최소값 :", min)
    print("중간값 :", median)
    
