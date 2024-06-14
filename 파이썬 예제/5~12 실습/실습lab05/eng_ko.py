menu = 0
words = {}
#words = {'serendipity':'우연한발견','impromptu':'즉흥적인','celebrity':'유명인','sporadically':'산발적으로','python':'파이썬'}

while menu != 5:
    print("========영한사전========")
    print("1. 단어 추가\n2. 단어 조회/수정\n3. 단어 삭제\n4. 전체 단어 출력\n5. 종료")
    print("========================")
    menu = int(input("선택 : "))
    print()
    
    if menu == 1:
        while True:
            word = input("단어를 입력하세요. 종료=[Enter] : ")
            if word == '':
                break
            elif word not in words:
                mean = input("뜻을 입력하세요 : ")
                words[word] = mean
            elif word in words:
                print("이미 존재하는 단어입니다")

    elif menu == 2:
        word = input("조회할 단어를 입력하세요. 종료=[Enter] : ")
        if word in words:
            print("단어 :", word, "\n뜻  :", words[word])
            select = input("수정하시겠습니까(y/n) : ")
            while select != 'y' and select != 'n':
                print("잘못된 입력입니다.")
                select = input("수정하시겠습니까(y/n) : ")
            if select == 'y':
                mean = input("단어 : %s\n뜻 : " %word)
                words[word] = mean
                print("수정되었습니다")
        else:
            print(word, "은(는) 사전에 존재하지 않습니다.")

    elif menu == 3:
        word = input("삭제할 단어를 입력하세요. 종료=[Enter] : ")
        if word in words:
            del words[word]
            print(word, "가 삭제되었습니다.")
        elif word not in words:
            print(word, "은(는) 사전에 존재하지 않습니다.")

    elif menu == 4:
        for word in words:
            #print(word, '\t', words[word])
            print('%-15s' %word, words[word])
        print()

    elif menu == 5:
        break
    
    else:
        print("메뉴를 다시 선택해주세요.")
                
