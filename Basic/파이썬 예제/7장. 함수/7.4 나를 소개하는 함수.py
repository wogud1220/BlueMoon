# 나를 소개하는 함수

def myintro(name, univ, grade):
    grade = grade + 1 
    print("나의 이름은 %s입니다." %name) 
    print("%s대학교 %d학년 학생입니다." %(univ, grade)) 

myintro("홍길동", "한국", 1)