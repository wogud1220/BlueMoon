# 입력을 받을 수 있는 enterbox 

import easygui
lang = easygui.enterbox("좋아하는 프로그래밍 언어는 어느 것입니까?")
easygui.msgbox ("당신은 " + lang + "을 좋아하시는 군요")
