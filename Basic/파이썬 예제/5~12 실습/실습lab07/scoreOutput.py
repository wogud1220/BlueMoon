engScore = []
korScore = []
sumScore = []

fileName = input("불러올 파일 이름을 확장자까지 입력: ")
f = open(fileName)

while True:
    line = f.readline()
    if len(line) == 0:
        break
    line = line.strip()
    score = line.split(' ')
    korScore.append(int(score[0]))
    engScore.append(int(score[1]))
    sumScore.append(int(score[0])+int(score[1]))
    
f.close()

korAvg = sum(korScore) / len(korScore)
engAvg = sum(engScore) / len(engScore)

sumMaxId = sumScore.index(max(sumScore))

print("국어 평균: %.2f\n영어 평균: %.2f" %(korAvg, engAvg))
print("합계 최고 점수(국어 영어): %d %d" %(korScore[sumMaxId], engScore[sumMaxId]))
