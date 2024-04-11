# 숫자 맞추기 예제를 easygui로 작성한 프로그램

import easygui
import random

answer = random.randint(1, 100)     
guess = 0
num = easygui.buttonbox("도전 횟수를 선택하세요", choices = ['5', '6', '7'] )

num = int(num)
while guess != answer and num > 0 :     
    guess = easygui.integerbox("1 ~ 100 사이의 숫자를 입력하세요. 도전기회 = "+str(num))
    if guess < answer:
        easygui.msgbox(str(guess)+"는 정답보다 작습니다.")
    elif guess > answer:
        easygui.msgbox(str(guess)+"는 정답보다 큽니다.")
    num = num -1

if guess == answer:             
    easygui.msgbox("정답입니다. 잘 맞추시네요")
else:
     easygui.msgbox("더이상 기회가 없습니다. 정답은 "+ str(answer))
