# 10진수를 스택을 이용하여 2진수로 변환하여 출력하기

stack = []
print ("10진수를 입력하세요 ")
num= int(input())
old_num = num
remainder = num % 2
quotient = num // 2

while quotient > 1:
    stack.append(remainder)
    print ("스택의 내용 : ",stack)
    remainder = quotient % 2
    quotient = quotient // 2

if quotient ==1:
    stack.append(remainder)
    stack.append(1)
    
print ("스택의 내용 : ", stack)
print("10진수", old_num,"의 2진수는 ", end=' ')
while stack!=[]:
    print (stack.pop(), end=' ')