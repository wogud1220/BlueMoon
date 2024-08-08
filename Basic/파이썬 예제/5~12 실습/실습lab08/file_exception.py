#https://docs.python.org/3/library/exceptions.html#bltin-exceptions
#read, readline 등은 EOF 만나면 빈 문자열을 반환함

fileName = input("텍스트 파일명 입력(확장자 포함):")

try:
    f = open(fileName)
    n = 1
    while True:
        line = f.readline()
        if line == '':
            print("파일의 끝입니다.")
            break

        line = line.strip()
        print("%2d" %n,line)
        n = n + 1

except FileNotFoundError as e:
    print(e)
else:
    f.close()
