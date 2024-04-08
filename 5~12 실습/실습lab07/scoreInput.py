scoreWrite = []

fileName = input("저장할 파일 이름을 확장자까지 입력:")

f = open(fileName, 'w')

print("국어와 영어 점수를 입력하세요(Enter 입력하여 종료)\n예) 90 85")
while True:
    score = input()
    if score == '':
        break
    
    scoreWrite.append(score)

for score in scoreWrite:
    msg = score + '\n'
    f.write(msg)
    
f.close()

print(fileName, "저장 완료")
