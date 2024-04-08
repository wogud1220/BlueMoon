import easygui
import random

count = 1
comWin = 0
userWin = 0
cases = ['가위', '바위', '보']

while count <= 5 and comWin < 3 and userWin < 3:
    computer = random.randint(1, 3)
    c_in = easygui.buttonbox("%d번째 판\n가위 바위 보 중 하나를 선택하세요" %count, choices=cases)

    if c_in == '가위':
        guess = 1
    elif c_in == '바위':
        guess = 2
    else:
        guess = 3

    diff = guess - computer
    if diff == 0:
        msg = "모두 " + c_in + "을 냈습니다. 비겼습니다."
        #count += 1
    elif diff == -1 or diff == 2:
        msg = "컴퓨터는 " + cases[computer-1] + "을 냈습니다. 당신이 졌습니다."
        comWin += 1
        count += 1
    else:
        msg = "컴퓨터는 " + cases[computer-1] + "을 냈습니다. 당신이 이겼습니다."
        userWin += 1
        count += 1

    msg += '\n' + "컴퓨터 " + str(comWin) + " : " + str(userWin) + " 사용자"
    easygui.msgbox(msg)

    msg = "컴퓨터 " + str(comWin) + " : " + str(userWin) + " 사용자\n"
    if comWin > userWin:
        easygui.msgbox(msg + "컴퓨터가 우승했습니다.")
    elif comWin < userWin:
        easygui.msgbox(msg + "당신이 우승했습니다.")
    else:
        easygui.msgbox(msg + "비겼습니다.")




