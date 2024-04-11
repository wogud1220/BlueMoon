# 메뉴를 버튼으로 선택하는 buttonbox

import easygui
lang = easygui.buttonbox("좋아하는 프로그래밍 언어는 어느 것입니까?", \
choices = ['C', 'Java', 'Python'])
easygui.msgbox(lang + "를 선택하셨습니다")