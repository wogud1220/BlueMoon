# 파일 내의 단어 출현 횟수 계산 함수 

filename = input("검색할 파일 이름을 입력하세요: ") 
f = open(filename) 
word_counts = {} 
for line in f: 
    list = line.split() 
    for word in list: 
        if word in word_counts: 
            word_counts[word] += 1 
        else: 
            word_counts[word] = 1 
for word in word_counts: 
    print(word, word_counts[word])