# 커피샵의 평점을 입력받아 사전에 저장하고 탐색, 삭제하는 프로그램
def print_menu():
    print('1. 전체 커피숍 평점 보기') 
    print('2. 커피숍 평점 추가') 
    print('3. 커피숍 평점 삭제')
    print('4. 커피숍 찾기') 
    print('5. 종료')

def show_review(reviews):
    print()
    print('커피숍 평점') 
    print()
    print('커피숍 \t 평점 ') 
    print('=======================') 
    for store in reviews:
        print(store, ' \t ', reviews[store]) 
    print('=======================') 
    print()

def add_review(reviews):
    print("새 평점 추가하기")
    store = input("커피숍:")
    grade = float(input("평점 [1...5] :")) 
    while (grade < 1 or grade > 5):
        print("1..5 사이의 평점을 입력하세요")
        grade = float(input("평점 [1...5] :")) 
    reviews[store] = grade
    show_review(reviews)

def delete_review(reviews): 
    print("커피숍 평점 삭제") 
    store = input("커피숍:")
    if store in reviews:
        del reviews[store]
    show_review(reviews)
    
def search_store(reviews): 
    print("커피숍 평점 찾기") 
    store = input("커피숍:")
    if store in reviews:
        print(store, " : ", reviews[store]) 
    else:
        print(store, " 자료 없음")
        
reviews = {}
choice = 0
print_menu()

while True:
    menu = int(input())
    if menu == 1:
        show_review(reviews)
    elif menu == 2:
        add_review(reviews)
    elif menu == 3:
        delete_review(reviews)
    elif menu == 4:
        search_store(reviews)
    if menu == 5:
        break
    print_menu()
