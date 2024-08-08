# 파일 길이를 계산하는 함수 
def filecount(filename): 
    file = open(filename) 
    wc = 0 
    lc = 0 
    cc = 0 
    for line in file: 
        lc = lc + 1 
        cc = cc + len(line) 
        list = line.split() 
        wc = wc + len(list) 
    return((lc,wc,cc)) 

x = filecount("raiseup.txt")
print(x)