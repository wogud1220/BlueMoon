# 메뉴 항목을 선택하는 choicebox

import easygui

menu = ["김밥","비빔밥","떡볶기"]
reply = easygui.choicebox("무엇을 드시겠습니까?", choices = menu)
easygui.msgbox (reply + " 주문했습니다.")
