# 성적을 입력받고 정렬하여 출력하는 프로그램

def print_menu():
    print ()
    print ("1. 순위와 평균 보기")
    print ("2. 점수 추가")
    print ("3. 점수 삭제")    
    print ("4. 종료")
    print ()
    print ("선택 : ", end=' ')

def show_ranking():    
    print
    print ("점수 순위")
    print    
    print ("=======================")
    if len(scores)==0:
        print ("빈 리스트")
        return
    
    rank=1
    total = 0
    scores.sort(reverse=True)
    for score in scores:
        print (rank," \t ",score)
        rank+=1
        total +=score
    print ("=======================")
    
    print ("평균 점수 : ",total/len(scores))
    print

def add_score():
    global scores
    
    while 1:
        print ("0..100 사이 점수를 입력하세요 (아니면 종료)")
        score = int(input("점수:"))
        if score < 0 or score > 100: break
        scores.append(score)        
        print (scores)
  

def delete_score():
    global scores

    print (scores)    
    score = int(input("삭제할 점수를 입력하세요 : "))
    if score in scores:
        scores.remove(score)
        print (scores)
    else:
        print ("해당 점수 없음.")        

scores=[]
choice=0
print_menu()
                
while (choice !=4):
    choice = int(input())
    if choice ==1:
        show_ranking()
    elif choice ==2:
        add_score()
    elif choice ==3:
        delete_score()
    elif choice==4:
        break
    print_menu()