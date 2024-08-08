# 텍스트 파일을 읽어서 각 문장을 출력하는 프로그램

def read_file():
    f = open('memo.txt') 
    while True: 
        line = f.readline() 
        if len(line) == 0: break 
        line = line.strip()   
        mymemo.append(line) 
    f.close() 

mymemo = [] 
read_file() 
for item in mymemo: 
    msg = item + '\n'
    print(msg) 
