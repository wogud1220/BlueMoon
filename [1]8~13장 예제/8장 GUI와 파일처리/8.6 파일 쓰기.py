# 항목을 입력받아 리스트에 저장하고 파일에 출력하는 프로그램

def write_file():
    f = open('memo.txt', 'w') 
    for item in mymemo: 
        msg = item + '\n'   
        f.write(msg) 
    f.close() 

mymemo = [] 
while True: 
    print("Write an item to buy. blank to exit: ") 
    item = input()
    if len(item) == 0: break 
    mymemo.append(item) 

write_file() 
print(len(mymemo), " items are written into file") 
